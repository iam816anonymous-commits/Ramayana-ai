'use client';

import { motion } from 'framer-motion';

interface SanctumResponse {
  reflection: string;
  meaning: string;
  context: string;
  takeaway: string;
}

export default function ScriptureCard({ data }: { data: SanctumResponse }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8 }}
      className="max-w-2xl w-full bg-[#1a1a1a] border border-sacred-gold/30 p-8 rounded-lg shadow-2xl space-y-8 text-sacred-warm"
    >
      <div className="space-y-2">
        <h3 className="text-sacred-gold font-bold uppercase tracking-widest text-sm">Reflection</h3>
        <p className="text-xl italic leading-relaxed text-sacred-warm/90">{data.reflection}</p>
      </div>

      <div className="space-y-2">
        <h3 className="text-sacred-gold font-bold uppercase tracking-widest text-sm">Meaning</h3>
        <p className="leading-relaxed">{data.meaning}</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="space-y-2">
          <h3 className="text-sacred-gold font-bold uppercase tracking-widest text-sm">Context</h3>
          <p className="text-sm text-sacred-warm/70">{data.context}</p>
        </div>
        <div className="space-y-2">
          <h3 className="text-sacred-gold font-bold uppercase tracking-widest text-sm">Takeaway</h3>
          <p className="text-sm font-bold border-l-2 border-sacred-gold pl-3">{data.takeaway}</p>
        </div>
      </div>
    </motion.div>
  );
}
