import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';

interface PerformanceStats {
  fps: number;
  memoryUsage: number;
  renderTime: number;
}

export const PerformanceMonitor: React.FC<{ enabled?: boolean }> = ({ 
  enabled = false 
}) => {
  const [stats, setStats] = useState<PerformanceStats>({
    fps: 60,
    memoryUsage: 0,
    renderTime: 0,
  });

  useEffect(() => {
    if (!enabled) return;

    let frameCount = 0;
    let lastTime = performance.now();
    let animationId: number;

    const measurePerformance = () => {
      const currentTime = performance.now();
      frameCount++;

      // Calculate FPS every second
      if (currentTime - lastTime >= 1000) {
        const fps = Math.round((frameCount * 1000) / (currentTime - lastTime));
        frameCount = 0;
        lastTime = currentTime;

        // Mock memory usage (in MB)
        const memoryUsage = Math.random() * 100 + 50;
        
        // Mock render time (in ms)
        const renderTime = Math.random() * 5 + 1;

        setStats({
          fps: fps,
          memoryUsage: Math.round(memoryUsage),
          renderTime: Math.round(renderTime * 10) / 10,
        });
      }

      animationId = requestAnimationFrame(measurePerformance);
    };

    animationId = requestAnimationFrame(measurePerformance);

    return () => {
      if (animationId) {
        cancelAnimationFrame(animationId);
      }
    };
  }, [enabled]);

  if (!enabled) {
    return null;
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Performance</Text>
      <Text style={styles.stat}>FPS: {stats.fps}</Text>
      <Text style={styles.stat}>Memory: {stats.memoryUsage}MB</Text>
      <Text style={styles.stat}>Render: {stats.renderTime}ms</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    position: 'absolute',
    top: 100,
    right: 10,
    backgroundColor: 'rgba(0, 0, 0, 0.8)',
    padding: 8,
    borderRadius: 8,
    zIndex: 9999,
  },
  title: {
    color: '#FFFFFF',
    fontSize: 12,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  stat: {
    color: '#FFFFFF',
    fontSize: 10,
    fontFamily: 'monospace',
  },
});