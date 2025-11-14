import { useEffect, useRef, useState } from 'react';
import { Platform, Alert } from 'react-native';
import { useAppStore } from '../stores/appStore';

// Note: This is a mock implementation for screen recording
// In a real app, you would use platform-specific APIs:
// - iOS: ReplayKit framework
// - Android: MediaProjection API

interface ScreenRecordingHook {
  startScreenRecording: () => Promise<void>;
  stopScreenRecording: () => Promise<string | null>;
  isRecording: boolean;
  error: string | null;
}

export const useScreenRecording = (): ScreenRecordingHook => {
  const { recording, settings } = useAppStore();
  const [error, setError] = useState<string | null>(null);
  const recordingRef = useRef<any>(null);

  const requestScreenRecordingPermissions = async (): Promise<boolean> => {
    try {
      if (Platform.OS === 'android') {
        // Android: Request MediaProjection permission
        // This would typically show a system dialog
        return new Promise((resolve) => {
          Alert.alert(
            settings.language === 'ja' ? '画面録画の許可' : 'Screen Recording Permission',
            settings.language === 'ja' 
              ? '画面録画を開始するには許可が必要です'
              : 'Permission needed to start screen recording',
            [
              {
                text: settings.language === 'ja' ? 'キャンセル' : 'Cancel',
                onPress: () => resolve(false),
                style: 'cancel',
              },
              {
                text: settings.language === 'ja' ? '許可' : 'Allow',
                onPress: () => resolve(true),
              },
            ]
          );
        });
      } else if (Platform.OS === 'ios') {
        // iOS: ReplayKit doesn't require explicit permission
        return true;
      }
      return false;
    } catch (err) {
      console.error('Permission request failed:', err);
      return false;
    }
  };

  const startScreenRecording = async (): Promise<void> => {
    try {
      setError(null);

      const hasPermission = await requestScreenRecordingPermissions();
      if (!hasPermission) {
        throw new Error('Permission denied');
      }

      if (Platform.OS === 'android') {
        // Android implementation using MediaProjection
        // This is a mock - in real implementation you would:
        // 1. Start MediaProjection service
        // 2. Create MediaRecorder
        // 3. Start recording
        console.log('Starting Android screen recording...');
        recordingRef.current = {
          platform: 'android',
          startTime: Date.now(),
        };
      } else if (Platform.OS === 'ios') {
        // iOS implementation using ReplayKit
        // This is a mock - in real implementation you would:
        // 1. Import ReplayKit
        // 2. Start recording with RPScreenRecorder
        console.log('Starting iOS screen recording...');
        recordingRef.current = {
          platform: 'ios',
          startTime: Date.now(),
        };
      }

      console.log(`Screen recording started with quality: ${settings.videoQuality}, FPS: ${settings.frameRate}`);
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Unknown error';
      setError(errorMessage);
      throw err;
    }
  };

  const stopScreenRecording = async (): Promise<string | null> => {
    try {
      setError(null);

      if (!recordingRef.current) {
        return null;
      }

      const platform = recordingRef.current.platform;
      const startTime = recordingRef.current.startTime;
      const duration = Date.now() - startTime;

      let videoPath: string | null = null;

      if (platform === 'android') {
        // Android: Stop MediaRecorder and get file path
        console.log('Stopping Android screen recording...');
        videoPath = `/storage/emulated/0/Movies/GameRecorder/recording_${Date.now()}.mp4`;
      } else if (platform === 'ios') {
        // iOS: Stop ReplayKit and get temporary file URL
        console.log('Stopping iOS screen recording...');
        videoPath = `file:///var/mobile/Containers/Data/Application/GameRecorder/Documents/recording_${Date.now()}.mp4`;
      }

      recordingRef.current = null;
      console.log(`Screen recording stopped. Duration: ${duration}ms, Path: ${videoPath}`);
      
      return videoPath;
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Unknown error';
      setError(errorMessage);
      console.error('Stop recording error:', err);
      return null;
    }
  };

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (recordingRef.current) {
        stopScreenRecording();
      }
    };
  }, []);

  return {
    startScreenRecording,
    stopScreenRecording,
    isRecording: !!recordingRef.current,
    error,
  };
};