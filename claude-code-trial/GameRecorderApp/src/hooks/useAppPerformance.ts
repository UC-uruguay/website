import { useEffect, useState, useCallback } from 'react';
import { AppState, AppStateStatus } from 'react-native';
import { PerformanceUtils } from '../utils/performanceUtils';

interface PerformanceState {
  isOptimized: boolean;
  memoryWarning: boolean;
  backgroundTime: number;
  foregroundTime: number;
}

export const useAppPerformance = () => {
  const [performance, setPerformance] = useState<PerformanceState>({
    isOptimized: true,
    memoryWarning: false,
    backgroundTime: 0,
    foregroundTime: Date.now(),
  });

  const [appState, setAppState] = useState(AppState.currentState);

  const optimizeForRecording = useCallback(() => {
    console.log('Optimizing app for recording...');
    
    // Reduce background processes
    PerformanceUtils.clearPerformanceMarks();
    
    // Enable performance monitoring
    setPerformance(prev => ({
      ...prev,
      isOptimized: true,
    }));
  }, []);

  const restoreNormalPerformance = useCallback(() => {
    console.log('Restoring normal performance...');
    
    setPerformance(prev => ({
      ...prev,
      isOptimized: false,
    }));
  }, []);

  const checkMemoryUsage = useCallback(() => {
    const hasMemoryWarning = PerformanceUtils.getMemoryWarning();
    
    setPerformance(prev => ({
      ...prev,
      memoryWarning: hasMemoryWarning,
    }));

    if (hasMemoryWarning) {
      console.warn('Memory usage is high - consider optimizing');
    }
  }, []);

  const handleAppStateChange = useCallback((nextAppState: AppStateStatus) => {
    const now = Date.now();
    
    if (appState === 'active' && nextAppState.match(/inactive|background/)) {
      // App going to background
      setPerformance(prev => ({
        ...prev,
        backgroundTime: now,
      }));
    } else if (appState.match(/inactive|background/) && nextAppState === 'active') {
      // App coming to foreground
      setPerformance(prev => ({
        ...prev,
        foregroundTime: now,
      }));
    }
    
    setAppState(nextAppState);
  }, [appState]);

  useEffect(() => {
    const subscription = AppState.addEventListener('change', handleAppStateChange);
    
    // Check memory usage periodically
    const memoryCheckInterval = setInterval(checkMemoryUsage, 10000); // Every 10 seconds
    
    return () => {
      subscription?.remove();
      clearInterval(memoryCheckInterval);
    };
  }, [handleAppStateChange, checkMemoryUsage]);

  const getPerformanceScore = useCallback((): number => {
    let score = 100;
    
    if (performance.memoryWarning) score -= 30;
    if (!performance.isOptimized) score -= 10;
    
    return Math.max(0, score);
  }, [performance]);

  const getPerformanceRecommendations = useCallback((): string[] => {
    const recommendations: string[] = [];
    
    if (performance.memoryWarning) {
      recommendations.push('Close other apps to free memory');
      recommendations.push('Restart the app if performance issues persist');
    }
    
    if (!performance.isOptimized) {
      recommendations.push('Enable recording optimization');
    }
    
    return recommendations;
  }, [performance]);

  return {
    performance,
    appState,
    optimizeForRecording,
    restoreNormalPerformance,
    checkMemoryUsage,
    getPerformanceScore,
    getPerformanceRecommendations,
  };
};