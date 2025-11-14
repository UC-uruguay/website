import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  FlatList,
  SafeAreaView,
  StatusBar,
  TouchableOpacity,
  Image,
  Alert,
} from 'react-native';
import { UniversalButton } from '../components/UniversalButton';
import { useAppStore } from '../stores/appStore';
import { VideoFile } from '../types';

export const GalleryScreen: React.FC = () => {
  const { videos, settings, navigateTo, goBack, deleteVideo } = useAppStore();

  const formatDuration = (duration: number) => {
    const minutes = Math.floor(duration / 60);
    const seconds = Math.floor(duration % 60);
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
  };

  const formatFileSize = (size: number) => {
    if (size < 1024 * 1024) {
      return `${(size / 1024).toFixed(1)} KB`;
    }
    return `${(size / (1024 * 1024)).toFixed(1)} MB`;
  };

  const handleDeleteVideo = (video: VideoFile) => {
    Alert.alert(
      settings.language === 'ja' ? '動画を削除' : 'Delete Video',
      settings.language === 'ja' 
        ? `"${video.name}"を削除しますか？`
        : `Delete "${video.name}"?`,
      [
        {
          text: settings.language === 'ja' ? 'キャンセル' : 'Cancel',
          style: 'cancel',
        },
        {
          text: settings.language === 'ja' ? '削除' : 'Delete',
          style: 'destructive',
          onPress: () => deleteVideo(video.id),
        },
      ]
    );
  };

  const renderVideoItem = ({ item }: { item: VideoFile }) => (
    <TouchableOpacity style={styles.videoItem}>
      <View style={styles.thumbnail}>
        {item.thumbnail ? (
          <Image source={{ uri: item.thumbnail }} style={styles.thumbnailImage} />
        ) : (
          <View style={styles.placeholderThumbnail}>
            <Text style={styles.placeholderText}>🎬</Text>
          </View>
        )}
        <View style={styles.durationBadge}>
          <Text style={styles.durationText}>{formatDuration(item.duration)}</Text>
        </View>
      </View>
      
      <View style={styles.videoInfo}>
        <Text style={styles.videoName} numberOfLines={2}>
          {item.name}
        </Text>
        <Text style={styles.videoMeta}>
          {formatFileSize(item.size)} • {item.createdAt.toLocaleDateString()}
        </Text>
      </View>

      <View style={styles.videoActions}>
        <TouchableOpacity
          style={styles.actionButton}
          onPress={() => handleDeleteVideo(item)}
        >
          <Text style={styles.actionIcon}>🗑️</Text>
        </TouchableOpacity>
      </View>
    </TouchableOpacity>
  );

  const renderEmptyState = () => (
    <View style={styles.emptyState}>
      <Text style={styles.emptyIcon}>📱</Text>
      <Text style={styles.emptyTitle}>
        {settings.language === 'ja' ? '録画がありません' : 'No recordings yet'}
      </Text>
      <Text style={styles.emptySubtitle}>
        {settings.language === 'ja' 
          ? '最初の録画を開始しましょう'
          : 'Start your first recording'}
      </Text>
      <UniversalButton
        onPress={() => navigateTo('Home')}
        icon="🎬"
        text={settings.language === 'ja' ? '録画開始' : 'Start Recording'}
        variant="primary"
        size="medium"
        style={styles.emptyStateButton}
      />
    </View>
  );

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="light-content" backgroundColor="#2C3E50" />
      
      <View style={styles.header}>
        <UniversalButton
          onPress={goBack}
          icon="←"
          variant="secondary"
          size="small"
          style={styles.backButton}
        />
        <Text style={styles.title}>
          {settings.language === 'ja' ? 'ギャラリー' : 'Gallery'}
        </Text>
        <View style={styles.headerSpacer} />
      </View>

      {videos.length === 0 ? (
        renderEmptyState()
      ) : (
        <FlatList
          data={videos}
          renderItem={renderVideoItem}
          keyExtractor={(item) => item.id}
          contentContainerStyle={styles.videoList}
          showsVerticalScrollIndicator={false}
        />
      )}
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#2C3E50',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#34495E',
  },
  backButton: {
    width: 44,
    height: 44,
    minHeight: 44,
  },
  title: {
    flex: 1,
    fontSize: 20,
    fontWeight: 'bold',
    color: '#FFFFFF',
    textAlign: 'center',
  },
  headerSpacer: {
    width: 44,
  },
  videoList: {
    padding: 16,
  },
  videoItem: {
    flexDirection: 'row',
    backgroundColor: '#34495E',
    borderRadius: 12,
    padding: 12,
    marginBottom: 12,
    alignItems: 'center',
  },
  thumbnail: {
    width: 80,
    height: 60,
    borderRadius: 8,
    overflow: 'hidden',
    marginRight: 12,
    position: 'relative',
  },
  thumbnailImage: {
    width: '100%',
    height: '100%',
  },
  placeholderThumbnail: {
    width: '100%',
    height: '100%',
    backgroundColor: '#2C3E50',
    alignItems: 'center',
    justifyContent: 'center',
  },
  placeholderText: {
    fontSize: 24,
  },
  durationBadge: {
    position: 'absolute',
    bottom: 4,
    right: 4,
    backgroundColor: 'rgba(0, 0, 0, 0.8)',
    paddingHorizontal: 4,
    paddingVertical: 2,
    borderRadius: 4,
  },
  durationText: {
    color: '#FFFFFF',
    fontSize: 10,
    fontWeight: '600',
  },
  videoInfo: {
    flex: 1,
    marginRight: 12,
  },
  videoName: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: '600',
    marginBottom: 4,
  },
  videoMeta: {
    color: '#BDC3C7',
    fontSize: 12,
  },
  videoActions: {
    flexDirection: 'row',
  },
  actionButton: {
    width: 44,
    height: 44,
    alignItems: 'center',
    justifyContent: 'center',
    borderRadius: 22,
    backgroundColor: '#E74C3C',
    marginLeft: 8,
  },
  actionIcon: {
    fontSize: 18,
  },
  emptyState: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 40,
  },
  emptyIcon: {
    fontSize: 64,
    marginBottom: 16,
  },
  emptyTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#FFFFFF',
    marginBottom: 8,
    textAlign: 'center',
  },
  emptySubtitle: {
    fontSize: 16,
    color: '#BDC3C7',
    textAlign: 'center',
    marginBottom: 32,
  },
  emptyStateButton: {
    minWidth: 160,
  },
});