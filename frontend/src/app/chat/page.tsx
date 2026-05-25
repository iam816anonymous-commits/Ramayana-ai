'use client';

import { useState } from 'react';
import ChatBox from '@/components/ChatBox';

const CHARACTERS = ['Rama', 'Sita', 'Hanuman'];

export default function ChatPage() {
  const [selectedCharacter, setSelectedCharacter] = useState(CHARACTERS[0]);

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-gray-900 mb-8">Ramayana AI Characters</h1>

        <div className="flex gap-4 mb-8">
          {CHARACTERS.map((char) => (
            <button
              key={char}
              onClick={() => setSelectedCharacter(char)}
              className={`px-6 py-2 rounded-full font-medium transition-colors ${
                selectedCharacter === char
                  ? 'bg-orange-600 text-white shadow-md'
                  : 'bg-white text-gray-600 hover:bg-orange-50'
              }`}
            >
              {char}
            </button>
          ))}
        </div>

        <div className="flex justify-center">
          <ChatBox character={selectedCharacter} />
        </div>
      </div>
    </div>
  );
}
