import os
import groq
from sqlalchemy.orm import Session
from .models import Product
from typing import List
import json

class LLMService:
    def __init__(self):
        # Initialize Groq client
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            print("Warning: GROQ_API_KEY not found. Using mock responses.")
            self.client = None
        else:
            self.client = groq.Groq(api_key=api_key)
    
    def get_products_info(self, db: Session) -> str:
        """Get formatted product information for the LLM context"""
        products = db.query(Product).all()
        if not products:
            return "No products available in the database."
        
        product_info = []
        for product in products:
            product_info.append({
                "product_id": product.product_id,
                "name": product.product_name,
                "category": product.category,
                "price": product.price,
                "stock": product.stock_quantity,
                "description": product.description
            })
        
        return json.dumps(product_info, indent=2)
    
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
        """Get AI response using Groq LLM"""
        
        # Get product information
        products_info = self.get_products_info(db)
        
        # Create system prompt
        system_prompt = f"""You are a helpful e-commerce assistant. You have access to the following product information:

{products_info}

Your role is to:
1. Help customers find products they're looking for
2. Provide detailed information about products
3. Ask clarifying questions when needed to better understand customer needs
4. Be friendly and professional
5. If a customer asks about a product that doesn't exist, politely inform them and suggest similar alternatives

Always respond in a helpful and conversational manner. If you need more information to help the customer, ask specific questions."""
        
        # If no Groq client available, use mock responses
        if not self.client:
            return self._get_mock_response(user_message, db)
        
        try:
            # Create chat completion
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                model="llama3-8b-8192",  # Using Llama 3 model
                temperature=0.7,
                max_tokens=1000
            )
            
            return chat_completion.choices[0].message.content
            
        except Exception as e:
            print(f"Error calling Groq API: {e}")
            return self._get_mock_response(user_message, db)
    
    def _get_mock_response(self, user_message: str, db: Session) -> str:
        """Provide mock responses when Groq API is not available"""
        user_message_lower = user_message.lower()
        
        # Search for relevant products
        products = self.search_products(user_message, db)
        
        if "laptop" in user_message_lower or "computer" in user_message_lower:
            laptop_products = [p for p in products if "laptop" in p.product_name.lower()]
            if laptop_products:
                product = laptop_products[0]
                return f"I found a great laptop for you! The {product.product_name} is priced at ${product.price} and is currently in stock ({product.stock_quantity} available). {product.description}"
            else:
                # Check all products for laptops
                all_products = db.query(Product).all()
                laptop_products = [p for p in all_products if "laptop" in p.product_name.lower()]
                if laptop_products:
                    product = laptop_products[0]
                    return f"I found a great laptop for you! The {product.product_name} is priced at ${product.price} and is currently in stock ({product.stock_quantity} available). {product.description}"
                else:
                    return "I don't see any laptops in our current inventory. Would you like me to show you other electronics we have available?"
        
        elif "headphone" in user_message_lower or "earphone" in user_message_lower:
            headphone_products = [p for p in products if "headphone" in p.product_name.lower()]
            if headphone_products:
                product = headphone_products[0]
                return f"Great choice! We have the {product.product_name} available for ${product.price}. {product.description} We currently have {product.stock_quantity} in stock."
            else:
                return "I don't see any headphones in our current inventory. Would you like me to show you other audio equipment we have?"
        
        elif "phone" in user_message_lower or "smartphone" in user_message_lower:
            phone_products = [p for p in products if "phone" in p.product_name.lower()]
            if phone_products:
                product = phone_products[0]
                return f"Perfect! We have the {product.product_name} available for ${product.price}. {product.description} We have {product.stock_quantity} units in stock."
            else:
                return "I don't see any smartphones in our current inventory. Would you like me to show you other electronics we have available?"
        
        elif "price" in user_message_lower or "cost" in user_message_lower:
            if products:
                product = products[0]
                return f"The {product.product_name} is priced at ${product.price}. {product.description}"
            else:
                return "I'd be happy to help you with pricing information! Could you please specify which product you're interested in?"
        
        elif "stock" in user_message_lower or "available" in user_message_lower:
            if products:
                product = products[0]
                return f"The {product.product_name} is currently in stock with {product.stock_quantity} units available."
            else:
                return "I'd be happy to check stock availability for you! Could you please specify which product you're interested in?"
        
        elif "category" in user_message_lower or "type" in user_message_lower:
            categories = db.query(Product.category).distinct().all()
            category_list = [cat[0] for cat in categories]
            return f"We have products in the following categories: {', '.join(category_list)}. Which category interests you?"
        
        elif "help" in user_message_lower or "what" in user_message_lower:
            return "I'm here to help you find the perfect products! I can help you with:\n- Product information and pricing\n- Stock availability\n- Product categories\n- Product recommendations\n\nWhat are you looking for today?"
        
        else:
            if products:
                product = products[0]
                return f"I found a product that might interest you: {product.product_name} for ${product.price}. {product.description} Would you like to know more about this product?"
            else:
                return "I'd be happy to help you find what you're looking for! Could you please provide more details about what you're interested in? I can help you with electronics, home & garden items, sports equipment, and more." 