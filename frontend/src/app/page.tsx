'use client';

import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import ScriptureCard from '@/components/ScriptureCard';
import Diya from '@/components/Diya';
import Pillar from '@/components/Pillar';

interface SanctumResponse {
  reflection: string;
  meaning: string;
  context: string;
  takeaway: string;
  brain_synthesis: string;
}

export default function SanctumPage() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState<SanctumResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState('');

  const handleReflect = async () => {
    if (!query.trim()) return;
    setLoading(true);
    setResponse(null);
    setStatus('Consulting the eternal records...');

    try {
      setTimeout(() => setStatus('Synthesizing fragments of wisdom...'), 1200);
      setTimeout(() => setStatus('Seeker Agent challenging the insight...'), 2400);
      setTimeout(() => setStatus('Refining dialectical truth...'), 3600);

      const res = await fetch('http://localhost:8000/api/sanctum/reflect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query }),
      });
      const data = await res.json();

      setTimeout(() => {
        setResponse(data);
        setLoading(false);
        setStatus('');
      }, 3000);

    } catch (error) {
      console.error('Sanctum error:', error);
      setLoading(false);
      setStatus('');
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center pt-32 pb-32 p-6 bg-sacred-dark selection:bg-sacred-gold/30 overflow-y-auto relative">
      {/* Background Textures & Architecture */}
      <div className="fixed top-0 left-0 w-full h-full pointer-events-none opacity-[0.04] bg-[url('https://www.transparenttextures.com/patterns/black-paper.png')] z-0" />
      <div className="fixed top-0 left-0 w-full h-40 bg-gradient-to-b from-black to-transparent z-0 opacity-60" />

      <Pillar side="left" />
      <Pillar side="right" />

      {/* Main Title Section */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 2 }}
        className="text-center mb-32 space-y-6 relative z-10"
      >
        <div className="flex justify-center mb-8">
           <Diya />
        </div>
        <h1 className="text-sacred-gold text-8xl font-serif tracking-[-0.05em] lowlight">Sanctum</h1>
        <div className="h-[1px] w-48 bg-gradient-to-r from-transparent via-sacred-gold/40 to-transparent mx-auto" />
        <p className="text-sacred-warm/40 italic text-xl tracking-[0.3em] font-light uppercase">The Eternal Intelligence</p>
      </motion.div>

      {/* Input Field (The Threshold) */}
      <motion.div
        animate={{ opacity: response ? 0.15 : 1, scale: response ? 0.98 : 1 }}
        transition={{ duration: 1 }}
        className="w-full max-w-2xl mb-32 relative z-10"
      >
        <div className="relative group">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleReflect()}
            placeholder="Inscribe your inquiry..."
            className="w-full bg-transparent border-b border-sacred-gold/20 py-10 px-4 text-4xl font-serif focus:outline-none focus:border-sacred-gold/60 text-sacred-warm placeholder:text-sacred-warm/5 transition-all duration-1000 text-center"
          />
          <div className="absolute inset-x-0 bottom-0 h-[1px] bg-sacred-gold/10 group-hover:bg-sacred-gold/30 transition-all duration-1000" />
        </div>

        <div className="absolute inset-x-0 -bottom-16 flex flex-col items-center gap-6">
           <AnimatePresence>
             {loading && (
               <motion.div
                 initial={{ opacity: 0, y: 10 }}
                 animate={{ opacity: 1, y: 0 }}
                 exit={{ opacity: 0 }}
                 className="flex flex-col items-center gap-4"
               >
                 <span className="text-sacred-gold/40 text-[10px] uppercase tracking-[0.5em] animate-pulse">
                   {status}
                 </span>
                 <div className="w-1 h-12 bg-gradient-to-b from-sacred-gold/40 to-transparent" />
               </motion.div>
             )}
           </AnimatePresence>
           {!loading && (
             <button
              onClick={handleReflect}
              className="text-sacred-gold/40 hover:text-sacred-gold transition-all uppercase text-[10px] tracking-[0.6em] font-bold border border-sacred-gold/10 px-8 py-3 rounded-full hover:bg-sacred-gold/5"
            >
              {response ? 'Seek Further' : 'Seek Wisdom'}
            </button>
           )}
        </div>
      </motion.div>

      {/* Results (The Revelation) */}
      <AnimatePresence mode="wait">
        {response && (
          <ScriptureCard key="scripture" data={response} />
        )}
      </AnimatePresence>

      {/* Decorative Floor */}
      <div className="fixed bottom-0 left-0 w-full h-24 bg-gradient-to-t from-black to-transparent pointer-events-none opacity-80" />

      <div className="fixed bottom-8 text-[9px] text-sacred-warm/20 uppercase tracking-[0.8em] font-medium z-20">
        Ramayana Mythology Intelligence • Phase I
      </div>
    </div>
  );
}
