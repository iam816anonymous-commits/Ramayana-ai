'use client';

import { useEffect, useState } from 'react';
import Timeline from '@/components/Timeline';

export default function TimelinePage() {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/api/timeline/')
      .then((res) => res.json())
      .then((data) => {
        setEvents(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Timeline fetch error:', err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="min-h-screen bg-[#0a0a0a] p-8 font-serif">
      <div className="max-w-3xl mx-auto">
        <h1 className="text-4xl font-bold text-[#d4af37] mb-4 drop-shadow-[0_2px_4px_rgba(0,0,0,0.8)]">
          Ramayana Timeline
        </h1>
        <p className="text-[#a0a0a0] mb-12 italic text-lg border-l-2 border-[#d4af37]/30 pl-4">
          Journey through the sacred events of the Ramayana.
        </p>

        {loading ? (
          <div className="flex justify-center py-20">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-[#d4af37]"></div>
          </div>
        ) : (
          <Timeline events={events} />
        )}
      </div>
    </div>
  );
}
