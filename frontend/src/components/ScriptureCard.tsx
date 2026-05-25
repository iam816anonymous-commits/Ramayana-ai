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
      className="max-w-3xl w-full bg-[#0d0d0d] border border-sacred-gold/30 p-16 rounded-sm shadow-[0_0_100px_rgba(212,175,55,0.08)] space-y-16 text-sacred-warm relative overflow-hidden"
    >
      {/* Subtle Grain & Texture Overlay */}
      <div className="absolute inset-0 pointer-events-none opacity-[0.05] bg-[url('https://www.transparenttextures.com/patterns/black-paper.png')]" />

      {/* Ornate Corner Accents */}
      <div className="absolute top-0 left-0 w-12 h-12 border-t-2 border-l-2 border-sacred-gold/30 rounded-tl-sm" />
      <div className="absolute top-0 right-0 w-12 h-12 border-t-2 border-r-2 border-sacred-gold/30 rounded-tr-sm" />
      <div className="absolute bottom-0 left-0 w-12 h-12 border-b-2 border-l-2 border-sacred-gold/30 rounded-bl-sm" />
      <div className="absolute bottom-0 right-0 w-12 h-12 border-b-2 border-r-2 border-sacred-gold/30 rounded-br-sm" />

      {/* Brain Synthesis Badge */}
      <motion.div
        variants={item}
        className="absolute bottom-10 right-16 flex items-center gap-4 text-[8px] uppercase tracking-[0.6em] text-sacred-gold/25 italic"
      >
        <span className="w-6 h-[1px] bg-sacred-gold/20" />
        {data.brain_synthesis}
      </motion.div>

      <motion.div variants={item} className="space-y-6 relative">
        <div className="absolute -left-8 top-0 text-4xl text-sacred-gold/20 font-serif">“</div>
        <h3 className="text-sacred-gold font-bold uppercase tracking-[0.6em] text-[10px] opacity-40 mb-2">The Eternal Insight</h3>
        <p className="text-4xl font-serif italic leading-[1.3] text-sacred-warm/95 selection:bg-sacred-gold/20 pr-8">
          {data.reflection}
        </p>
      </motion.div>

      <motion.div variants={item} className="space-y-6 border-l border-sacred-gold/10 pl-10">
        <h3 className="text-sacred-gold font-bold uppercase tracking-[0.6em] text-[10px] opacity-40">Illumination</h3>
        <p className="leading-relaxed text-2xl font-light text-sacred-warm/80 max-w-[95%]">
          {data.meaning}
        </p>
      </motion.div>

      <motion.div variants={item} className="grid grid-cols-1 md:grid-cols-2 gap-16 pt-12 border-t border-sacred-gold/10">
        <div className="space-y-4">
          <h3 className="text-sacred-gold font-bold uppercase tracking-[0.6em] text-[10px] opacity-40">Sacred Context</h3>
          <p className="text-base italic text-sacred-warm/40 leading-relaxed font-light">{data.context}</p>
        </div>
        <div className="space-y-4">
          <h3 className="text-sacred-gold font-bold uppercase tracking-[0.6em] text-[10px] opacity-40">Guiding Sutra</h3>
          <p className="text-lg font-medium text-sacred-gold/70 italic leading-snug bg-sacred-gold/5 p-6 border-r border-sacred-gold/20">
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
