'use client';

import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import ScriptureCard from '@/components/ScriptureCard';

interface SanctumResponse {
  reflection: string;
  meaning: string;
  context: string;
  takeaway: string;
}

export default function SanctumPage() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState<SanctumResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleReflect = async () => {
    if (!query.trim()) return;
    setLoading(true);
    setResponse(null);

    try {
      const res = await fetch('http://localhost:8000/api/sanctum/reflect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query }),
      });
      const data = await res.json();
      setResponse(data);
    } catch (error) {
      console.error('Sanctum error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-6 bg-sacred-dark">
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 2 }}
        className="text-center mb-16 space-y-4"
      >
        <h1 className="text-sacred-gold text-6xl font-serif tracking-tighter">Sanctum</h1>
        <p className="text-sacred-warm/60 italic text-xl">Sit. Ask. Reflect.</p>
      </motion.div>

      <div className="w-full max-w-xl mb-12 relative">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleReflect()}
          placeholder="What seek you in the eternal story?"
          className="w-full bg-transparent border-b border-sacred-gold/50 py-4 px-2 text-2xl focus:outline-none focus:border-sacred-gold text-sacred-warm placeholder:text-sacred-warm/20 transition-colors"
        />
        <button
          onClick={handleReflect}
          disabled={loading}
          className="absolute right-0 bottom-4 text-sacred-gold hover:text-sacred-warm transition-colors disabled:opacity-30"
        >
          {loading ? 'Thinking...' : 'Reflect'}
        </button>
      </div>

      <AnimatePresence>
        {response && (
          <ScriptureCard data={response} />
        )}
      </AnimatePresence>

      {loading && (
        <motion.div
          animate={{ scale: [1, 1.1, 1], opacity: [0.3, 0.6, 0.3] }}
          transition={{ repeat: Infinity, duration: 2 }}
          className="w-24 h-24 rounded-full border-2 border-sacred-gold/20 flex items-center justify-center"
        >
          <div className="w-2 h-2 bg-sacred-gold rounded-full" />
        </motion.div>
      )}
    </div>
  );
}
