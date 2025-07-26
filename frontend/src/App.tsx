import React from 'react';
import './App.css';
import { ChatProvider, useChat } from './contexts/ChatContext';
import ChatWindow from './components/ChatWindow';

const ChatApp: React.FC = () => {
  const { state, sendMessage, startNewConversation, loadConversation } = useChat();

  return (
    <ChatWindow
      messages={state.messages}
      onSendMessage={sendMessage}
      isLoading={state.isLoading}
      title="E-commerce AI Assistant"
      onNewConversation={startNewConversation}
      conversations={state.conversations}
      currentConversationId={state.currentConversationId}
      onSelectConversation={loadConversation}
    />
  );
};

function App() {
  return (
    <div className="App">
      <ChatProvider>
        <ChatApp />
      </ChatProvider>
    </div>
  );
}

export default App;
