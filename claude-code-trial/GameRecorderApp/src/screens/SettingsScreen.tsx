import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  SafeAreaView,
  StatusBar,
  ScrollView,
  TouchableOpacity,
  Switch,
} from 'react-native';
import { UniversalButton } from '../components/UniversalButton';
import { useAppStore } from '../stores/appStore';

export const SettingsScreen: React.FC = () => {
  const { settings, updateSettings, goBack } = useAppStore();

  const SettingItem: React.FC<{
    icon: string;
    title: string;
    subtitle?: string;
    children: React.ReactNode;
  }> = ({ icon, title, subtitle, children }) => (
    <View style={styles.settingItem}>
      <View style={styles.settingInfo}>
        <Text style={styles.settingIcon}>{icon}</Text>
        <View style={styles.settingText}>
          <Text style={styles.settingTitle}>{title}</Text>
          {subtitle && <Text style={styles.settingSubtitle}>{subtitle}</Text>}
        </View>
      </View>
      <View style={styles.settingControl}>{children}</View>
    </View>
  );

  const OptionButton: React.FC<{
    label: string;
    isSelected: boolean;
    onPress: () => void;
  }> = ({ label, isSelected, onPress }) => (
    <TouchableOpacity
      style={[styles.optionButton, isSelected && styles.selectedOption]}
      onPress={onPress}
    >
      <Text style={[styles.optionText, isSelected && styles.selectedOptionText]}>
        {label}
      </Text>
    </TouchableOpacity>
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
          {settings.language === 'ja' ? '設定' : 'Settings'}
        </Text>
        <View style={styles.headerSpacer} />
      </View>

      <ScrollView style={styles.content} showsVerticalScrollIndicator={false}>
        {/* Language Setting */}
        <SettingItem
          icon="🌍"
          title={settings.language === 'ja' ? '言語' : 'Language'}
          subtitle={settings.language === 'ja' ? '表示言語を選択' : 'Select display language'}
        >
          <View style={styles.optionRow}>
            <OptionButton
              label="日本語"
              isSelected={settings.language === 'ja'}
              onPress={() => updateSettings({ language: 'ja' })}
            />
            <OptionButton
              label="English"
              isSelected={settings.language === 'en'}
              onPress={() => updateSettings({ language: 'en' })}
            />
          </View>
        </SettingItem>

        {/* Video Quality Setting */}
        <SettingItem
          icon="🎥"
          title={settings.language === 'ja' ? '動画品質' : 'Video Quality'}
          subtitle={settings.language === 'ja' ? '録画品質を選択' : 'Select recording quality'}
        >
          <View style={styles.optionColumn}>
            <OptionButton
              label="HD (720p)"
              isSelected={settings.videoQuality === 'HD'}
              onPress={() => updateSettings({ videoQuality: 'HD' })}
            />
            <OptionButton
              label="FHD (1080p)"
              isSelected={settings.videoQuality === 'FHD'}
              onPress={() => updateSettings({ videoQuality: 'FHD' })}
            />
            <OptionButton
              label="4K"
              isSelected={settings.videoQuality === '4K'}
              onPress={() => updateSettings({ videoQuality: '4K' })}
            />
          </View>
        </SettingItem>

        {/* Frame Rate Setting */}
        <SettingItem
          icon="⚡"
          title={settings.language === 'ja' ? 'フレームレート' : 'Frame Rate'}
          subtitle={settings.language === 'ja' ? '録画フレームレート' : 'Recording frame rate'}
        >
          <View style={styles.optionRow}>
            <OptionButton
              label="30 FPS"
              isSelected={settings.frameRate === 30}
              onPress={() => updateSettings({ frameRate: 30 })}
            />
            <OptionButton
              label="60 FPS"
              isSelected={settings.frameRate === 60}
              onPress={() => updateSettings({ frameRate: 60 })}
            />
          </View>
        </SettingItem>

        {/* Audio Setting */}
        <SettingItem
          icon="🎵"
          title={settings.language === 'ja' ? '音声録音' : 'Audio Recording'}
          subtitle={settings.language === 'ja' ? 'マイク音声を録音' : 'Record microphone audio'}
        >
          <Switch
            value={settings.audioEnabled}
            onValueChange={(value) => updateSettings({ audioEnabled: value })}
            trackColor={{ false: '#767577', true: '#4ECDC4' }}
            thumbColor={settings.audioEnabled ? '#FFFFFF' : '#f4f3f4'}
          />
        </SettingItem>

        {/* Camera Overlay Setting */}
        <SettingItem
          icon="📹"
          title={settings.language === 'ja' ? 'カメラオーバーレイ' : 'Camera Overlay'}
          subtitle={settings.language === 'ja' ? '表情カメラを表示' : 'Show face camera overlay'}
        >
          <Switch
            value={settings.cameraOverlayEnabled}
            onValueChange={(value) => updateSettings({ cameraOverlayEnabled: value })}
            trackColor={{ false: '#767577', true: '#4ECDC4' }}
            thumbColor={settings.cameraOverlayEnabled ? '#FFFFFF' : '#f4f3f4'}
          />
        </SettingItem>

        {/* Theme Setting */}
        <SettingItem
          icon="🎨"
          title={settings.language === 'ja' ? 'テーマ' : 'Theme'}
          subtitle={settings.language === 'ja' ? 'アプリの外観' : 'App appearance'}
        >
          <View style={styles.optionRow}>
            <OptionButton
              label={settings.language === 'ja' ? 'ライト' : 'Light'}
              isSelected={settings.theme === 'light'}
              onPress={() => updateSettings({ theme: 'light' })}
            />
            <OptionButton
              label={settings.language === 'ja' ? 'ダーク' : 'Dark'}
              isSelected={settings.theme === 'dark'}
              onPress={() => updateSettings({ theme: 'dark' })}
            />
          </View>
        </SettingItem>

        <View style={styles.footer}>
          <Text style={styles.footerText}>
            {settings.language === 'ja' 
              ? 'ゲーム録画アプリ v1.0.0'
              : 'Game Recorder App v1.0.0'}
          </Text>
        </View>
      </ScrollView>
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
  content: {
    flex: 1,
    padding: 16,
  },
  settingItem: {
    backgroundColor: '#34495E',
    borderRadius: 12,
    padding: 16,
    marginBottom: 12,
  },
  settingInfo: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 12,
  },
  settingIcon: {
    fontSize: 24,
    marginRight: 12,
  },
  settingText: {
    flex: 1,
  },
  settingTitle: {
    fontSize: 16,
    fontWeight: '600',
    color: '#FFFFFF',
    marginBottom: 2,
  },
  settingSubtitle: {
    fontSize: 12,
    color: '#BDC3C7',
  },
  settingControl: {
    alignItems: 'flex-end',
  },
  optionRow: {
    flexDirection: 'row',
    gap: 8,
  },
  optionColumn: {
    gap: 8,
  },
  optionButton: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 20,
    backgroundColor: '#2C3E50',
    borderWidth: 1,
    borderColor: '#4ECDC4',
    minWidth: 80,
    alignItems: 'center',
  },
  selectedOption: {
    backgroundColor: '#4ECDC4',
  },
  optionText: {
    color: '#4ECDC4',
    fontSize: 14,
    fontWeight: '600',
  },
  selectedOptionText: {
    color: '#FFFFFF',
  },
  footer: {
    alignItems: 'center',
    paddingVertical: 32,
  },
  footerText: {
    color: '#7F8C8D',
    fontSize: 12,
  },
});