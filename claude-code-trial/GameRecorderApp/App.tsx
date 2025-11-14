import React, { useEffect } from 'react';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { GestureHandlerRootView } from 'react-native-gesture-handler';
import { HomeScreen } from './src/screens/HomeScreen';
import { GalleryScreen } from './src/screens/GalleryScreen';
import { SettingsScreen } from './src/screens/SettingsScreen';
import { useAppStore } from './src/stores/appStore';
import { VideoUtils } from './src/utils/videoUtils';

const App: React.FC = () => {
  const { navigation } = useAppStore();

  useEffect(() => {
    // Initialize app directories
    const initializeApp = async () => {
      try {
        const videosDir = VideoUtils.getAppVideosDirectory();
        await VideoUtils.ensureDirectoryExists(videosDir);
        console.log('App initialized successfully');
      } catch (error) {
        console.error('App initialization error:', error);
      }
    };

    initializeApp();
  }, []);

  const renderCurrentScreen = () => {
    switch (navigation.currentScreen) {
      case 'Home':
        return <HomeScreen />;
      case 'Gallery':
        return <GalleryScreen />;
      case 'Settings':
        return <SettingsScreen />;
      default:
        return <HomeScreen />;
    }
  };

  return (
    <SafeAreaProvider>
      <GestureHandlerRootView style={{ flex: 1 }}>
        {renderCurrentScreen()}
      </GestureHandlerRootView>
    </SafeAreaProvider>
  );
};

export default App;
