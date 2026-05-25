'use client';

interface Event {
  id: number;
  title: string;
  description: string;
  kanda: string;
}

export default function Timeline({ events }: { events: Event[] }) {
  return (
    <div className="relative border-l-4 border-orange-500 ml-4 py-8 space-y-12">
      {events.map((event) => (
        <div key={event.id} className="relative ml-8">
          <div className="absolute -left-[42px] top-1 w-6 h-6 bg-orange-600 rounded-full border-4 border-white shadow"></div>
          <div className="bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition-shadow border border-orange-100">
            <span className="text-sm font-semibold text-orange-600 uppercase tracking-wider">
              {event.kanda}
            </span>
            <h3 className="text-2xl font-bold text-gray-900 mt-1">{event.title}</h3>
            <p className="text-gray-600 mt-3 leading-relaxed">{event.description}</p>
          </div>
        </div>
      ))}
    </div>
  );
}
