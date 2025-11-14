import { AppState, AppStateStatus } from 'react-native';
import BackgroundJob from 'react-native-background-job';
import { useAppStore } from '../stores/appStore';

export class BackgroundService {
  private static instance: BackgroundService;
  private appStateSubscription: any;
  private backgroundJobStarted = false;
  private recordingCheckInterval: NodeJS.Timeout | null = null;

  private constructor() {
    this.initializeAppStateListener();
  }

  public static getInstance(): BackgroundService {
    if (!BackgroundService.instance) {
      BackgroundService.instance = new BackgroundService();
    }
    return BackgroundService.instance;
  }

  private initializeAppStateListener() {
    this.appStateSubscription = AppState.addEventListener(
      'change',
      this.handleAppStateChange.bind(this)
    );
  }

  private handleAppStateChange(nextAppState: AppStateStatus) {
    const { recording } = useAppStore.getState();
    
    console.log('App state changed to:', nextAppState);
    
    if (nextAppState === 'background' && recording.isRecording) {
      this.startBackgroundRecording();
    } else if (nextAppState === 'active') {
      this.stopBackgroundRecording();
    }
  }

  private startBackgroundRecording() {
    if (this.backgroundJobStarted) {
      return;
    }

    try {
      BackgroundJob.start({
        jobKey: 'gameRecording',
        period: 15000, // Check every 15 seconds (minimum allowed)
      });

      this.backgroundJobStarted = true;
      
      // Set up periodic check for recording state
      this.recordingCheckInterval = setInterval(() => {
        this.checkRecordingState();
      }, 1000);

      console.log('Background recording service started');
    } catch (error) {
      console.error('Failed to start background recording:', error);
    }
  }

  private stopBackgroundRecording() {
    if (!this.backgroundJobStarted) {
      return;
    }

    try {
      BackgroundJob.stop({
        jobKey: 'gameRecording',
      });

      this.backgroundJobStarted = false;

      if (this.recordingCheckInterval) {
        clearInterval(this.recordingCheckInterval);
        this.recordingCheckInterval = null;
      }

      console.log('Background recording service stopped');
    } catch (error) {
      console.error('Failed to stop background recording:', error);
    }
  }

  private checkRecordingState() {
    const { recording } = useAppStore.getState();
    
    if (!recording.isRecording) {
      // Recording was stopped, clean up background service
      this.stopBackgroundRecording();
      return;
    }

    // Ensure recording is still active
    // In a real implementation, you would check the actual recording status
    // from the native recording services
    console.log('Background recording check - still recording');
  }

  public async requestBackgroundPermissions(): Promise<boolean> {
    try {
      // For Android, you would request FOREGROUND_SERVICE permission
      // For iOS, background app refresh needs to be enabled
      
      console.log('Requesting background permissions...');
      
      // Mock permission request
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve(true);
        }, 1000);
      });
    } catch (error) {
      console.error('Background permission request failed:', error);
      return false;
    }
  }

  public startForegroundService(title: string, message: string) {
    try {
      // This would start a foreground service notification on Android
      // to keep the app running in the background
      
      console.log('Starting foreground service:', { title, message });
      
      // Mock implementation - in real app you would use:
      // - Android: Foreground Service with ongoing notification
      // - iOS: Background App Refresh + Audio session for continuous recording
      
    } catch (error) {
      console.error('Failed to start foreground service:', error);
    }
  }

  public stopForegroundService() {
    try {
      console.log('Stopping foreground service');
      
      // Stop the foreground service and remove notification
      
    } catch (error) {
      console.error('Failed to stop foreground service:', error);
    }
  }

  public destroy() {
    if (this.appStateSubscription) {
      this.appStateSubscription?.remove();
    }
    
    if (this.recordingCheckInterval) {
      clearInterval(this.recordingCheckInterval);
    }
    
    this.stopBackgroundRecording();
    
    console.log('Background service destroyed');
  }
}

// Export singleton instance
export const backgroundService = BackgroundService.getInstance();