import React, { createContext, useContext, useReducer, ReactNode } from 'react';
import { ChatState, ChatContextType, Message, Conversation } from '../types/chat';
import { chatAPI } from '../services/api';

// Initial state
const initialState: ChatState = {
  messages: [],
  isLoading: false,
  currentConversationId: undefined,
  conversations: [],
  userInput: '',
};

// Action types
type ChatAction =
  | { type: 'SET_LOADING'; payload: boolean }
  | { type: 'ADD_MESSAGE'; payload: Message }
  | { type: 'SET_MESSAGES'; payload: Message[] }
  | { type: 'SET_CONVERSATION_ID'; payload: string | undefined }
  | { type: 'SET_CONVERSATIONS'; payload: Conversation[] }
  | { type: 'SET_USER_INPUT'; payload: string }
  | { type: 'CLEAR_MESSAGES' };

// Reducer function
const chatReducer = (state: ChatState, action: ChatAction): ChatState => {
  switch (action.type) {
    case 'SET_LOADING':
      return { ...state, isLoading: action.payload };
    
    case 'ADD_MESSAGE':
      return { 
        ...state, 
        messages: [...state.messages, action.payload] 
      };
    
    case 'SET_MESSAGES':
      return { ...state, messages: action.payload };
    
    case 'SET_CONVERSATION_ID':
      return { ...state, currentConversationId: action.payload };
    
    case 'SET_CONVERSATIONS':
      return { ...state, conversations: action.payload };
    
    case 'SET_USER_INPUT':
      return { ...state, userInput: action.payload };
    
    case 'CLEAR_MESSAGES':
      return { ...state, messages: [] };
    
    default:
      return state;
  }
};

// Create context
const ChatContext = createContext<ChatContextType | undefined>(undefined);

// Provider component
export const ChatProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [state, dispatch] = useReducer(chatReducer, initialState);

  // Generate a simple user ID (in a real app, this would come from authentication)
  const userId = 'user123';

  const sendMessage = async (message: string) => {
    try {
      dispatch({ type: 'SET_LOADING', payload: true });
      
      // Add user message to state immediately
      const userMessage: Message = {
        content: message,
        role: 'user',
        timestamp: new Date().toISOString(),
      };
      dispatch({ type: 'ADD_MESSAGE', payload: userMessage });

      // Send message to API
      const response = await chatAPI.sendMessage({
        message,
        conversation_id: state.currentConversationId,
        user_id: userId,
      });

      // Add AI response to state
      const aiMessage: Message = {
        content: response.response,
        role: 'assistant',
        timestamp: new Date().toISOString(),
      };
      dispatch({ type: 'ADD_MESSAGE', payload: aiMessage });

      // Update conversation ID if this is a new conversation
      if (!state.currentConversationId) {
        dispatch({ type: 'SET_CONVERSATION_ID', payload: response.conversation_id });
      }

    } catch (error) {
      console.error('Error sending message:', error);
      
      // Add error message
      const errorMessage: Message = {
        content: 'Sorry, I encountered an error. Please try again.',
        role: 'assistant',
        timestamp: new Date().toISOString(),
      };
      dispatch({ type: 'ADD_MESSAGE', payload: errorMessage });
    } finally {
      dispatch({ type: 'SET_LOADING', payload: false });
    }
  };

  const startNewConversation = () => {
    dispatch({ type: 'CLEAR_MESSAGES' });
    dispatch({ type: 'SET_CONVERSATION_ID', payload: undefined });
  };

  const loadConversation = async (conversationId: string) => {
    try {
      dispatch({ type: 'SET_LOADING', payload: true });
      
      const conversation = await chatAPI.getConversationHistory(conversationId);
      
      dispatch({ type: 'SET_MESSAGES', payload: conversation.messages });
      dispatch({ type: 'SET_CONVERSATION_ID', payload: conversationId });
      
    } catch (error) {
      console.error('Error loading conversation:', error);
    } finally {
      dispatch({ type: 'SET_LOADING', payload: false });
    }
  };

  const setUserInput = (input: string) => {
    dispatch({ type: 'SET_USER_INPUT', payload: input });
  };

  const value: ChatContextType = {
    state,
    sendMessage,
    startNewConversation,
    loadConversation,
    setUserInput,
  };

  return (
    <ChatContext.Provider value={value}>
      {children}
    </ChatContext.Provider>
  );
};

// Custom hook to use the chat context
export const useChat = (): ChatContextType => {
  const context = useContext(ChatContext);
  if (context === undefined) {
    throw new Error('useChat must be used within a ChatProvider');
  }
  return context;
}; 