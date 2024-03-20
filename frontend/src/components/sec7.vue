<template>
  <div class="chat-app">
    <div class="chat-container">
      <div class="chat-history">
        <div v-for="(chat, index) in chatHistory" :key="index" class="chat-session">
          <div class="chat-messages">
            <div v-for="(message, messageIndex) in chat" :key="messageIndex" :class="['message-bubble', message.sender]">
              <template v-if="message.isCodeBlock">
                <pre class="code-block"><code>{{ message.text }}</code></pre>
              </template>
              <p v-else>{{ message.text }}</p>
            </div>
          </div>
        </div>
      </div>
      <div class="chat-input">
        <div class="suggestions">
          <button v-for="(suggestion, index) in suggestions" :key="index" @click="sendSuggestion(suggestion)">
            {{ suggestion }}
          </button>
        </div>
        <textarea v-model="message" @keyup.enter="sendMessage" placeholder="Type your message..."></textarea>
        <button @click="sendMessage">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
            stroke-linejoin="round" class="feather feather-send">
            <line x1="22" y1="2" x2="11" y2="13"></line>
            <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';

interface Message {
  sender: string;
  text: string;
  isCodeBlock?: boolean;
}

export default {
  setup() {
    const message = ref('');
    const chatHistory = ref<Message[][]>([
      [
        { sender: 'ai', text: "Hello, I'm ChatAI! How can I assist you today?" },
      ],
    ]);
    const isThinking = ref(false);
    const suggestions = ref(['Write me a Python calculator', 'Implement basic HTML page']);

    const sendMessage = async () => {
      if (message.value.trim()) {
        isThinking.value = true;
        chatHistory.value[chatHistory.value.length - 1].push({ sender: 'user', text: message.value });

        const response = await fetch('http://127.0.0.1:5000/generate', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ prompt: message.value }),
        });

        if (!response.ok) {
          console.error('Server error:', response.status, response.statusText);
          isThinking.value = false;
          return;
        }

        const data = await response.json();
        if (data && data.choices && data.choices.length > 0) {
          const aiResponse = data.choices[0].message.content;
          const codeBlockContent = detectCodeBlock(aiResponse);
          const isCodeBlock = !!codeBlockContent;

          chatHistory.value[chatHistory.value.length - 1].push({
            sender: 'ai',
            text: isCodeBlock ? codeBlockContent : aiResponse.trim(),
            isCodeBlock
          });
          isThinking.value = false;
          message.value = '';
        }
      }
    };

    const sendSuggestion = (suggestion: string) => {
      message.value = suggestion;
      sendMessage();
    };

    const detectCodeBlock = (text: string) => {
      const codeBlockRegex = /```([\s\S]*?)```/;
      const match = codeBlockRegex.exec(text);
      if (match && match[1]) {
        return match[1].trim();
      } else {
        return false;
      }
    };


    return { message, chatHistory, sendMessage, suggestions, sendSuggestion };
  },
};
</script>



<style scoped>
.chat-app {
  font-family: 'Roboto', sans-serif;
  width: 100%;
  margin: 0 auto;
  height: 100vh;
  background-color: #343541;
  color: #fff;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100vh;
}

.chat-container {
  width: 100%;
  max-width: 90%;
  background-color: #40414f;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
  overflow: hidden;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.chat-header {
  background-color: #343541;
  color: #fff;
  padding: 16px;
  text-align: center;
}

.chat-messages {
  flex-grow: 1;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  overflow-y: auto;
}

.message-bubble {
  max-width: 70%;
  padding: 8px 12px;
  border-radius: 16px;
  font-size: 14px;
  line-height: 1.4;
  word-wrap: break-word;
}

.user {
  background-color: #6e6e7e;
  color: #fff;
  align-self: flex-end;
  margin-right: 8px;
}

.ai {
  background-color: #8ab4f8;
  color: #202123;
  align-self: flex-start;
  margin-left: 8px;
}

.chat-input {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 16px;
  background-color: #40414f;
  border-top: 1px solid #2c2c38;
}

textarea {
  flex-grow: 1;
  padding: 8px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  resize: none;
  background-color: #343541;
  color: #fff;
}

.chat-history {
  flex-grow: 1;
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  flex-grow: 1;
}

.chat-session {
  border-bottom: 1px solid #2c2c38;
  padding-bottom: 16px;
}

.chat-session:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

button {
  background-color: #8ab4f8;
  color: #202123;
  border: none;
  border-radius: 4px;
  padding: 8px 16px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

button:hover {
  background-color: #7aa4f0;
}

.feather {
  width: 16px;
  height: 16px;
  vertical-align: middle;
}

.thinking-animation {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 4px;
}

.dot {
  width: 6px;
  height: 6px;
  background-color: #8ab4f8;
  border-radius: 50%;
  animation: pulse 1s infinite ease-in-out;
}

.dot:nth-child(2) {
  animation-delay: 0.2s;
}

.dot:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes pulse {

  0%,
  100% {
    transform: scale(1);
  }

  50% {
    transform: scale(1.5);
  }
}

.suggestions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding: 8px;
  background-color: #40414f;
  border-top: 1px solid #2c2c38;
}

.suggestions button {
  background-color: #8ab4f8;
  color: #202123;
  border: none;
  border-radius: 4px;
  padding: 8px 16px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.suggestions button:hover {
  background-color: #7aa4f0;
}

.code-block {
  background-color: #2c2c38;
  color: #fff;
  padding: 10px;
  border-radius: 5px;
  overflow-x: auto;
  white-space: pre-wrap;
  font-family: 'Courier New', Courier, monospace;
}</style>
