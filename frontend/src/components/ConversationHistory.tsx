import React from 'react';
import { Conversation } from '../types/chat';
import './ConversationHistory.css';

export interface ConversationHistoryProps {
  conversations: Conversation[];
  currentConversationId?: string;
  onSelectConversation: (conversationId: string) => void;
  onNewConversation: () => void;
  isOpen: boolean;
  onToggle: () => void;
}

const ConversationHistory: React.FC<ConversationHistoryProps> = ({
  conversations,
  currentConversationId,
  onSelectConversation,
  onNewConversation,
  isOpen,
  onToggle
}) => {
  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    const now = new Date();
    const diffInHours = (now.getTime() - date.getTime()) / (1000 * 60 * 60);
    
    if (diffInHours < 24) {
      return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    } else if (diffInHours < 168) { // 7 days
      return date.toLocaleDateString([], { weekday: 'short' });
    } else {
      return date.toLocaleDateString([], { month: 'short', day: 'numeric' });
    }
  };

  const getConversationTitle = (conversation: Conversation) => {
    if (conversation.title) {
      return conversation.title;
    }
    
    const firstMessage = conversation.messages[0];
    if (firstMessage) {
      const content = firstMessage.content;
      return content.length > 30 ? content.substring(0, 30) + '...' : content;
    }
    
    return 'New Conversation';
  };

  return (
    <>
      {/* Mobile overlay */}
      {isOpen && (
        <div className="conversation-overlay" onClick={onToggle} />
      )}
      
      {/* Side panel */}
      <div className={`conversation-history ${isOpen ? 'open' : ''}`}>
        <div className="conversation-header">
          <h3>Conversations</h3>
          <button className="close-button" onClick={onToggle}>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>
        
        <div className="conversation-actions">
          <button className="new-conversation-button" onClick={onNewConversation}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <line x1="12" y1="5" x2="12" y2="19"></line>
              <line x1="5" y1="12" x2="19" y2="12"></line>
            </svg>
            New Chat
          </button>
        </div>
        
        <div className="conversation-list">
          {conversations.length === 0 ? (
            <div className="empty-state">
              <p>No conversations yet</p>
              <p>Start a new chat to begin!</p>
            </div>
          ) : (
            conversations.map((conversation) => (
              <div
                key={conversation.conversation_id}
                className={`conversation-item ${
                  conversation.conversation_id === currentConversationId ? 'active' : ''
                }`}
                onClick={() => onSelectConversation(conversation.conversation_id)}
              >
                <div className="conversation-content">
                  <div className="conversation-title">
                    {getConversationTitle(conversation)}
                  </div>
                  <div className="conversation-meta">
                    <span className="conversation-date">
                      {formatDate(conversation.updated_at || conversation.created_at)}
                    </span>
                    <span className="conversation-count">
                      {conversation.messages.length} messages
                    </span>
                  </div>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
      
      {/* Mobile toggle button */}
      <button className="history-toggle-button" onClick={onToggle}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>
    </>
  );
};

export default ConversationHistory; 