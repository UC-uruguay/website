import React, { useState, useRef } from 'react';
import {
  SafeAreaView,
  StyleSheet,
  Text,
  View,
  Button,
  findNodeHandle,
} from 'react-native';
import CameraOverlay from './src/components/CameraOverlay';
import ScreenRecorder from './src/services/ScreenRecorder';
import FloatingWindow from './src/services/FloatingWindowService';
import { requireNativeComponent } from 'react-native';

const CameraView = requireNativeComponent('CameraView');

function App(): JSX.Element {
  const [isRecording, setIsRecording] = useState(false);
  const [showCamera, setShowCamera] = useState(false);
  const cameraViewRef = useRef(null);

  const handleStartRecording = async () => {
    try {
      const result = await ScreenRecorder.start();
      console.log(result);
      setIsRecording(true);
    } catch (error) {
      console.error(error);
    }
  };

  const handleStopRecording = async () => {
    try {
      const result = await ScreenRecorder.stop();
      console.log(result);
      setIsRecording(false);
    } catch (error) {
      console.error(error);
    }
  };

  const handleToggleCamera = () => {
    setShowCamera(!showCamera);
  };

  const handleStartFloatingWindow = () => {
    FloatingWindow.startFloatingWindow();
  };

  const handleStopFloatingWindow = () => {
    FloatingWindow.stopFloatingWindow();
  };

  const onCameraReady = () => {
    if (cameraViewRef.current) {
      const nodeHandle = findNodeHandle(cameraViewRef.current);
      if (nodeHandle) {
        ScreenRecorder.setCameraSurface(nodeHandle);
      }
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Game Recorder App</Text>
      </View>
      <View style={styles.controls}>
        <Button
          title={isRecording ? 'Stop Recording' : 'Start Recording'}
          onPress={isRecording ? handleStopRecording : handleStartRecording}
        />
        <Button
          title={showCamera ? 'Hide Camera' : 'Show Camera'}
          onPress={handleToggleCamera}
        />
        <Button
          title="Start Floating Window"
          onPress={handleStartFloatingWindow}
        />
        <Button
          title="Stop Floating Window"
          onPress={handleStopFloatingWindow}
        />
      </View>
      {showCamera && (
        <CameraView ref={cameraViewRef} style={styles.cameraView} onLayout={onCameraReady} />
      )}
      {showCamera && <CameraOverlay position="bottom-right" size="medium" />}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    padding: 20,
    backgroundColor: '#6200ee',
  },
  title: {
    color: 'white',
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  controls: {
    padding: 20,
    justifyContent: 'space-around',
    flexDirection: 'row',
    flexWrap: 'wrap',
  },
  cameraView: {
    position: 'absolute',
    width: 1, // These are dummy values, the actual size is controlled by the CameraOverlay
    height: 1,
    top: -1000,
    left: -1000,
  },
});

export default App;