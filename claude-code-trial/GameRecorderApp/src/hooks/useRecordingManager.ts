import { useCallback, useEffect, useState } from 'react';
import { Alert, Platform } from 'react-native';
import { useAppStore } from '../stores/appStore';
import { useScreenRecording } from './useScreenRecording';
import { useCameraRecording } from './useCameraRecording';
import { VideoUtils } from '../utils/videoUtils';
import { backgroundService } from '../services/BackgroundService';

export const useRecordingManager = () => {
  const {
    recording,
    camera,
    settings,
    setRecording,
    toggleCamera,
    addVideo,
    startRecording: storeStartRecording,
    stopRecording: storeStopRecording,
  } = useAppStore();

  const screenRecording = useScreenRecording();
  const cameraRecording = useCameraRecording();
  const [isInitializing, setIsInitializing] = useState(false);

  // Initialize background service permissions
  useEffect(() => {
    const initializeBackgroundService = async () => {
      try {
        const hasPermission = await backgroundService.requestBackgroundPermissions();
        if (!hasPermission) {
          console.warn('Background permissions not granted');
        }
      } catch (error) {
        console.error('Background service initialization failed:', error);
      }
    };

    initializeBackgroundService();

    // Cleanup on unmount
    return () => {
      if (recording.isRecording) {
        handleStopRecording();
      }
    };
  }, []);

  const handleStartRecording = useCallback(async () => {
    if (isInitializing) return;

    try {
      setIsInitializing(true);
      
      // Update store state first
      storeStartRecording();

      // Start foreground service for background recording
      const serviceTitle = settings.language === 'ja' 
        ? 'ゲーム録画中' 
        : 'Game Recording';
      const serviceMessage = settings.language === 'ja'
        ? 'タップして戻る'
        : 'Tap to return';
      
      backgroundService.startForegroundService(serviceTitle, serviceMessage);

      // Start screen recording
      await screenRecording.startScreenRecording();
      console.log('Screen recording started');

      // Start camera recording if enabled
      if (settings.cameraOverlayEnabled && camera.isActive) {
        await cameraRecording.startCameraRecording();
        console.log('Camera recording started');
      }

      // Activate camera preview if not already active
      if (settings.cameraOverlayEnabled && !camera.isActive) {
        toggleCamera();
      }

      console.log('Recording started successfully');
    } catch (error) {
      console.error('Failed to start recording:', error);
      
      // Revert store state on error
      storeStopRecording();
      backgroundService.stopForegroundService();
      
      Alert.alert(
        settings.language === 'ja' ? 'エラー' : 'Error',
        settings.language === 'ja' 
          ? '録画の開始に失敗しました'
          : 'Failed to start recording'
      );
    } finally {
      setIsInitializing(false);
    }
  }, [
    isInitializing,
    screenRecording,
    cameraRecording,
    camera.isActive,
    settings,
    storeStartRecording,
    storeStopRecording,
    toggleCamera,
  ]);

  const handleStopRecording = useCallback(async () => {
    if (isInitializing) return;

    try {
      setIsInitializing(true);

      // Stop foreground service
      backgroundService.stopForegroundService();

      // Stop screen recording
      const screenVideoPath = await screenRecording.stopScreenRecording();
      console.log('Screen recording stopped:', screenVideoPath);

      // Stop camera recording if it was active
      let cameraVideoPath: string | null = null;
      if (cameraRecording.isRecording) {
        cameraVideoPath = await cameraRecording.stopCameraRecording();
        console.log('Camera recording stopped:', cameraVideoPath);
      }

      // Update store state
      storeStopRecording();

      // Process and save the video
      if (screenVideoPath) {
        try {
          const videoFile = await VideoUtils.createVideoFile(
            screenVideoPath,
            cameraVideoPath || undefined
          );
          
          addVideo(videoFile);
          
          Alert.alert(
            settings.language === 'ja' ? '録画完了' : 'Recording Completed',
            settings.language === 'ja' 
              ? '動画が保存されました'
              : 'Video has been saved',
            [
              {
                text: 'OK',
                onPress: () => console.log('Recording completion acknowledged'),
              },
            ]
          );
        } catch (saveError) {
          console.error('Failed to save video:', saveError);
          Alert.alert(
            settings.language === 'ja' ? 'エラー' : 'Error',
            settings.language === 'ja' 
              ? '動画の保存に失敗しました'
              : 'Failed to save video'
          );
        }
      }

      console.log('Recording stopped successfully');
    } catch (error) {
      console.error('Failed to stop recording:', error);
      
      Alert.alert(
        settings.language === 'ja' ? 'エラー' : 'Error',
        settings.language === 'ja' 
          ? '録画の停止に失敗しました'
          : 'Failed to stop recording'
      );
    } finally {
      setIsInitializing(false);
    }
  }, [
    isInitializing,
    screenRecording,
    cameraRecording,
    settings,
    storeStopRecording,
    addVideo,
  ]);

  const handlePauseRecording = useCallback(async () => {
    // Note: Pausing screen recording is complex and not supported by all platforms
    // This is a placeholder for pause functionality
    try {
      console.log('Pause recording requested');
      
      // In a real implementation, you would:
      // 1. Pause the screen recording service
      // 2. Pause the camera recording
      // 3. Update the recording state
      
      Alert.alert(
        settings.language === 'ja' ? '情報' : 'Info',
        settings.language === 'ja' 
          ? '一時停止機能は開発中です'
          : 'Pause functionality is under development'
      );
    } catch (error) {
      console.error('Failed to pause recording:', error);
    }
  }, [settings]);

  const isRecordingActive = recording.isRecording || isInitializing;
  const hasErrors = screenRecording.error || cameraRecording.error;

  return {
    isRecording: isRecordingActive,
    isInitializing,
    startRecording: handleStartRecording,
    stopRecording: handleStopRecording,
    pauseRecording: handlePauseRecording,
    errors: {
      screen: screenRecording.error,
      camera: cameraRecording.error,
    },
    hasErrors,
  };
};