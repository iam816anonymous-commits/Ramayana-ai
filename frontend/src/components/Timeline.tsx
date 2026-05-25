'use client';

interface Event {
  id: number;
  title: string;
  description: string;
  kanda: string;
}

export default function Timeline({ events }: { events: Event[] }) {
  return (
    <div className="relative border-l-2 border-[#d4af37]/30 ml-4 py-8 space-y-12">
      {events.map((event) => (
        <div key={event.id} className="relative ml-8">
          <div className="absolute -left-[41px] top-1 w-4 h-4 bg-[#d4af37] rounded-full shadow-[0_0_10px_#d4af37]"></div>
          <div className="bg-[#1a1a1a]/80 backdrop-blur-sm p-6 rounded-lg shadow-2xl transition-all hover:bg-[#222]/90 border border-[#d4af37]/20 group">
            <span className="text-sm font-semibold text-[#d4af37]/70 uppercase tracking-[0.2em] font-serif">
              {event.kanda}
            </span>
            <h3 className="text-2xl font-bold text-[#d4af37] mt-1 group-hover:text-[#f1c40f] transition-colors">
              {event.title}
            </h3>
            <p className="text-[#a0a0a0] mt-3 leading-relaxed font-serif italic opacity-90">
              {event.description}
            </p>
          </div>
        </div>
      ))}
    </div>
  );
}
