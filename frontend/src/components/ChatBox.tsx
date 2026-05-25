'use client';

import { useState } from 'react';

interface Message {
  role: 'user' | 'bot';
  text: string;
}

export default function ChatBox({ character }: { character: string }) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg: Message = { role: 'user', text: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      const res = await fetch('http://localhost:8000/api/characters/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ character, message: input }),
      });
      const data = await res.json();
      setMessages((prev) => [...prev, { role: 'bot', text: data.response }]);
    } catch (error) {
      console.error('Chat error:', error);
      setMessages((prev) => [...prev, { role: 'bot', text: 'Sorry, I am unable to connect.' }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-[600px] w-full max-w-4xl border border-sacred-gold/10 rounded-xl overflow-hidden bg-black/40 backdrop-blur-sm shadow-2xl relative group">
      {/* Decorative Border Glow */}
      <div className="absolute inset-0 border border-sacred-gold/5 rounded-xl pointer-events-none group-hover:border-sacred-gold/20 transition-all duration-1000" />

      <div className="border-b border-sacred-gold/10 p-6 flex items-center justify-between bg-sacred-gold/5">
        <div className="text-left">
          <h2 className="text-sacred-gold text-2xl font-serif tracking-wide">{character}</h2>
          <p className="text-[10px] text-sacred-warm/30 uppercase tracking-[0.2em] font-medium">Eternal Persona</p>
        </div>
        <div className="w-2 h-2 rounded-full bg-sacred-gold/40 animate-pulse shadow-[0_0_10px_rgba(212,175,55,0.4)]" />
      </div>

      <div className="flex-1 overflow-y-auto p-8 space-y-8 scrollbar-thin scrollbar-thumb-sacred-gold/10">
        {messages.length === 0 && (
          <div className="h-full flex flex-col items-center justify-center space-y-4 opacity-40">
            <div className="w-12 h-[1px] bg-sacred-gold/20" />
            <p className="text-sacred-warm italic font-serif text-lg">Inquire and the resonance shall follow</p>
            <div className="w-12 h-[1px] bg-sacred-gold/20" />
          </div>
        )}
        {messages.map((m, i) => (
          <div key={i} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'} animate-in fade-in slide-in-from-bottom-4 duration-1000`}>
            <div className={`max-w-[85%] p-6 rounded-2xl font-serif leading-relaxed ${
              m.role === 'user'
                ? 'bg-sacred-gold/5 text-sacred-gold/80 border border-sacred-gold/10 italic text-right'
                : 'text-sacred-warm/90 relative'
            }`}>
              {m.role === 'bot' && (
                <div className="absolute -left-4 top-0 w-[1px] h-full bg-gradient-to-b from-sacred-gold/40 to-transparent" />
              )}
              <p className="whitespace-pre-wrap text-lg">{m.text}</p>
            </div>
          </div>
        ))}
        {loading && (
          <div className="flex justify-start animate-pulse">
            <div className="text-sacred-gold/40 italic font-serif tracking-widest text-sm">Translating divine echoes...</div>
          </div>
        )}
      </div>

      <div className="p-6 bg-black/20 border-t border-sacred-gold/5">
        <div className="relative flex items-center gap-4">
          <input
            type="text"
            className="flex-1 bg-sacred-gold/5 border border-sacred-gold/10 rounded-full px-8 py-4 focus:outline-none focus:border-sacred-gold/40 text-sacred-warm placeholder:text-sacred-warm/10 font-serif text-lg transition-all"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
            placeholder={`Address ${character}...`}
          />
          <button
            onClick={sendMessage}
            disabled={loading}
            className="bg-sacred-gold/10 text-sacred-gold px-8 py-4 rounded-full font-serif tracking-widest hover:bg-sacred-gold/20 transition-all disabled:opacity-20 border border-sacred-gold/20"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
