import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { useAppStore } from '../stores/appStore';

export const RecordingTimer: React.FC = () => {
  const { recording } = useAppStore();
  const [displayTime, setDisplayTime] = useState('00:00');

  useEffect(() => {
    let interval: NodeJS.Timeout;

    if (recording.isRecording && !recording.isPaused && recording.startTime) {
      interval = setInterval(() => {
        const elapsed = Date.now() - recording.startTime!;
        const minutes = Math.floor(elapsed / 60000);
        const seconds = Math.floor((elapsed % 60000) / 1000);
        setDisplayTime(
          `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`
        );
      }, 1000);
    }

    return () => {
      if (interval) {
        clearInterval(interval);
      }
    };
  }, [recording.isRecording, recording.isPaused, recording.startTime]);

  if (!recording.isRecording) {
    return null;
  }

  return (
    <View style={styles.container}>
      <View style={[styles.indicator, recording.isPaused && styles.paused]} />
      <Text style={styles.time}>{displayTime}</Text>
      {recording.isPaused && (
        <Text style={styles.pausedText}>⏸️</Text>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.8)',
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 20,
    position: 'absolute',
    top: 60,
    alignSelf: 'center',
    zIndex: 1000,
  },
  indicator: {
    width: 12,
    height: 12,
    borderRadius: 6,
    backgroundColor: '#FF4757',
    marginRight: 8,
    shadowColor: '#FF4757',
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.8,
    shadowRadius: 4,
  },
  paused: {
    backgroundColor: '#FFA502',
    shadowColor: '#FFA502',
  },
  time: {
    color: '#FFFFFF',
    fontSize: 18,
    fontWeight: '600',
    fontFamily: 'monospace',
    marginRight: 8,
  },
  pausedText: {
    fontSize: 16,
  },
});