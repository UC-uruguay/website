import React, { useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  StatusBar,
  SafeAreaView,
  Alert,
} from 'react-native';
import { Camera } from 'react-native-vision-camera';
import { request, PERMISSIONS, RESULTS } from 'react-native-permissions';
import { UniversalButton } from '../components/UniversalButton';
import { RecordingTimer } from '../components/RecordingTimer';
import { CameraPreview } from '../components/CameraPreview';
import { PerformanceMonitor } from '../components/PerformanceMonitor';
import { useAppStore } from '../stores/appStore';
import { useRecordingManager } from '../hooks/useRecordingManager';
import { useAppPerformance } from '../hooks/useAppPerformance';

export const HomeScreen: React.FC = () => {
  const {
    recording,
    camera,
    settings,
    toggleCamera,
    navigateTo,
  } = useAppStore();

  const {
    isRecording,
    isInitializing,
    startRecording,
    stopRecording,
    hasErrors,
    errors,
  } = useRecordingManager();

  const {
    performance,
    optimizeForRecording,
    restoreNormalPerformance,
    getPerformanceScore,
  } = useAppPerformance();

  useEffect(() => {
    requestPermissions();
  }, []);

  const requestPermissions = async () => {
    try {
      const cameraPermission = await request(PERMISSIONS.ANDROID.CAMERA);
      const microphonePermission = await request(PERMISSIONS.ANDROID.RECORD_AUDIO);
      
      if (cameraPermission !== RESULTS.GRANTED || microphonePermission !== RESULTS.GRANTED) {
        Alert.alert(
          settings.language === 'ja' ? '権限が必要です' : 'Permissions Required',
          settings.language === 'ja' 
            ? 'カメラとマイクの権限を許可してください'
            : 'Please grant camera and microphone permissions'
        );
      }
    } catch (error) {
      console.error('Permission request error:', error);
    }
  };

  const handleRecordPress = () => {
    if (isRecording) {
      stopRecording();
      restoreNormalPerformance();
    } else {
      optimizeForRecording();
      startRecording();
    }
  };

  const getRecordButtonText = () => {
    if (isInitializing) {
      return settings.language === 'ja' ? '準備中...' : 'Preparing...';
    }
    if (isRecording) {
      return settings.language === 'ja' ? '停止' : 'Stop';
    }
    return settings.language === 'ja' ? '録画開始' : 'Start Recording';
  };

  const getRecordButtonIcon = () => {
    if (isInitializing) {
      return '⏳';
    }
    return isRecording ? '⏹️' : '🎬';
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="light-content" backgroundColor="#2C3E50" />
      
      <RecordingTimer />
      <CameraPreview />
      <PerformanceMonitor enabled={__DEV__ && isRecording} />

      <View style={styles.header}>
        <Text style={styles.title}>
          {settings.language === 'ja' ? 'ゲーム録画' : 'Game Recorder'}
        </Text>
        <Text style={styles.subtitle}>
          {settings.language === 'ja' 
            ? '画面と表情を同時に記録'
            : 'Record screen and expressions'}
        </Text>
      </View>

      <View style={styles.mainContent}>
        <View style={styles.recordButtonContainer}>
          <UniversalButton
            onPress={handleRecordPress}
            icon={getRecordButtonIcon()}
            text={getRecordButtonText()}
            variant={isRecording ? 'danger' : 'primary'}
            size="xlarge"
            style={styles.recordButton}
            disabled={isInitializing}
            testID="record-button"
          />
        </View>

        <View style={styles.secondaryActions}>
          <UniversalButton
            onPress={toggleCamera}
            icon={camera.isActive ? '📹' : '📹'}
            text={settings.language === 'ja' ? 'カメラ' : 'Camera'}
            variant="secondary"
            size="medium"
            style={styles.secondaryButton}
          />
          
          <UniversalButton
            onPress={() => navigateTo('Gallery')}
            icon="📁"
            text={settings.language === 'ja' ? 'ギャラリー' : 'Gallery'}
            variant="secondary"
            size="medium"
            style={styles.secondaryButton}
          />
        </View>
      </View>

      <View style={styles.bottomActions}>
        <UniversalButton
          onPress={() => navigateTo('Settings')}
          icon="⚙️"
          text={settings.language === 'ja' ? '設定' : 'Settings'}
          variant="secondary"
          size="small"
          style={styles.bottomButton}
        />
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#2C3E50',
  },
  header: {
    alignItems: 'center',
    paddingVertical: 20,
    paddingHorizontal: 20,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#FFFFFF',
    marginBottom: 8,
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 16,
    color: '#BDC3C7',
    textAlign: 'center',
  },
  mainContent: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 40,
  },
  recordButtonContainer: {
    alignItems: 'center',
    marginBottom: 40,
  },
  recordButton: {
    width: 200,
    height: 200,
    borderRadius: 100,
    shadowColor: '#FF6B6B',
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.4,
    shadowRadius: 16,
    elevation: 12,
  },
  secondaryActions: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    width: '100%',
    paddingHorizontal: 20,
  },
  secondaryButton: {
    minWidth: 120,
  },
  bottomActions: {
    paddingHorizontal: 20,
    paddingBottom: 20,
    alignItems: 'center',
  },
  bottomButton: {
    minWidth: 100,
  },
});