import React from 'react';
import MessageList from './MessageList';
import UserInput from './UserInput';
import { MessageProps } from './Message';
import './ChatWindow.css';

export interface ChatWindowProps {
  messages: MessageProps[];
  onSendMessage: (message: string) => void;
  isLoading?: boolean;
  title?: string;
  onNewConversation?: () => void;
}

const ChatWindow: React.FC<ChatWindowProps> = ({
  messages,
  onSendMessage,
  isLoading = false,
  title = "AI Assistant",
  onNewConversation
}) => {
  return (
    <div className="chat-window">
      <div className="chat-header">
        <div className="chat-header-content">
          <div className="chat-title">
            <span className="chat-icon">🤖</span>
            <h2>{title}</h2>
          </div>
          {onNewConversation && (
            <button 
              className="new-chat-button"
              onClick={onNewConversation}
              title="Start new conversation"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <line x1="12" y1="5" x2="12" y2="19"></line>
                <line x1="5" y1="12" x2="19" y2="12"></line>
              </svg>
            </button>
          )}
        </div>
      </div>
      
      <MessageList 
        messages={messages} 
        isLoading={isLoading} 
      />
      
      <UserInput 
        onSendMessage={onSendMessage}
        disabled={isLoading}
        placeholder="Ask me anything about our products..."
      />
    </div>
  );
};

export default ChatWindow; 