# Think41 Interview Project

This is the implementation for the Think41 interview assignment - a conversational AI agent for e-commerce.

## Tech Stack
- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: React 18, TypeScript, CSS3, Nginx
- **LLM**: Groq API (Llama 3 model)
- **Database**: PostgreSQL
- **Data Processing**: Pandas
- **Containerization**: Docker, Docker Compose

## Project Structure
```
think41-interview-project/
├── backend/                 # Backend service
│   ├── app/                # FastAPI application
│   ├── scripts/            # Data ingestion scripts
│   ├── data/               # Sample data
│   ├── Dockerfile          # Dockerfile for backend
│   └── README.md           # Backend documentation
├── frontend/                # React frontend application
│   ├── src/                # React source code
│   ├── public/             # Static assets
│   ├── Dockerfile          # Dockerfile for frontend
│   └── README.md           # Frontend documentation
├── docker-compose.yml      # Docker Compose file
└── README.md               # This file
```

## Milestones Completed
- ✅ **Milestone 2**: Database Setup and Data Ingestion
- ✅ **Milestone 3**: Data Schemas and Backend Service
- ✅ **Milestone 4**: Core Chat API
- ✅ **Milestone 5**: LLM Integration and Business Logic
- ✅ **Milestone 6**: Core Chat UI Components
- ✅ **Milestone 7**: Client-Side State Management
- ✅ **Milestone 8**: Conversation History Panel
- ✅ **Milestone 9**: Full-Stack Integration
- ✅ **Milestone 10**: Dockerization

## Features Implemented

### Backend Service
- **Database Setup**: PostgreSQL database with product catalog
- **Data Ingestion**: CSV data loading script
- **Robust Schema**: Support for users, conversations, and messages
- **Core Chat API**: RESTful chat endpoint with conversation management
- **LLM Integration**: Groq API integration with fallback mock responses
- **Product Search**: Intelligent product search and recommendations
- **CORS Configuration**: Enabled for frontend communication

### Frontend Application
- **Modern UI Components**: Clean, responsive design with smooth animations
- **Real-time Chat**: Instant messaging with AI assistant
- **Conversation History**: Side panel to view and switch between past conversations
- **State Management**: React Context API with useReducer for efficient state management
- **API Integration**: Seamless communication with the backend service
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices

### API Endpoints
- `POST /api/chat` - Core chat functionality
- `GET /api/products` - Product catalog
- `GET /api/conversations/{id}` - Conversation history
- `GET /api/users/{id}/conversations` - User conversations

## Quick Start (Docker Compose)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/krishna512-code/think41-interview-project.git
   cd think41-interview-project
   ```

2. **Build and run the containers:**
   ```bash
   docker-compose up --build
   ```

This will build the backend and frontend images, start the database, backend, and frontend services. The frontend will be accessible at `http://localhost:3000`.

3. **Load sample data (if needed):**
   You can execute the load data script within the backend container:
   ```bash
   docker-compose exec backend python scripts/load_data.py
   ```

## Documentation
- [Backend Documentation](backend/README.md) - Detailed backend setup and API documentation
- [Frontend Documentation](frontend/README.md) - Frontend setup and component documentation

## I have completed all milestones and am ready to move forward.
