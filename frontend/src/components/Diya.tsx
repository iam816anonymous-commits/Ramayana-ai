'use client';

import { motion } from 'framer-motion';

export default function Diya() {
  return (
    <div className="relative flex flex-col items-center">
      {/* Flame */}
      <motion.div
        animate={{
          scale: [1, 1.1, 0.9, 1.05, 1],
          opacity: [0.7, 0.9, 0.6, 0.8, 0.7],
          rotate: [-1, 1, -0.5, 0.5, 0],
        }}
        transition={{
          duration: 3,
          repeat: Infinity,
          ease: "easeInOut"
        }}
        className="w-4 h-8 bg-gradient-to-t from-orange-600 via-yellow-400 to-white rounded-full blur-[2px] diya-glow"
        style={{ borderRadius: '50% 50% 50% 50% / 80% 80% 20% 20%' }}
      />
      {/* Wick */}
      <div className="w-[1px] h-2 bg-black/40 mt-[-2px] relative z-10" />
      {/* Bowl */}
      <div className="w-10 h-4 bg-gradient-to-b from-[#4a3721] to-[#2a1a0a] rounded-b-full shadow-lg relative overflow-hidden">
         <div className="absolute inset-0 bg-sacred-gold/10 mix-blend-overlay" />
      </div>
    </div>
  );
}
