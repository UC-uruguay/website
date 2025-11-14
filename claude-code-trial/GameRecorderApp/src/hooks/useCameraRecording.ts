import { useRef, useState, useCallback } from 'react';
import { Platform } from 'react-native';
import { Camera, useCameraDevice } from 'react-native-vision-camera';
import { useAppStore } from '../stores/appStore';

interface CameraRecordingHook {
  startCameraRecording: () => Promise<void>;
  stopCameraRecording: () => Promise<string | null>;
  isRecording: boolean;
  error: string | null;
  cameraRef: React.RefObject<Camera>;
}

export const useCameraRecording = (): CameraRecordingHook => {
  const { camera, settings } = useAppStore();
  const [error, setError] = useState<string | null>(null);
  const [isRecording, setIsRecording] = useState(false);
  const cameraRef = useRef<Camera>(null);

  const device = useCameraDevice(camera.isFrontCamera ? 'front' : 'back');

  const startCameraRecording = useCallback(async (): Promise<void> => {
    try {
      setError(null);

      if (!cameraRef.current || !device) {
        throw new Error('Camera not available');
      }

      const videoCodec = Platform.OS === 'ios' ? 'h264' : 'h264';
      const videoBitRate = settings.videoQuality === '4K' ? 20000000 : 
                          settings.videoQuality === 'FHD' ? 10000000 : 5000000;

      await cameraRef.current.startRecording({
        flash: 'off',
        onRecordingFinished: (video) => {
          console.log('Camera recording finished:', video.path);
          setIsRecording(false);
        },
        onRecordingError: (error) => {
          console.error('Camera recording error:', error);
          setError(error.message);
          setIsRecording(false);
        },
        videoCodec: videoCodec,
        videoBitRate: videoBitRate,
      });

      setIsRecording(true);
      console.log('Camera recording started');
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Unknown error';
      setError(errorMessage);
      console.error('Start camera recording error:', err);
      throw err;
    }
  }, [device, settings]);

  const stopCameraRecording = useCallback(async (): Promise<string | null> => {
    try {
      setError(null);

      if (!cameraRef.current || !isRecording) {
        return null;
      }

      await cameraRef.current.stopRecording();
      setIsRecording(false);
      
      console.log('Camera recording stopped');
      
      // The actual video path will be provided in the onRecordingFinished callback
      // For now, return a mock path
      return `/path/to/camera/recording_${Date.now()}.mp4`;
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Unknown error';
      setError(errorMessage);
      console.error('Stop camera recording error:', err);
      return null;
    }
  }, [isRecording]);

  return {
    startCameraRecording,
    stopCameraRecording,
    isRecording,
    error,
    cameraRef,
  };
};