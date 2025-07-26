import os
from typing import List
from sqlalchemy.orm import Session
from .models import Product
import groq
from dotenv import load_dotenv

load_dotenv()

class LLMService:
    def __init__(self):
        # Use environment variable for API key
        self.api_key = os.getenv("GROQ_API_KEY")
        try:
            if self.api_key:
                self.client = groq.Groq(api_key=self.api_key)
                self.model = "llama3-8b-8192"  # Using Llama 3 model
            else:
                print("Warning: GROQ_API_KEY not found in environment variables")
                self.client = None
                self.model = None
        except Exception as e:
            print(f"Warning: Could not initialize Groq client: {e}")
            self.client = None
            self.model = None
        
    def get_products_info(self, products: List[Product]) -> str:
        """Get formatted product information for LLM context"""
        if not products:
            return "No products found in the database."
        
        product_info = []
        for product in products:
            info = f"- {product.product_name} (${product.price}): {product.description}. Stock: {product.stock_quantity}"
            product_info.append(info)
        
        return "\n".join(product_info)

    def search_products(self, query: str, db: Session) -> List[Product]:
        """Search products based on user query"""
        query_lower = query.lower()
        # Split query into words for better matching
        query_words = query_lower.split()
        
        products = []
        for word in query_words:
            if len(word) > 2:  # Only search for words longer than 2 characters
                word_products = db.query(Product).filter(
                    (Product.product_name.ilike(f"%{word}%")) |
                    (Product.category.ilike(f"%{word}%")) |
                    (Product.description.ilike(f"%{word}%"))
                ).all()
                products.extend(word_products)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_products = []
        for product in products:
            if product.id not in seen:
                seen.add(product.id)
                unique_products.append(product)
        
        return unique_products

    def get_response(self, user_message: str, db: Session) -> str:
        """Get AI response using Groq API with fallback to mock response"""
        # If Groq client is not available, use mock response
        if not self.client or not self.model:
            return self._get_mock_response(user_message, db)
            
        try:
            # Search for relevant products
            products = self.search_products(user_message, db)
            products_info = self.get_products_info(products)
            
            # Create system prompt
            system_prompt = f"""You are a helpful e-commerce AI assistant. You have access to the following product information:

{products_info}

Please help customers find products, answer questions about inventory, pricing, and features. Be friendly, informative, and helpful. If you don't have information about a specific product, let the customer know and suggest alternatives if available."""

            # Create user prompt
            user_prompt = f"Customer message: {user_message}"

            # Call Groq API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"Error calling Groq API: {e}")
            # Fallback to mock response
            return self._get_mock_response(user_message, db)

    def _get_mock_response(self, user_message: str, db: Session) -> str:
        """Fallback mock response when API is unavailable"""
        user_message_lower = user_message.lower()
        products = self.search_products(user_message, db)
        
        # Check all products if initial search is empty
        if not products:
            all_products = db.query(Product).all()
            if "laptop" in user_message_lower or "computer" in user_message_lower:
                laptop_products = [p for p in all_products if "laptop" in p.product_name.lower()]
                if laptop_products:
                    product = laptop_products[0]
                    return f"I found a great laptop for you! The {product.product_name} is priced at ${product.price} and is currently in stock ({product.stock_quantity} available). {product.description}"
                else:
                    return "I don't see any laptops in our current inventory. Would you like me to show you other electronics we have available?"
        
        if products:
            product = products[0]
            return f"I found a great product for you! The {product.product_name} is priced at ${product.price} and is currently in stock ({product.stock_quantity} available). {product.description}"
        
        return "I'm here to help you find the perfect product! Could you tell me more about what you're looking for? I can help with laptops, smartphones, headphones, and other electronics." 