import axios from 'axios';
import { ChatRequest, ChatResponse, Conversation } from '../types/chat';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const chatAPI = {
  sendMessage: async (request: ChatRequest): Promise<ChatResponse> => {
    const response = await api.post<ChatResponse>('/api/chat', request);
    return response.data;
  },

  getConversationHistory: async (conversationId: string): Promise<Conversation> => {
    const response = await api.get<Conversation>(`/api/conversations/${conversationId}`);
    return response.data;
  },

  getUserConversations: async (userId: string): Promise<Conversation[]> => {
    const response = await api.get<Conversation[]>(`/api/users/${userId}/conversations`);
    return response.data;
  },
};

export default api; 