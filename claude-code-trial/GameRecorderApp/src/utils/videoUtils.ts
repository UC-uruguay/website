import RNFS from 'react-native-fs';
import { CameraRoll } from '@react-native-camera-roll/camera-roll';
import { VideoFile } from '../types';

export class VideoUtils {
  static async saveVideoToCameraRoll(videoPath: string): Promise<void> {
    try {
      await CameraRoll.save(videoPath, { type: 'video' });
      console.log('Video saved to camera roll:', videoPath);
    } catch (error) {
      console.error('Error saving video to camera roll:', error);
      throw error;
    }
  }

  static async deleteVideo(videoPath: string): Promise<void> {
    try {
      const exists = await RNFS.exists(videoPath);
      if (exists) {
        await RNFS.unlink(videoPath);
        console.log('Video deleted:', videoPath);
      }
    } catch (error) {
      console.error('Error deleting video:', error);
      throw error;
    }
  }

  static async getVideoInfo(videoPath: string): Promise<{
    size: number;
    duration: number;
  }> {
    try {
      const stat = await RNFS.stat(videoPath);
      // Note: Getting actual video duration would require a native module
      // For now, we'll use file modification time as a proxy
      const duration = 60; // Mock duration in seconds
      
      return {
        size: stat.size,
        duration: duration,
      };
    } catch (error) {
      console.error('Error getting video info:', error);
      return { size: 0, duration: 0 };
    }
  }

  static async generateThumbnail(videoPath: string): Promise<string | null> {
    try {
      // This would require a native module like react-native-video-processing
      // For now, return null to use placeholder
      console.log('Generating thumbnail for:', videoPath);
      return null;
    } catch (error) {
      console.error('Error generating thumbnail:', error);
      return null;
    }
  }

  static async createVideoFile(
    screenVideoPath: string,
    cameraVideoPath?: string
  ): Promise<VideoFile> {
    try {
      const timestamp = Date.now();
      const fileName = `GameRecording_${new Date().toISOString().replace(/[:.]/g, '-')}.mp4`;
      
      let finalVideoPath = screenVideoPath;
      
      // If we have both screen and camera videos, we would merge them here
      if (cameraVideoPath) {
        finalVideoPath = await this.mergeVideos(screenVideoPath, cameraVideoPath);
      }

      const { size, duration } = await this.getVideoInfo(finalVideoPath);
      const thumbnail = await this.generateThumbnail(finalVideoPath);

      const videoFile: VideoFile = {
        id: timestamp.toString(),
        path: finalVideoPath,
        thumbnail: thumbnail || '',
        duration: duration,
        createdAt: new Date(),
        size: size,
        name: fileName,
      };

      // Save to camera roll
      await this.saveVideoToCameraRoll(finalVideoPath);

      return videoFile;
    } catch (error) {
      console.error('Error creating video file:', error);
      throw error;
    }
  }

  private static async mergeVideos(
    screenVideoPath: string,
    cameraVideoPath: string
  ): Promise<string> {
    try {
      // This would require FFmpeg or similar video processing library
      // For now, just return the screen video path
      console.log('Merging videos:', { screenVideoPath, cameraVideoPath });
      
      const outputPath = `${RNFS.DocumentDirectoryPath}/merged_${Date.now()}.mp4`;
      
      // Mock merge process - in real implementation:
      // 1. Load both videos
      // 2. Resize camera video to overlay size
      // 3. Position camera video as overlay
      // 4. Merge/composite the videos
      // 5. Export to output path
      
      // For now, just copy the screen video
      await RNFS.copyFile(screenVideoPath, outputPath);
      
      return outputPath;
    } catch (error) {
      console.error('Error merging videos:', error);
      throw error;
    }
  }

  static formatDuration(seconds: number): string {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
  }

  static formatFileSize(bytes: number): string {
    if (bytes === 0) return '0 Bytes';
    
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  }

  static async ensureDirectoryExists(dirPath: string): Promise<void> {
    try {
      const exists = await RNFS.exists(dirPath);
      if (!exists) {
        await RNFS.mkdir(dirPath);
        console.log('Directory created:', dirPath);
      }
    } catch (error) {
      console.error('Error creating directory:', error);
      throw error;
    }
  }

  static getAppVideosDirectory(): string {
    return `${RNFS.DocumentDirectoryPath}/GameRecorder`;
  }
}