import { NativeModules } from 'react-native';

const { FloatingWindowModule } = NativeModules;

interface FloatingWindowInterface {
  startFloatingWindow(): void;
  stopFloatingWindow(): void;
}

export default FloatingWindowModule as FloatingWindowInterface;
