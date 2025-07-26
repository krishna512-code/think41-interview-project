# Frontend Application - E-commerce AI Assistant

This is the React frontend application for the Think41 interview project - a conversational AI agent for e-commerce.

## Features

- **Modern UI Components**: Clean, responsive design with smooth animations
- **Real-time Chat**: Instant messaging with AI assistant
- **Conversation History**: Side panel to view and switch between past conversations
- **State Management**: React Context API with useReducer for efficient state management
- **API Integration**: Seamless communication with the backend service
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices

## Tech Stack

- **Framework**: React 18 with TypeScript
- **State Management**: React Context API + useReducer
- **Styling**: CSS3 with modern design patterns
- **HTTP Client**: Axios for API communication
- **Build Tool**: Create React App

## Project Structure

```
frontend/
├── public/                 # Static assets
├── src/
│   ├── components/         # UI Components
│   │   ├── ChatWindow.tsx      # Main chat interface
│   │   ├── MessageList.tsx     # Message display component
│   │   ├── Message.tsx         # Individual message component
│   │   ├── UserInput.tsx       # Message input component
│   │   └── ConversationHistory.tsx # Conversation history panel
│   ├── contexts/           # State Management
│   │   └── ChatContext.tsx     # Chat state and logic
│   ├── services/           # API Services
│   │   └── api.ts             # Backend API communication
│   ├── types/              # TypeScript Types
│   │   └── chat.ts            # Chat-related type definitions
│   └── App.tsx             # Main application component
├── package.json           # Dependencies and scripts
└── README.md             # This file
```

## Setup Instructions

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn
- Backend service running (see backend README)

### Installation

1. **Install Dependencies**:
```bash
npm install
```

2. **Configure Environment** (Optional):
Create a `.env` file in the frontend directory:
```env
REACT_APP_API_URL=http://localhost:8000
```

3. **Start Development Server**:
```bash
npm start
```

The application will be available at `http://localhost:3000`

### Build for Production

```bash
npm run build
```

## Component Architecture

### Core Components

#### ChatWindow
- **Purpose**: Main container orchestrating the entire chat interface
- **Features**: Header, message list, user input, and conversation history panel
- **Props**: Messages, loading state, conversation data, event handlers

#### MessageList
- **Purpose**: Renders a scrollable list of messages
- **Features**: Auto-scroll to bottom, loading indicator, smooth animations
- **Props**: Messages array, loading state

#### Message
- **Purpose**: Individual message display
- **Features**: Different styling for user and AI messages, timestamps, avatars
- **Props**: Content, role, timestamp

#### UserInput
- **Purpose**: Controlled form for user message input
- **Features**: Send button, Enter key support, disabled state during loading
- **Props**: Send handler, disabled state, placeholder text

#### ConversationHistory
- **Purpose**: Side panel displaying past conversations
- **Features**: Conversation list, new chat button, mobile-responsive overlay
- **Props**: Conversations array, selection handlers, open/close state

### State Management

The application uses React Context API with useReducer for state management:

#### ChatState
```typescript
interface ChatState {
  messages: Message[];
  isLoading: boolean;
  currentConversationId?: string;
  conversations: Conversation[];
  userInput: string;
}
```

#### Actions
- `SET_LOADING`: Toggle loading state
- `ADD_MESSAGE`: Add new message to conversation
- `SET_MESSAGES`: Replace all messages (for loading conversation)
- `SET_CONVERSATION_ID`: Update current conversation
- `SET_CONVERSATIONS`: Update conversation list
- `SET_USER_INPUT`: Update input field
- `CLEAR_MESSAGES`: Clear current conversation

## API Integration

The frontend communicates with the backend through the `api.ts` service:

### Endpoints Used
- `POST /api/chat` - Send message and get AI response
- `GET /api/conversations/{id}` - Get conversation history
- `GET /api/users/{id}/conversations` - Get user's conversations

### Error Handling
- Network errors are caught and displayed as user-friendly messages
- Loading states prevent multiple simultaneous requests
- Graceful fallbacks for missing data

## Styling

### Design System
- **Colors**: Purple gradient theme (#667eea to #764ba2)
- **Typography**: System fonts with proper hierarchy
- **Spacing**: Consistent 8px grid system
- **Animations**: Smooth transitions and hover effects

### Responsive Design
- **Desktop**: Full-width layout with side panel
- **Tablet**: Adaptive layout with collapsible sidebar
- **Mobile**: Stacked layout with overlay navigation

### CSS Features
- CSS Grid and Flexbox for layouts
- CSS Custom Properties for theming
- Smooth animations and transitions
- Custom scrollbars
- Mobile-first responsive design

## Development

### Available Scripts

- `npm start` - Start development server
- `npm test` - Run test suite
- `npm run build` - Build for production
- `npm run eject` - Eject from Create React App

### Code Style
- TypeScript for type safety
- Functional components with hooks
- Consistent naming conventions
- Proper prop interfaces
- Error boundaries and loading states

## Testing

The application includes:
- Component testing with React Testing Library
- Type checking with TypeScript
- Linting with ESLint
- Code formatting with Prettier

## Deployment

### Build Process
1. Run `npm run build`
2. Deploy the `build/` folder to your hosting service
3. Configure environment variables for production API URL

### Environment Variables
- `REACT_APP_API_URL`: Backend API base URL

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- Lazy loading for components
- Optimized bundle size
- Efficient re-renders with React.memo
- Debounced API calls
- Proper cleanup in useEffect hooks

## Accessibility

- Semantic HTML structure
- ARIA labels and roles
- Keyboard navigation support
- Screen reader compatibility
- High contrast mode support

## Future Enhancements

- Real-time notifications
- File upload support
- Voice input/output
- Advanced search functionality
- User authentication
- Dark mode theme
- Offline support with service workers
