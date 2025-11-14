export interface RecordingState {
  isRecording: boolean;
  isPaused: boolean;
  startTime: number | null;
  duration: number;
  videoPath: string | null;
}

export interface CameraState {
  isActive: boolean;
  isFrontCamera: boolean;
  showPreview: boolean;
  previewPosition: { x: number; y: number };
  previewSize: { width: number; height: number };
}

export interface AppSettings {
  videoQuality: 'HD' | 'FHD' | '4K';
  frameRate: 30 | 60;
  audioEnabled: boolean;
  cameraOverlayEnabled: boolean;
  language: 'ja' | 'en';
  theme: 'light' | 'dark';
}

export interface VideoFile {
  id: string;
  path: string;
  thumbnail: string;
  duration: number;
  createdAt: Date;
  size: number;
  name: string;
}

export type ScreenName = 'Home' | 'Recording' | 'Gallery' | 'Settings';

export interface NavigationState {
  currentScreen: ScreenName;
  history: ScreenName[];
}