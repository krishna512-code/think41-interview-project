# Conversational AI Backend Service

This is the backend service for the Think41 interview project - a conversational AI agent for e-commerce.

## Features

- **Database Setup**: SQLite database with product catalog
- **Data Ingestion**: CSV data loading script
- **Robust Schema**: Support for users, conversations, and messages
- **Core Chat API**: RESTful chat endpoint with conversation management
- **LLM Integration**: Groq API integration with fallback mock responses
- **Product Search**: Intelligent product search and recommendations

## Tech Stack

- **Framework**: FastAPI
- **Database**: SQLite (configurable for PostgreSQL)
- **ORM**: SQLAlchemy
- **LLM**: Groq API (Llama 3 model)
- **Data Processing**: Pandas

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── database.py      # Database configuration
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   └── llm_service.py   # LLM integration
├── scripts/
│   └── load_data.py     # Data ingestion script
├── data/
│   └── products.csv     # Sample product data
├── requirements.txt     # Python dependencies
├── run_server.py        # Server startup script
└── README.md           # This file
```

## Setup Instructions

### 1. Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Set Up Database

```bash
# Load sample data
python scripts/load_data.py
```

### 3. Configure Environment Variables (Optional)

Create a `.env` file in the backend directory:

```env
GROQ_API_KEY=your_groq_api_key_here
DATABASE_URL=sqlite:///./chatbot.db
```

### 4. Run the Server

```bash
# Start the server
python run_server.py
```

The server will be available at `http://localhost:8000`

## API Endpoints

### Health Check
- `GET /health` - Server health status

### Products
- `GET /api/products` - Get all products
- `GET /api/products/{product_id}` - Get specific product
- `GET /api/products/category/{category}` - Get products by category

### Users
- `POST /api/users` - Create new user
- `GET /api/users/{user_id}` - Get user information

### Conversations
- `POST /api/conversations` - Create new conversation
- `GET /api/conversations/{conversation_id}` - Get conversation history
- `GET /api/users/{user_id}/conversations` - Get user's conversations

### Chat (Core Feature)
- `POST /api/chat` - Send message and get AI response

#### Chat Request Format:
```json
{
  "message": "I need a laptop",
  "user_id": "user123",
  "conversation_id": "optional-existing-conversation-id"
}
```

#### Chat Response Format:
```json
{
  "response": "I found a great laptop for you! The Laptop Pro is priced at $1299.99...",
  "conversation_id": "generated-conversation-id",
  "message_id": "generated-message-id"
}
```

## Database Schema

### Products Table
- `id` (Primary Key)
- `product_id` (Unique)
- `product_name`
- `category`
- `price`
- `stock_quantity`
- `description`

### Users Table
- `id` (Primary Key)
- `user_id` (Unique)
- `username`
- `email`
- `created_at`
- `is_active`

### Conversations Table
- `id` (Primary Key)
- `conversation_id` (Unique)
- `user_id` (Foreign Key)
- `title`
- `created_at`
- `updated_at`
- `is_active`

### Messages Table
- `id` (Primary Key)
- `conversation_id` (Foreign Key)
- `message_id` (Unique)
- `role` ('user' or 'assistant')
- `content`
- `created_at`

## LLM Integration

The service integrates with Groq API using the Llama 3 model. If no API key is provided, it falls back to intelligent mock responses based on the product database.

### Features:
- Product-aware responses
- Contextual recommendations
- Clarifying questions
- Stock and pricing information

## Testing

### Test the API

1. **Health Check**:
```bash
curl http://localhost:8000/health
```

2. **Get Products**:
```bash
curl http://localhost:8000/api/products
```

3. **Chat with AI**:
```bash
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "I need a laptop", "user_id": "user123"}'
```

4. **Get Conversation History**:
```bash
curl http://localhost:8000/api/conversations/{conversation_id}
```

## Milestones Completed

- ✅ **Milestone 2**: Database Setup and Data Ingestion
- ✅ **Milestone 3**: Data Schemas and Backend Service
- ✅ **Milestone 4**: Core Chat API
- ✅ **Milestone 5**: LLM Integration and Business Logic

## Development

### Adding New Products

1. Update `data/products.csv` with new product data
2. Run the data loading script:
```bash
python scripts/load_data.py
```

### Customizing LLM Responses

Modify the `LLMService` class in `app/llm_service.py` to customize:
- System prompts
- Response logic
- Product search algorithms

### Database Migrations

For production, consider using Alembic for database migrations:
```bash
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

## Production Deployment

For production deployment:

1. Use PostgreSQL instead of SQLite
2. Set up proper environment variables
3. Configure CORS settings
4. Add authentication middleware
5. Set up logging and monitoring
6. Use a production ASGI server like Gunicorn

## License

This project is part of the Think41 interview assignment. 