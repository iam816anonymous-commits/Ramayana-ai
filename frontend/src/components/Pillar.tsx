'use client';

import { motion } from 'framer-motion';

export default function Pillar({ side }: { side: 'left' | 'right' }) {
  return (
    <div className={`fixed top-0 bottom-0 w-24 pointer-events-none z-0 hidden lg:block ${side === 'left' ? 'left-8' : 'right-8'}`}>
      {/* Pillar Shaft */}
      <div className="absolute inset-0 bg-gradient-to-b from-transparent via-sacred-gold/5 to-transparent border-x border-sacred-gold/10 overflow-hidden">
         {/* Etchings */}
         <div className="h-full w-full opacity-10 flex flex-col items-center justify-around py-20">
           {[...Array(10)].map((_, i) => (
             <div key={i} className="w-12 h-12 border border-sacred-gold rounded-full flex items-center justify-center rotate-45">
               <div className="w-6 h-6 border border-sacred-gold" />
             </div>
           ))}
         </div>
      </div>

      {/* Pillar Cap */}
      <div className="absolute top-0 left-[-10px] right-[-10px] h-12 bg-sacred-dark border-b border-sacred-gold/20 flex items-end justify-center pb-2">
        <div className="w-full h-[1px] bg-sacred-gold/40 mb-1" />
      </div>

      {/* Pillar Base */}
      <div className="absolute bottom-0 left-[-10px] right-[-10px] h-20 bg-sacred-dark border-t border-sacred-gold/20 shadow-[0_-10px_30px_rgba(212,175,55,0.05)]">
         <div className="w-full h-full p-4 flex items-start justify-center">
            <div className="w-8 h-8 border border-sacred-gold/20 rounded-sm rotate-45" />
         </div>
      </div>
    </div>
  );
}
