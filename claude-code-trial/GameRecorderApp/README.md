# 🎬 Game Recorder App

ゲーム画面と表情を同時に録画できるスマートフォンアプリ

A smartphone app that can simultaneously record game screens and facial expressions.

## ✨ Features / 機能

### 🎥 Core Features / 主要機能
- **Screen Recording** / **画面録画**: Record device screen with high quality
- **Face Camera** / **表情カメラ**: Overlay face camera with Picture-in-Picture
- **Background Recording** / **バックグラウンド録画**: Continue recording when app is in background
- **Universal Design** / **ユニバーサルデザイン**: Icon-based UI with large touch targets

### 🎨 UI/UX Features / UI/UX機能
- **Minimal Text Interface** / **最小限のテキスト**: Icon-driven interface for universal accessibility
- **Bilingual Support** / **多言語対応**: Japanese and English support
- **Draggable Camera Preview** / **ドラッグ可能プレビュー**: Freely position the face camera overlay
- **One-Tap Recording** / **ワンタップ録画**: Large, accessible recording button

### ⚙️ Settings / 設定
- **Video Quality** / **動画品質**: HD (720p), FHD (1080p), 4K recording options
- **Frame Rate** / **フレームレート**: 30fps / 60fps options
- **Audio Recording** / **音声録音**: Toggle microphone recording
- **Camera Overlay** / **カメラオーバーレイ**: Enable/disable face camera overlay

## 🚀 Getting Started / 始め方

> **Note**: Make sure you have completed the [Set Up Your Environment](https://reactnative.dev/docs/set-up-your-environment) guide before proceeding.

## Step 1: Start Metro

First, you will need to run **Metro**, the JavaScript build tool for React Native.

To start the Metro dev server, run the following command from the root of your React Native project:

```sh
# Using npm
npm start

# OR using Yarn
yarn start
```

## Step 2: Build and run your app

With Metro running, open a new terminal window/pane from the root of your React Native project, and use one of the following commands to build and run your Android or iOS app:

### Android

```sh
# Using npm
npm run android

# OR using Yarn
yarn android
```

### iOS

For iOS, remember to install CocoaPods dependencies (this only needs to be run on first clone or after updating native deps).

The first time you create a new project, run the Ruby bundler to install CocoaPods itself:

```sh
bundle install
```

Then, and every time you update your native dependencies, run:

```sh
bundle exec pod install
```

For more information, please visit [CocoaPods Getting Started guide](https://guides.cocoapods.org/using/getting-started.html).

```sh
# Using npm
npm run ios

# OR using Yarn
yarn ios
```

If everything is set up correctly, you should see your new app running in the Android Emulator, iOS Simulator, or your connected device.

This is one way to run your app — you can also build it directly from Android Studio or Xcode.

## Step 3: Modify your app

Now that you have successfully run the app, let's make changes!

Open `App.tsx` in your text editor of choice and make some changes. When you save, your app will automatically update and reflect these changes — this is powered by [Fast Refresh](https://reactnative.dev/docs/fast-refresh).

When you want to forcefully reload, for example to reset the state of your app, you can perform a full reload:

- **Android**: Press the <kbd>R</kbd> key twice or select **"Reload"** from the **Dev Menu**, accessed via <kbd>Ctrl</kbd> + <kbd>M</kbd> (Windows/Linux) or <kbd>Cmd ⌘</kbd> + <kbd>M</kbd> (macOS).
- **iOS**: Press <kbd>R</kbd> in iOS Simulator.

## Congratulations! :tada:

You've successfully run and modified your React Native App. :partying_face:

### Now what?

- If you want to add this new React Native code to an existing application, check out the [Integration guide](https://reactnative.dev/docs/integration-with-existing-apps).
- If you're curious to learn more about React Native, check out the [docs](https://reactnative.dev/docs/getting-started).

# Troubleshooting

If you're having issues getting the above steps to work, see the [Troubleshooting](https://reactnative.dev/docs/troubleshooting) page.

# Learn More

To learn more about React Native, take a look at the following resources:

- [React Native Website](https://reactnative.dev) - learn more about React Native.
- [Getting Started](https://reactnative.dev/docs/environment-setup) - an **overview** of React Native and how setup your environment.
- [Learn the Basics](https://reactnative.dev/docs/getting-started) - a **guided tour** of the React Native **basics**.
- [Blog](https://reactnative.dev/blog) - read the latest official React Native **Blog** posts.
- [`@facebook/react-native`](https://github.com/facebook/react-native) - the Open Source; GitHub **repository** for React Native.
