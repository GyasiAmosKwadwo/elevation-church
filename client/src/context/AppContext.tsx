import React, { createContext, useContext, useReducer, ReactNode } from 'react';
import { imgs } from '@/assets/assets';
import { LogOut } from 'lucide-react';

export interface Sermon {
  id: string;
  title: string;
  description: string;
  videoUrl: string;
  podcastUrl?: string;
  preacher: string;
  date: string;
  series?: string;
  tags: string[];
}

export interface Series {
  id: string;
  title: string;
  description: string;
  sermons: string[];
  thumbnail: string;
}

export interface Event {
  id: string;
  title: string;
  description: string;
  date: string;
  time: string;
  location: string;
  image: string;
  registrationLink?: string;
  featured: boolean;
  status?: 'upcoming' | 'past' | 'ongoing';
}

export interface AppState {
  sermons: Sermon[];
  series: Series[];
  events: Event[];
  isLivestreaming: boolean;
  livestreamUrl?: string;
  currentUser?: {
    id: string;
    name: string;
    role: 'admin' | 'user';
  };
  churchSettings: {
    name: string;
    logo: string;
  };
}

type AppAction =
  | { type: 'ADD_SERMON'; payload: Sermon }
  | { type: 'UPDATE_SERMON'; payload: Sermon }
  | { type: 'DELETE_SERMON'; payload: string }
  | { type: 'ADD_SERIES'; payload: Series }
  | { type: 'UPDATE_SERIES'; payload: Series }
  | { type: 'DELETE_SERIES'; payload: string }
  | { type: 'ADD_EVENT'; payload: Event }
  | { type: 'UPDATE_EVENT'; payload: Event }
  | { type: 'DELETE_EVENT'; payload: string }
  | { type: 'SET_LIVESTREAM'; payload: { isLive: boolean; url?: string } }
  | { type: 'SET_USER'; payload: AppState['currentUser'] }
  | { type: 'UPDATE_CHURCH_SETTINGS'; payload: { name: string , logo: "string" } };


function calculateEventStatus(eventDate: string): 'upcoming' | 'ongoing' | 'past' {
    const now = new Date();
    const eventStart = new Date(eventDate);
    const eventEnd = new Date(eventDate);
    eventEnd.setHours(eventEnd.getHours() + 2); // Assuming events last 2 hours
  
    if (now < eventStart) {
      return 'upcoming';
    } else if (now >= eventStart && now <= eventEnd) {
      return 'ongoing';
    } else {
      return 'past';
    }
}

const initialState: AppState = {
  sermons: [
    {
      id: 'w1',
      title: 'Established In Righteousness',
      description: 'Your position determines your possession. Understanding our identity in Christ.',
      videoUrl: 'https://youtu.be/8ZrWV9VETMw?si=ebEPTWWviaHQ4VYV',
      podcastUrl: 'https://example.com/podcast/1',
      preacher: 'Pastor Julius-Cudjoe',
      date: '2024-01-15',
      series: 'Ephesus 8',
      tags: ['righteousness', 'identity', 'position']
    },
    {
      id: 'w2',
      title: 'How to Train and Protect the Heart',
      description: 'Understanding the heart of man and training it according to God\'s word.',
      videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
      podcastUrl: 'https://example.com/podcast/2',
      preacher: 'Prophet Edem Julius-Cudjoe',
      date: '2024-01-22',
      series: 'Heart Training',
      tags: ['heart', 'training', 'protection']
    },
    {
      id: 'w3',
      title: 'Exercising Our Authority in Christ',
      description: 'Learning to walk in the authority that Christ has given us through prayer and faith.',
      videoUrl: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
      preacher: 'Pastor Julius-Cudjoe',
      date: '2024-01-29',
      series: 'Prayer Seminar',
      tags: ['authority', 'prayer', 'faith']
    },
    ...Array.from({ length: 100 }, (_, i) => ({
      id: `${i + 1}`,
      title: `Sermon Title ${i + 1}`,
      description: `Description for Sermon ${i + 1}`,
      videoUrl: `https://youtu.be/8ZrWV9VETMw?si=ebEPTWWviaHQ4VYV`,
      podcastUrl: `https://example.com/podcast/${i + 1}`,
      preacher: `Preacher ${i % 5 + 1}`,
      date: `2024-01-${(i % 31) + 1}`,
      series: `Series ${Math.floor(i / 10) + 1}`,
      tags: [`tag${i % 3 + 1}`, `tag${i % 5 + 1}`],
    })),
  ],
  series: [
    {
      id: 'w1',
      title: 'Ephesus 8',
      description: 'A deep dive into spiritual establishment and righteousness',
      sermons: ['1'],
      thumbnail: imgs.img_pls_02
    },
    {
      id: 'w2',
      title: 'Heart Training',
      description: 'Understanding and protecting the heart according to God\'s design',
      sermons: ['2'],
      thumbnail: imgs.img_pls_02
    },
    {
      id: 'w3',
      title: 'Prayer Seminar',
      description: 'Exercising our authority in Christ through prayer',
      sermons: ['3'],
      thumbnail: imgs.img_pls_02
    },
    ...Array.from({ length: 10 }, (_, i) => ({
      id: `${i + 1}`,
      title: `Series ${i + 1}`,
      description: `Description for Series ${i + 1}`,
      sermons: Array.from({ length: 10 }, (_, j) => `${i * 10 + j + 1}`),
      thumbnail: imgs.img_pls_02,
    })),
    
  ],
  events: [
    ...Array.from({ length: 10 }, (_, i) => ({
      id: `${i + 1}`,
      title: `Event ${i + 1}`,
      description: `Description for Event ${i + 1}`,
      date: `2024-0${(i % 12) + 1}-15`,
      time: `${(i % 12) + 8}:00`,
      location: `Location ${i + 1}`,
      image: imgs.img_pls_03,
      registrationLink: `https://example.com/register/${i + 1}`,
      featured: i % 2 === 0,
      status: calculateEventStatus(`2024-0${(i % 12) + 1}-15`), // Calculate status dynamically
    })),
  ],
  isLivestreaming: true,
  livestreamUrl: 'https://www.youtube.com/watch?v=live_stream',
  churchSettings: {
    name: 'Miracle Fruits Gathering',
    logo: imgs.logo, // Add logo property to store the church logo
  }
};

function appReducer(state: AppState, action: AppAction): AppState {
  switch (action.type) {
    case 'ADD_SERMON':
      return {
        ...state,
        sermons: [...state.sermons, action.payload]
      };
    case 'UPDATE_SERMON':
      return {
        ...state,
        sermons: state.sermons.map(sermon =>
          sermon.id === action.payload.id ? action.payload : sermon
        )
      };
    case 'DELETE_SERMON':
      return {
        ...state,
        sermons: state.sermons.filter(sermon => sermon.id !== action.payload)
      };
    case 'ADD_SERIES':
      return {
        ...state,
        series: [...state.series, action.payload]
      };
    case 'UPDATE_SERIES':
      return {
        ...state,
        series: state.series.map(series =>
          series.id === action.payload.id ? action.payload : series
        )
      };
    case 'DELETE_SERIES':
      return {
        ...state,
        series: state.series.filter(series => series.id !== action.payload)
      };
    case 'ADD_EVENT':
      return {
        ...state,
        events: [...state.events, action.payload]
      };
    case 'UPDATE_EVENT':
      return {
        ...state,
        events: state.events.map(event =>
          event.id === action.payload.id ? action.payload : event
        )
      };
    case 'DELETE_EVENT':
      return {
        ...state,
        events: state.events.filter(event => event.id !== action.payload)
      };
    case 'SET_LIVESTREAM':
      return {
        ...state,
        isLivestreaming: action.payload.isLive,
        livestreamUrl: action.payload.url
      };
    case 'SET_USER':
      return {
        ...state,
        currentUser: action.payload
      };
    case 'UPDATE_CHURCH_SETTINGS':
      return {
        ...state,
        churchSettings: { 
          name: action.payload.name,
          logo: action.payload.logo  // Preserve existing logo
        },
      };
    default:
      return state;
  }
}

const AppContext = createContext<{
  state: AppState;
  dispatch: React.Dispatch<AppAction>;
} | null>(null);

export function AppProvider({ children }: { children: ReactNode }) {
  const [state, dispatch] = useReducer(appReducer, initialState);

  return (
    <AppContext.Provider value={{ state, dispatch }}>
      {children}
    </AppContext.Provider>
  );
}

export function useAppContext() {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useAppContext must be used within an AppProvider');
  }
  return context;
}