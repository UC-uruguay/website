import { create } from 'zustand';
import { RecordingState, CameraState, AppSettings, NavigationState, VideoFile, ScreenName } from '../types';

interface AppStore {
  // Recording state
  recording: RecordingState;
  setRecording: (recording: Partial<RecordingState>) => void;
  startRecording: () => void;
  stopRecording: () => void;
  pauseRecording: () => void;
  resumeRecording: () => void;

  // Camera state
  camera: CameraState;
  setCamera: (camera: Partial<CameraState>) => void;
  toggleCamera: () => void;
  toggleCameraPosition: () => void;
  updatePreviewPosition: (position: { x: number; y: number }) => void;

  // Settings
  settings: AppSettings;
  updateSettings: (settings: Partial<AppSettings>) => void;

  // Navigation
  navigation: NavigationState;
  navigateTo: (screen: ScreenName) => void;
  goBack: () => void;

  // Videos
  videos: VideoFile[];
  addVideo: (video: VideoFile) => void;
  deleteVideo: (id: string) => void;
  updateVideo: (id: string, updates: Partial<VideoFile>) => void;
}

export const useAppStore = create<AppStore>((set, get) => ({
  // Initial recording state
  recording: {
    isRecording: false,
    isPaused: false,
    startTime: null,
    duration: 0,
    videoPath: null,
  },

  setRecording: (recording) =>
    set((state) => ({
      recording: { ...state.recording, ...recording },
    })),

  startRecording: () =>
    set((state) => ({
      recording: {
        ...state.recording,
        isRecording: true,
        isPaused: false,
        startTime: Date.now(),
        duration: 0,
      },
    })),

  stopRecording: () =>
    set((state) => ({
      recording: {
        ...state.recording,
        isRecording: false,
        isPaused: false,
        startTime: null,
        duration: 0,
        videoPath: null,
      },
    })),

  pauseRecording: () =>
    set((state) => ({
      recording: {
        ...state.recording,
        isPaused: true,
      },
    })),

  resumeRecording: () =>
    set((state) => ({
      recording: {
        ...state.recording,
        isPaused: false,
      },
    })),

  // Initial camera state
  camera: {
    isActive: false,
    isFrontCamera: true,
    showPreview: true,
    previewPosition: { x: 20, y: 100 },
    previewSize: { width: 120, height: 160 },
  },

  setCamera: (camera) =>
    set((state) => ({
      camera: { ...state.camera, ...camera },
    })),

  toggleCamera: () =>
    set((state) => ({
      camera: {
        ...state.camera,
        isActive: !state.camera.isActive,
      },
    })),

  toggleCameraPosition: () =>
    set((state) => ({
      camera: {
        ...state.camera,
        isFrontCamera: !state.camera.isFrontCamera,
      },
    })),

  updatePreviewPosition: (position) =>
    set((state) => ({
      camera: {
        ...state.camera,
        previewPosition: position,
      },
    })),

  // Initial settings
  settings: {
    videoQuality: 'HD',
    frameRate: 30,
    audioEnabled: true,
    cameraOverlayEnabled: true,
    language: 'ja',
    theme: 'light',
  },

  updateSettings: (settings) =>
    set((state) => ({
      settings: { ...state.settings, ...settings },
    })),

  // Initial navigation
  navigation: {
    currentScreen: 'Home',
    history: [],
  },

  navigateTo: (screen) =>
    set((state) => ({
      navigation: {
        currentScreen: screen,
        history: [...state.navigation.history, state.navigation.currentScreen],
      },
    })),

  goBack: () =>
    set((state) => {
      const history = [...state.navigation.history];
      const previousScreen = history.pop() as ScreenName;
      return {
        navigation: {
          currentScreen: previousScreen || 'Home',
          history,
        },
      };
    }),

  // Initial videos
  videos: [],

  addVideo: (video) =>
    set((state) => ({
      videos: [video, ...state.videos],
    })),

  deleteVideo: (id) =>
    set((state) => ({
      videos: state.videos.filter((video) => video.id !== id),
    })),

  updateVideo: (id, updates) =>
    set((state) => ({
      videos: state.videos.map((video) =>
        video.id === id ? { ...video, ...updates } : video
      ),
    })),
}));