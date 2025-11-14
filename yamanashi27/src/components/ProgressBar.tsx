import React from 'react';
import { ProgressStats } from '../types';

interface ProgressBarProps {
  stats: ProgressStats;
}

export const ProgressBar: React.FC<ProgressBarProps> = ({ stats }) => {
  return (
    <div className="w-full bg-gray-200 rounded-full h-6 dark:bg-gray-700">
      <div
        className="bg-gradient-to-r from-purple-500 to-pink-500 h-6 rounded-full transition-all duration-500 ease-out"
        style={{ width: `${stats.percentage}%` }}
      >
        <div className="flex items-center justify-center h-full text-xs font-medium text-white">
          {stats.completed}/{stats.total} ({stats.percentage}%)
        </div>
      </div>
    </div>
  );
};