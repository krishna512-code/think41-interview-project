import React from 'react';
import './Message.css';

export interface MessageProps {
  content: string;
  role: 'user' | 'assistant';
  timestamp?: string;
}

const Message: React.FC<MessageProps> = ({ content, role, timestamp }) => {
  const isUser = role === 'user';
  
  return (
    <div className={`message ${isUser ? 'message-user' : 'message-assistant'}`}>
      <div className="message-avatar">
        {isUser ? '👤' : '🤖'}
      </div>
      <div className="message-content">
        <div className="message-text">{content}</div>
        {timestamp && (
          <div className="message-timestamp">{timestamp}</div>
        )}
      </div>
    </div>
  );
};

export default Message; 