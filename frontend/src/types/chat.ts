export interface Message {
  content: string;
  role: 'user' | 'assistant';
  timestamp?: string;
}

export interface Conversation {
  conversation_id: string;
  title?: string;
  messages: Message[];
  created_at: string;
  updated_at?: string;
}

export interface ChatRequest {
  message: string;
  conversation_id?: string;
  user_id: string;
}

export interface ChatResponse {
  response: string;
  conversation_id: string;
  message_id: string;
}

export interface ChatState {
  messages: Message[];
  isLoading: boolean;
  currentConversationId?: string;
  conversations: Conversation[];
  userInput: string;
}

export interface ChatContextType {
  state: ChatState;
  sendMessage: (message: string) => Promise<void>;
  startNewConversation: () => void;
  loadConversation: (conversationId: string) => void;
  setUserInput: (input: string) => void;
} 