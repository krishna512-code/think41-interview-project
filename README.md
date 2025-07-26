# Conversational AI E-commerce Assistant

A full-stack conversational AI application that helps customers find products, answer questions about inventory, pricing, and features. Built with React frontend, FastAPI backend, and SQLite database.

## Features

- **AI-Powered Chat Interface**: Interactive chat with an AI assistant that can help with product recommendations
- **Product Search**: Intelligent product search based on user queries
- **Conversation History**: Persistent conversation history with the ability to view past conversations
- **Real-time Responses**: Fast, responsive chat interface
- **Product Database**: Comprehensive product catalog with detailed information

## Tech Stack

### Frontend
- React 19.1.0 with TypeScript
- Axios for API communication
- Modern CSS with responsive design
- Context API for state management

### Backend
- FastAPI (Python 3.9)
- SQLAlchemy ORM
- SQLite database (configurable to PostgreSQL)
- Groq LLM integration with fallback mock responses
- CORS middleware for cross-origin requests

### Infrastructure
- Docker and Docker Compose for containerization
- Multi-stage builds for optimized production images

## Project Structure

```
think41-interview-project/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI application
│   │   ├── database.py      # Database configuration
│   │   ├── models.py        # SQLAlchemy models
│   │   ├── schemas.py       # Pydantic schemas
│   │   └── llm_service.py   # AI service integration
│   ├── data/
│   │   └── products.csv     # Product data
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile          # Backend container
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── contexts/        # React contexts
│   │   ├── services/        # API services
│   │   ├── types/          # TypeScript types
│   │   └── App.tsx         # Main application
│   ├── package.json        # Node.js dependencies
│   └── Dockerfile          # Frontend container
├── docker-compose.yml      # Multi-service orchestration
└── README.md              # This file
```

## Quick Start with Docker

### Prerequisites
- Docker
- Docker Compose

### Running the Application

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd think41-interview-project
   ```

2. **Start all services**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Development Setup

### Backend Development

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server**
   ```bash
   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Development

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm start
   ```

## API Endpoints

### Chat API
- `POST /api/chat` - Send a message and get AI response
- `GET /api/conversations/{conversation_id}` - Get conversation history
- `GET /api/users/{user_id}/conversations` - Get user's conversations

### Product API
- `GET /api/products` - Get all products
- `GET /api/products/{product_id}` - Get specific product
- `GET /api/products/category/{category}` - Get products by category

### Health Check
- `GET /health` - Service health status

## Environment Variables

### Backend
- `DATABASE_URL`: Database connection string (default: SQLite)
- `GROQ_API_KEY`: Groq API key for LLM service

### Frontend
- `REACT_APP_API_URL`: Backend API URL (default: http://localhost:8000)

## Database

The application uses SQLite by default for development. The database file is created automatically at `backend/chatbot.db`.

### Loading Sample Data

Sample product data is included in `backend/data/products.csv`. The database is initialized automatically when the application starts.

## Testing the Application

1. **Start the application** using Docker Compose or development servers
2. **Open the frontend** at http://localhost:3000
3. **Start a conversation** by typing a message like:
   - "I need help finding a laptop"
   - "What smartphones do you have?"
   - "Show me headphones under $100"

## Deployment

### Production Deployment

1. **Build production images**
   ```bash
   docker-compose -f docker-compose.prod.yml up --build
   ```

2. **Environment configuration**
   - Set production environment variables
   - Configure database connection
   - Set up reverse proxy (nginx)

### Cloud Deployment

The application can be deployed to:
- AWS ECS/Fargate
- Google Cloud Run
- Azure Container Instances
- Heroku (with modifications)

## Troubleshooting

### Common Issues

1. **Port conflicts**: Ensure ports 3000 and 8000 are available
2. **Database issues**: Check database file permissions
3. **CORS errors**: Verify CORS configuration in backend
4. **API connection**: Check REACT_APP_API_URL environment variable

### Logs

View application logs:
```bash
# Docker Compose
docker-compose logs -f

# Individual services
docker-compose logs -f backend
docker-compose logs -f frontend
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions, please open an issue in the repository.

