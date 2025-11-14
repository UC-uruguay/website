import React from 'react';
import { StyleSheet, View } from 'react-native';
import { Camera, useCameraDevices } from 'react-native-vision-camera';
import { useCamera } from '../hooks/useCamera';

interface CameraOverlayProps {
  position: 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right';
  size: 'small' | 'medium' | 'large';
}

const CameraOverlay: React.FC<CameraOverlayProps> = ({ position, size }) => {
  const { hasPermission } = useCamera();
  const devices = useCameraDevices();
  const device = devices.front;

  if (!hasPermission || !device) {
    return null;
  }

  const getSize = () => {
    switch (size) {
      case 'small':
        return styles.small;
      case 'medium':
        return styles.medium;
      case 'large':
        return styles.large;
    }
  };

  const getPosition = () => {
    switch (position) {
      case 'top-left':
        return styles.topLeft;
      case 'top-right':
        return styles.topRight;
      case 'bottom-left':
        return styles.bottomLeft;
      case 'bottom-right':
        return styles.bottomRight;
    }
  };

  return (
    <View style={[styles.container, getPosition()]}>
      <Camera
        style={[styles.camera, getSize()]}
        device={device}
        isActive={true}
        photo={true}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    position: 'absolute',
    zIndex: 1000,
  },
  camera: {
    borderRadius: 10,
  },
  small: {
    width: 80,
    height: 120,
  },
  medium: {
    width: 120,
    height: 180,
  },
  large: {
    width: 160,
    height: 240,
  },
  topLeft: {
    top: 20,
    left: 20,
  },
  topRight: {
    top: 20,
    right: 20,
  },
  bottomLeft: {
    bottom: 20,
    left: 20,
  },
  bottomRight: {
    bottom: 20,
    right: 20,
  },
});

export default CameraOverlay;
