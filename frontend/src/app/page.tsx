'use client';

import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import ScriptureCard from '@/components/ScriptureCard';

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
      // Simulate steps of the "Brain"
      setTimeout(() => setStatus('Synthesizing fragments of wisdom...'), 1500);

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
      }, 3000); // Artificial delay for "reflection"

    } catch (error) {
      console.error('Sanctum error:', error);
      setLoading(false);
      setStatus('');
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center pt-32 pb-32 p-6 bg-sacred-dark selection:bg-sacred-gold/30 overflow-y-auto">
      <div className="fixed top-0 left-0 w-full h-full pointer-events-none opacity-[0.03] bg-[url('https://www.transparenttextures.com/patterns/paper-fibers.png')]" />

      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 2 }}
        className="text-center mb-32 space-y-4 relative z-10"
      >
        <h1 className="text-sacred-gold text-7xl font-serif tracking-[-0.05em] lowlight">Sanctum</h1>
        <p className="text-sacred-warm/40 italic text-xl tracking-widest font-light">Sit. Ask. Reflect.</p>
      </motion.div>

      <motion.div
        animate={{ opacity: response ? 0.2 : 1, scale: response ? 0.98 : 1 }}
        transition={{ duration: 1 }}
        className="w-full max-w-2xl mb-32 relative z-10"
      >
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleReflect()}
          placeholder="What seek you in the eternal story?"
          className="w-full bg-transparent border-b border-sacred-gold/20 py-8 px-4 text-4xl font-serif focus:outline-none focus:border-sacred-gold text-sacred-warm placeholder:text-sacred-warm/10 transition-all duration-1000"
        />
        <div className="absolute right-4 bottom-8 flex items-center gap-6">
           <AnimatePresence>
             {loading && (
               <motion.span
                 initial={{ opacity: 0, x: 10 }}
                 animate={{ opacity: 1, x: 0 }}
                 exit={{ opacity: 0 }}
                 className="text-sacred-gold/40 text-[10px] uppercase tracking-[0.3em] animate-pulse"
               >
                 {status}
               </motion.span>
             )}
           </AnimatePresence>
           <button
            onClick={handleReflect}
            disabled={loading}
            className="text-sacred-gold/60 hover:text-sacred-gold transition-all disabled:opacity-0 uppercase text-xs tracking-[0.4em] font-bold"
          >
            {response ? 'Ask Again' : 'Reflect'}
          </button>
        </div>
      </motion.div>

      <AnimatePresence mode="wait">
        {response && (
          <ScriptureCard key="scripture" data={response} />
        )}
      </AnimatePresence>

      {loading && !response && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="flex flex-col items-center gap-8 py-12"
        >
          <div className="relative w-32 h-32">
            <motion.div
              animate={{ rotate: 360 }}
              transition={{ repeat: Infinity, duration: 20, ease: "linear" }}
              className="absolute inset-0 border border-sacred-gold/10 rounded-full"
            />
            <motion.div
              animate={{ rotate: -360 }}
              transition={{ repeat: Infinity, duration: 15, ease: "linear" }}
              className="absolute inset-4 border border-sacred-gold/5 rounded-full"
            />
            <div className="absolute inset-0 flex items-center justify-center">
               <div className="w-1.5 h-1.5 bg-sacred-gold/40 rounded-full blur-[2px] animate-pulse" />
            </div>
          </div>
        </motion.div>
      )}

      <div className="fixed bottom-8 text-[9px] text-sacred-warm/20 uppercase tracking-[0.5em] font-medium">
        Ramayana Mythology Intelligence
      </div>
    </div>
  );
}
