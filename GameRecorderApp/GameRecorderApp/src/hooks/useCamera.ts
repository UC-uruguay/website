import { useEffect, useState } from 'react';
import { Camera, CameraPermissionStatus } from 'react-native-vision-camera';

export const useCamera = () => {
  const [hasPermission, setHasPermission] = useState(false);
  const [cameraPermission, setCameraPermission] = useState<CameraPermissionStatus>();

  useEffect(() => {
    const getPermission = async () => {
      const permission = await Camera.getCameraPermissionStatus();
      setCameraPermission(permission);
      if (permission === 'authorized') {
        setHasPermission(true);
      } else if (permission === 'not-determined') {
        const newPermission = await Camera.requestCameraPermission();
        setCameraPermission(newPermission);
        if (newPermission === 'authorized') {
          setHasPermission(true);
        }
      }
    };
    getPermission();
  }, []);

  return { hasPermission, cameraPermission };
};
