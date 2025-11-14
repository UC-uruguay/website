import React, { useState, useMemo } from 'react';
import { Mountain, Camera, MapPin } from 'lucide-react';
import { municipalities as initialMunicipalities } from './data/municipalities';
import { ProgressBar } from './components/ProgressBar';
import { MunicipalityCard } from './components/MunicipalityCard';
import { Municipality } from './types';

function App() {
  const [municipalities, setMunicipalities] = useState<Municipality[]>(initialMunicipalities);

  const stats = useMemo(() => {
    const completed = municipalities.filter(m => m.isCompleted).length;
    return {
      completed,
      total: municipalities.length,
      percentage: Math.round((completed / municipalities.length) * 100)
    };
  }, [municipalities]);

  const handleToggleComplete = (id: string) => {
    setMunicipalities(prev =>
      prev.map(m =>
        m.id === id
          ? { ...m, isCompleted: !m.isCompleted, visitDate: !m.isCompleted ? new Date() : undefined }
          : m
      )
    );
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <div
        className="relative bg-cover bg-center h-96"
        style={{
          backgroundImage: 'url("https://images.unsplash.com/photo-1490806843957-31f4c9a91c65?ixlib=rb-1.2.1&auto=format&fit=crop&w=2850&q=80")',
        }}
      >
        <div className="absolute inset-0 bg-black bg-opacity-50" />
        <div className="relative container mx-auto px-4 h-full flex flex-col justify-center items-center text-white">
          <h1 className="text-4xl md:text-6xl font-bold mb-4 text-center">
            山梨27市町村制覇チャレンジ
          </h1>
          <p className="text-xl md:text-2xl text-center mb-8">
            山梨県の全27市町村を巡る冒険の記録
          </p>
          <div className="flex gap-4 text-sm md:text-base">
            <div className="flex items-center gap-2">
              <Mountain className="w-5 h-5" />
              <span>27市町村</span>
            </div>
            <div className="flex items-center gap-2">
              <Camera className="w-5 h-5" />
              <span>思い出を記録</span>
            </div>
            <div className="flex items-center gap-2">
              <MapPin className="w-5 h-5" />
              <span>進捗を共有</span>
            </div>
          </div>
        </div>
      </div>

      {/* Progress Section */}
      <div className="container mx-auto px-4 py-8">
        <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4">進捗状況</h2>
          <ProgressBar stats={stats} />
        </div>

        {/* Municipalities Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {municipalities.map(municipality => (
            <MunicipalityCard
              key={municipality.id}
              municipality={municipality}
              onToggleComplete={handleToggleComplete}
            />
          ))}
        </div>
      </div>

      {/* Social Feed Section */}
      <div className="container mx-auto px-4 py-8">
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-2xl font-bold mb-4">SNSでシェア</h2>
          <p className="text-gray-600 mb-4">
            あなたの冒険を #山梨27 でシェアしよう！
          </p>
          <div className="flex gap-4">
            <a
              href="https://twitter.com/intent/tweet?hashtags=山梨27"
              target="_blank"
              rel="noopener noreferrer"
              className="bg-blue-400 text-white px-6 py-2 rounded-full hover:bg-blue-500 transition-colors"
            >
              X (Twitter)でシェア
            </a>
            <a
              href="https://www.instagram.com/explore/tags/山梨27/"
              target="_blank"
              rel="noopener noreferrer"
              className="bg-gradient-to-r from-purple-500 to-pink-500 text-white px-6 py-2 rounded-full hover:opacity-90 transition-opacity"
            >
              Instagramでシェア
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;