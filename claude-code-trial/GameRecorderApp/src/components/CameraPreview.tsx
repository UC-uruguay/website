import React, { useRef } from 'react';
import { View, StyleSheet, Dimensions, PanResponder } from 'react-native';
import { Camera, useCameraDevice } from 'react-native-vision-camera';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  runOnJS,
} from 'react-native-reanimated';
import { useAppStore } from '../stores/appStore';

const { width: screenWidth, height: screenHeight } = Dimensions.get('window');

export const CameraPreview: React.FC = () => {
  const { camera, updatePreviewPosition } = useAppStore();
  const device = useCameraDevice(camera.isFrontCamera ? 'front' : 'back');

  const translateX = useSharedValue(camera.previewPosition.x);
  const translateY = useSharedValue(camera.previewPosition.y);

  const panResponder = useRef(
    PanResponder.create({
      onMoveShouldSetPanResponder: () => true,
      onPanResponderGrant: () => {
        // Add haptic feedback here if needed
      },
      onPanResponderMove: (_, gestureState) => {
        const newX = Math.max(
          0,
          Math.min(
            screenWidth - camera.previewSize.width,
            camera.previewPosition.x + gestureState.dx
          )
        );
        const newY = Math.max(
          100, // Keep below status bar and timer
          Math.min(
            screenHeight - camera.previewSize.height - 100, // Keep above controls
            camera.previewPosition.y + gestureState.dy
          )
        );

        translateX.value = newX;
        translateY.value = newY;
      },
      onPanResponderRelease: () => {
        runOnJS(updatePreviewPosition)({
          x: translateX.value,
          y: translateY.value,
        });
      },
    })
  ).current;

  const animatedStyle = useAnimatedStyle(() => ({
    transform: [
      { translateX: translateX.value },
      { translateY: translateY.value },
    ],
  }));

  if (!camera.isActive || !camera.showPreview || !device) {
    return null;
  }

  return (
    <Animated.View
      style={[styles.container, animatedStyle]}
      {...panResponder.panHandlers}
    >
      <View style={styles.preview}>
        <Camera
          style={StyleSheet.absoluteFillObject}
          device={device}
          isActive={true}
          preview={true}
        />
        <View style={styles.border} />
        <View style={styles.dragIndicator}>
          <View style={styles.dragHandle} />
        </View>
      </View>
    </Animated.View>
  );
};

const styles = StyleSheet.create({
  container: {
    position: 'absolute',
    zIndex: 999,
  },
  preview: {
    width: 120,
    height: 160,
    borderRadius: 12,
    overflow: 'hidden',
    backgroundColor: '#000',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 8,
  },
  border: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    borderWidth: 2,
    borderColor: '#FF6B6B',
    borderRadius: 12,
    pointerEvents: 'none',
  },
  dragIndicator: {
    position: 'absolute',
    top: 4,
    left: 4,
    right: 4,
    height: 16,
    alignItems: 'center',
    justifyContent: 'center',
  },
  dragHandle: {
    width: 30,
    height: 4,
    borderRadius: 2,
    backgroundColor: 'rgba(255, 255, 255, 0.8)',
  },
});