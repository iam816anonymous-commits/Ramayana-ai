'use client';

import { motion } from 'framer-motion';

interface SanctumResponse {
  reflection: string;
  meaning: string;
  context: string;
  takeaway: string;
  brain_synthesis: string;
}

export default function ScriptureCard({ data }: { data: SanctumResponse }) {
  const container = {
    hidden: { opacity: 0, scale: 0.98 },
    show: {
      opacity: 1,
      scale: 1,
      transition: {
        staggerChildren: 0.3,
        duration: 1,
        ease: "easeOut"
      }
    }
  };

  const item = {
    hidden: { opacity: 0, y: 10 },
    show: { opacity: 1, y: 0, transition: { duration: 0.8 } }
  };

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="max-w-2xl w-full bg-[#0a0a0a] border border-sacred-gold/20 p-10 rounded-sm shadow-[0_0_60px_rgba(212,175,55,0.05)] space-y-12 text-sacred-warm relative overflow-hidden"
    >
      {/* Subtle Grain Overlay */}
      <div className="absolute inset-0 pointer-events-none opacity-[0.03] bg-[url('https://www.transparenttextures.com/patterns/p6.png')]" />

      {/* Brain Synthesis Badge - Moved to bottom for better flow */}
      <motion.div
        variants={item}
        className="absolute bottom-8 left-10 flex items-center gap-3 text-[8px] uppercase tracking-[0.5em] text-sacred-gold/20"
      >
        <span className="w-1 h-1 bg-sacred-gold/20 rounded-full animate-pulse" />
        {data.brain_synthesis}
      </motion.div>

      <motion.div variants={item} className="space-y-4">
        <h3 className="text-sacred-gold font-bold uppercase tracking-[0.4em] text-[9px] opacity-40">Reflection</h3>
        <p className="text-3xl font-serif italic leading-[1.4] text-sacred-warm/95 selection:bg-sacred-gold/20">
          “{data.reflection}”
        </p>
      </motion.div>

      <motion.div variants={item} className="space-y-4">
        <h3 className="text-sacred-gold font-bold uppercase tracking-[0.4em] text-[9px] opacity-40">The Meaning</h3>
        <p className="leading-relaxed text-xl font-light text-sacred-warm/80 max-w-[90%]">
          {data.meaning}
        </p>
      </motion.div>

      <motion.div variants={item} className="grid grid-cols-1 md:grid-cols-2 gap-12 pt-6 border-t border-sacred-gold/5">
        <div className="space-y-3">
          <h3 className="text-sacred-gold font-bold uppercase tracking-[0.4em] text-[9px] opacity-40">Contextual Lore</h3>
          <p className="text-sm italic text-sacred-warm/40 leading-relaxed">{data.context}</p>
        </div>
        <div className="space-y-3">
          <h3 className="text-sacred-gold font-bold uppercase tracking-[0.4em] text-[9px] opacity-40">Eternal Sutra</h3>
          <p className="text-base font-medium border-l-2 border-sacred-gold/20 pl-6 py-2 text-sacred-gold/80 italic">
            {data.takeaway}
          </p>
        </div>
      </motion.div>

      {/* Decorative Corner */}
      <div className="absolute bottom-0 right-0 w-16 h-16 pointer-events-none opacity-10">
        <div className="absolute bottom-4 right-4 w-12 h-[1px] bg-sacred-gold" />
        <div className="absolute bottom-4 right-4 w-[1px] h-12 bg-sacred-gold" />
      </div>
    </motion.div>
  );
}
