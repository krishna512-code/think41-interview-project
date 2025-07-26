# Think41 Interview Project

This is the implementation for the Think41 interview assignment - a conversational AI agent for e-commerce.

## Tech Stack
- **Backend**: FastAPI, SQLAlchemy, SQLite/PostgreSQL
- **LLM**: Groq API (Llama 3 model)
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Data Processing**: Pandas

## Project Structure
```
think41-interview-project/
├── backend/                 # Backend service
│   ├── app/                # FastAPI application
│   ├── scripts/            # Data ingestion scripts
│   ├── data/               # Sample data
│   └── README.md           # Backend documentation
└── README.md               # This file
```

## Milestones Completed
- ✅ **Milestone 2**: Database Setup and Data Ingestion
- ✅ **Milestone 3**: Data Schemas and Backend Service
- ✅ **Milestone 4**: Core Chat API
- ✅ **Milestone 5**: LLM Integration and Business Logic

## Features Implemented

### Backend Service
- **Database Setup**: SQLite database with product catalog
- **Data Ingestion**: CSV data loading script
- **Robust Schema**: Support for users, conversations, and messages
- **Core Chat API**: RESTful chat endpoint with conversation management
- **LLM Integration**: Groq API integration with fallback mock responses
- **Product Search**: Intelligent product search and recommendations

### API Endpoints
- `POST /api/chat` - Core chat functionality
- `GET /api/products` - Product catalog
- `GET /api/conversations/{id}` - Conversation history
- `GET /api/users/{id}/conversations` - User conversations

## Quick Start

### Backend Setup
```bash
git clone https://github.com/krishna512-code/think41-interview-project.git
cd think41-interview-project/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Load sample data
python scripts/load_data.py

# Start server
python run_server.py
```

The backend will be available at `http://localhost:8000`

### Test the API
```bash
# Health check
curl http://localhost:8000/health

# Chat with AI
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "I need a laptop", "user_id": "user123"}'
```

## Documentation
- [Backend Documentation](backend/README.md) - Detailed backend setup and API documentation

## I have completed all milestones and am ready to move forward.

