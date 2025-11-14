import React from 'react';
import { MapPin, Calendar, Image as ImageIcon, CheckCircle2, Circle } from 'lucide-react';
import { Municipality } from '../types';
import { format } from 'date-fns';
import { ja } from 'date-fns/locale';

interface MunicipalityCardProps {
  municipality: Municipality;
  onToggleComplete: (id: string) => void;
}

export const MunicipalityCard: React.FC<MunicipalityCardProps> = ({
  municipality,
  onToggleComplete,
}) => {
  return (
    <div
      className={`relative p-4 rounded-lg shadow-md transition-all duration-300 ${
        municipality.isCompleted
          ? 'bg-green-50 border-2 border-green-500'
          : 'bg-white border border-gray-200 hover:border-blue-300'
      }`}
      onClick={() => onToggleComplete(municipality.id)}
      role="button"
      tabIndex={0}
    >
      <div className="absolute top-4 right-4 transition-transform duration-300 transform">
        {municipality.isCompleted ? (
          <CheckCircle2 size={24} className="text-green-600" />
        ) : (
          <Circle size={24} className="text-gray-400" />
        )}
      </div>
      
      <h3 className="text-xl font-bold mb-1 pr-8">{municipality.name}</h3>
      <p className="text-sm text-gray-600 mb-3">{municipality.reading}</p>
      
      <div className={`flex items-center gap-2 text-sm mb-2 transition-colors duration-300 ${
        municipality.isCompleted ? 'text-green-700' : 'text-blue-600'
      }`}>
        <MapPin size={16} className={municipality.isCompleted ? 'text-green-500' : 'text-blue-500'} />
        <span className="font-medium">
          {municipality.isCompleted ? '訪問済み' : 'これから行く！'}
        </span>
      </div>

      {municipality.visitDate && (
        <div className="flex items-center gap-2 text-sm text-gray-700 mb-2">
          <Calendar size={16} className="text-blue-500" />
          <span>{format(municipality.visitDate, 'yyyy年MM月dd日', { locale: ja })}</span>
        </div>
      )}

      {municipality.photos.length > 0 && (
        <div className="flex items-center gap-2 text-sm text-gray-700">
          <ImageIcon size={16} className="text-pink-500" />
          <span>{municipality.photos.length}枚の写真</span>
        </div>
      )}

      <div className={`absolute bottom-0 left-0 w-full h-1 rounded-b-lg transition-all duration-300 ${
        municipality.isCompleted ? 'bg-green-500' : 'bg-transparent'
      }`} />
    </div>
  );
};