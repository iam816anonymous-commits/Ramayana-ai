'use client';

import { useState } from 'react';
import ChatBox from '@/components/ChatBox';
import Diya from '@/components/Diya';
import Pillar from '@/components/Pillar';

const CHARACTERS = ['Rama', 'Sita', 'Hanuman', 'Lakshmana', 'Ravana'];

export default function ChatPage() {
  const [selectedCharacter, setSelectedCharacter] = useState(CHARACTERS[0]);

  return (
    <div className="min-h-screen bg-sacred-dark p-8 relative overflow-hidden flex flex-col items-center pt-24">
      {/* Background elements to match the Sanctum theme */}
      <div className="fixed top-0 left-0 w-full h-full pointer-events-none opacity-[0.04] bg-[url('https://www.transparenttextures.com/patterns/black-paper.png')] z-0" />
      <Pillar side="left" />
      <Pillar side="right" />

      <div className="max-w-5xl w-full mx-auto relative z-10 text-center">
        <div className="flex justify-center mb-8">
           <Diya />
        </div>
        <h1 className="text-sacred-gold text-6xl font-serif mb-4 tracking-tight">Divine Dialogue</h1>
        <p className="text-sacred-warm/40 italic text-sm tracking-[0.4em] uppercase mb-16">Converse with the Eternal Personas</p>

        <div className="flex flex-wrap justify-center gap-6 mb-16">
          {CHARACTERS.map((char) => (
            <button
              key={char}
              onClick={() => setSelectedCharacter(char)}
              className={`px-8 py-4 rounded-full font-serif text-lg tracking-widest transition-all duration-700 border ${
                selectedCharacter === char
                  ? 'border-sacred-gold bg-sacred-gold/5 text-sacred-gold shadow-[0_0_20px_rgba(212,175,55,0.1)]'
                  : 'border-sacred-gold/10 text-sacred-warm/40 hover:border-sacred-gold/40 hover:text-sacred-gold/60'
              }`}
            >
              {char}
              <div className="text-[8px] tracking-[0.2em] font-sans opacity-60 mt-1 uppercase">
                {char === 'Rama' ? 'Dharma' : char === 'Sita' ? 'Purity' : char === 'Hanuman' ? 'Devotion' : char === 'Lakshmana' ? 'Loyalty' : 'Ego'}
              </div>
            </button>
          ))}
        </div>

        <div className="flex justify-center w-full">
          <ChatBox character={selectedCharacter} />
        </div>
      </div>
    </div>
  );
}
