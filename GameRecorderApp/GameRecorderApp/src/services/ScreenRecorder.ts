import { NativeModules } from 'react-native';

const { ScreenRecorderModule } = NativeModules;

interface ScreenRecorderInterface {
  start(): Promise<string>;
  stop(): Promise<string>;
}

export default ScreenRecorderModule as ScreenRecorderInterface;
