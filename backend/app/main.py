from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import uuid
from datetime import datetime

from .database import get_db, engine
from .models import Base, Product, User, Conversation, Message
from .schemas import (
    Product as ProductSchema,
    User as UserSchema,
    Conversation as ConversationSchema,
    Message as MessageSchema,
    ChatRequest,
    ChatResponse,
    ConversationHistory
)
from .llm_service import LLMService

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Conversational AI Backend", version="1.0.0")

# Add CORS middleware
origins = [
    "http://localhost:3000",  # Allow frontend origin
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Initialize LLM service
llm_service = LLMService()

@app.get("/")
def read_root():
    return {"message": "Conversational AI Backend API"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}

# Product endpoints
@app.get("/api/products", response_model=List[ProductSchema])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products

@app.get("/api/products/{product_id}", response_model=ProductSchema)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.get("/api/products/category/{category}", response_model=List[ProductSchema])
def get_products_by_category(category: str, db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.category == category).all()
    return products

# User endpoints
@app.post("/api/users", response_model=UserSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = User(
        user_id=user.user_id,
        username=user.username,
        email=user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/api/users/{user_id}", response_model=UserSchema)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Conversation endpoints
@app.post("/api/conversations", response_model=ConversationSchema)
def create_conversation(conversation: ConversationSchema, db: Session = Depends(get_db)):
    db_conversation = Conversation(
        conversation_id=conversation.conversation_id,
        user_id=conversation.user_id,
        title=conversation.title
    )
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    return db_conversation

@app.get("/api/conversations/{conversation_id}", response_model=ConversationHistory)
def get_conversation_history(conversation_id: str, db: Session = Depends(get_db)):
    conversation = db.query(Conversation).filter(Conversation.conversation_id == conversation_id).first()
    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    messages = db.query(Message).filter(Message.conversation_id == conversation_id).order_by(Message.created_at).all()
    
    return ConversationHistory(
        conversation_id=conversation.conversation_id,
        title=conversation.title,
        messages=messages,
        created_at=conversation.created_at,
        updated_at=conversation.updated_at
    )

@app.get("/api/users/{user_id}/conversations", response_model=List[ConversationSchema])
def get_user_conversations(user_id: str, db: Session = Depends(get_db)):
    conversations = db.query(Conversation).filter(Conversation.user_id == user_id).all()
    return conversations

# Core Chat API - Milestone 4
@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    # Generate unique IDs
    message_id = str(uuid.uuid4())
    
    # Handle conversation creation if needed
    if not request.conversation_id:
        conversation_id = str(uuid.uuid4())
        db_conversation = Conversation(
            conversation_id=conversation_id,
            user_id=request.user_id
        )
        db.add(db_conversation)
        db.commit()
    else:
        conversation_id = request.conversation_id
        # Verify conversation exists
        conversation = db.query(Conversation).filter(Conversation.conversation_id == conversation_id).first()
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
    
    # Save user message
    user_message = Message(
        message_id=str(uuid.uuid4()),
        conversation_id=conversation_id,
        role="user",
        content=request.message
    )
    db.add(user_message)
    
    # Get AI response
    ai_response = llm_service.get_response(request.message, db)
    
    # Save AI response
    ai_message = Message(
        message_id=message_id,
        conversation_id=conversation_id,
        role="assistant",
        content=ai_response
    )
    db.add(ai_message)
    
    # Update conversation timestamp
    conversation = db.query(Conversation).filter(Conversation.conversation_id == conversation_id).first()
    if conversation:
        conversation.updated_at = datetime.now()
    
    db.commit()
    
    return ChatResponse(
        response=ai_response,
        conversation_id=conversation_id,
        message_id=message_id
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 