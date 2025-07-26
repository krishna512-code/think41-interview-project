from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# Product schemas
class ProductBase(BaseModel):
    product_name: str
    category: str
    price: float
    stock_quantity: int
    description: str

class ProductCreate(ProductBase):
    product_id: int

class Product(ProductBase):
    id: int
    product_id: int

    class Config:
        from_attributes = True

# User schemas
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    user_id: str

class User(UserBase):
    id: int
    user_id: str
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True

# Conversation schemas
class ConversationBase(BaseModel):
    title: Optional[str] = None

class ConversationCreate(ConversationBase):
    conversation_id: str
    user_id: str

class Conversation(ConversationBase):
    id: int
    conversation_id: str
    user_id: str
    created_at: datetime
    updated_at: Optional[datetime]
    is_active: bool

    class Config:
        from_attributes = True

# Message schemas
class MessageBase(BaseModel):
    content: str
    role: str  # 'user' or 'assistant'

class MessageCreate(MessageBase):
    message_id: str
    conversation_id: str

class Message(MessageBase):
    id: int
    message_id: str
    conversation_id: str
    created_at: datetime

    class Config:
        from_attributes = True

# Chat request/response schemas
class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None
    user_id: str

class ChatResponse(BaseModel):
    response: str
    conversation_id: str
    message_id: str

# Conversation history response
class ConversationHistory(BaseModel):
    conversation_id: str
    title: Optional[str]
    messages: List[Message]
    created_at: datetime
    updated_at: Optional[datetime] 