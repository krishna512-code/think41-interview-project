import React from 'react';
import './App.css';
import { ChatProvider } from './contexts/ChatContext';
import ChatWindow from './components/ChatWindow';
import { useChat } from './contexts/ChatContext';

const ChatApp: React.FC = () => {
  const { state, sendMessage, startNewConversation } = useChat();

  return (
    <ChatWindow
      messages={state.messages}
      onSendMessage={sendMessage}
      isLoading={state.isLoading}
      title="E-commerce AI Assistant"
      onNewConversation={startNewConversation}
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
