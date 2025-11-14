#!/usr/bin/env python3
"""
Generate a test video in Japanese using pre-made avatar images.

This script creates a debate video with Japanese dialogue using the
existing avatar images in data/test_avatars/.
"""
import shutil
from pathlib import Path
from datetime import datetime
import yaml

from src.agents.debate_orchestrator import DebateOrchestrator
from src.nlp.summarize import DebateTopic
from src.tts.gcloud_tts import GoogleCloudTTSProvider
from src.video.video_generator import VideoGenerator
from src.audio.mix import AudioMixer
from src.shared.settings import get_settings


def main():
    """Generate a Japanese debate video."""
    print("=" * 60)
    print("日本語討論ビデオ生成")
    print("=" * 60)
    print()

    # Setup paths
    work_dir = Path("data/work/test_video_ja")
    work_dir.mkdir(parents=True, exist_ok=True)

    avatar_source_dir = Path("data/test_avatars")

    audio_stems_dir = work_dir / "audio_stems"
    audio_stems_dir.mkdir(parents=True, exist_ok=True)

    video_dir = work_dir / "video"
    video_dir.mkdir(parents=True, exist_ok=True)

    # Avatar directory for VideoGenerator (must match VideoGenerator's expected path)
    avatar_dest_dir = video_dir / "avatars"
    avatar_dest_dir.mkdir(parents=True, exist_ok=True)

    # Copy existing avatar images to work directory
    print("既存のアバター画像をコピー中...")
    for avatar_file in avatar_source_dir.glob("avatar_*.png"):
        dest_file = avatar_dest_dir / avatar_file.name
        if not dest_file.exists():
            shutil.copy2(avatar_file, dest_file)
            print(f"  コピー: {avatar_file.name}")
    print()

    # Load character configurations
    print("キャラクター設定を読み込み中...")
    config_path = Path("configs/characters.yaml")
    with open(config_path, 'r', encoding='utf-8') as f:
        characters = yaml.safe_load(f)
    print(f"  {len(characters)}人のキャラクターを読み込みました")
    print()

    # Create debate topic
    topic = DebateTopic(
        title="AIは創造性を持てるか？",
        summary=(
            "AI技術の進歩により、音楽、絵画、文章など様々な創作活動にAIが使われるようになった。"
            "しかし、AIが生成するコンテンツは本当の意味で「創造的」と言えるのだろうか？"
            "人間とAIの創造性の違いについて議論する。"
        ),
        key_points=[
            "AIは既存のデータから学習し、新しい組み合わせを生み出すことができる",
            "しかし、AIには感情や経験がないため、真の意味での創造性には疑問がある",
            "人間の創造性とは何か、AIの創造性とどう違うのか"
        ],
        source_articles=["テスト記事"]
    )

    print(f"トピック: {topic.title}")
    print(f"概要: {topic.summary}")
    print()

    # Generate debate script
    print("討論スクリプトを生成中...")
    orchestrator = DebateOrchestrator(date=datetime.now())
    script = orchestrator.generate_script(topic, target_duration_min=2)

    print(f"  {len(script.lines)}行のスクリプトを生成しました")
    print(f"  推定時間: {script.total_duration_sec:.1f}秒")
    print()

    # Display script
    print("=" * 60)
    print("討論スクリプト")
    print("=" * 60)
    for i, line in enumerate(script.lines, 1):
        char = characters.get(line.speaker, {})
        persona = char.get("persona_name", line.speaker)
        print(f"{i:2}. [{persona}]")
        print(f"    {line.text}")
        print()

    # Generate audio using Google Cloud TTS
    print("=" * 60)
    print("音声を生成中（Google Cloud TTS使用）...")

    # Load settings to get voice configurations
    settings = get_settings()

    # Voice configurations for each speaker
    voice_configs = {
        "chatgpt": {
            "voice_name": "ja-JP-Wavenet-C",
            "speaking_rate": 1.28
        },
        "gemini": {
            "voice_name": "ja-JP-Wavenet-D",
            "speaking_rate": 1.23
        },
        "claude": {
            "voice_name": "ja-JP-Wavenet-B",
            "speaking_rate": 1.25
        }
    }

    audio_files = []
    for i, line in enumerate(script.lines):
        output_path = audio_stems_dir / f"{i:03d}_{line.speaker}.wav"

        # Get voice config for this speaker
        voice_config = voice_configs.get(line.speaker, voice_configs["chatgpt"])

        # Create TTS provider for this speaker
        tts = GoogleCloudTTSProvider(
            voice_name=voice_config["voice_name"],
            language_code="ja-JP",
            speaking_rate=voice_config["speaking_rate"]
        )

        # Synthesize audio
        tts.synthesize(
            text=line.text,
            speaker=line.speaker,
            output_path=output_path
        )
        audio_files.append(output_path)
        print(f"  生成: {output_path.name}")
    print()

    # Mix audio
    print("音声をミキシング中...")
    mixer = AudioMixer()
    mixed_audio_path = work_dir / "mixed_audio.mp3"

    mixer.mix_podcast(
        voice_files=audio_files,
        output_path=mixed_audio_path,
        bgm_path=None,  # No background music for test
        crossfade_ms=0  # No crossfade for clearer speaker separation
    )
    print(f"  ミックス完了: {mixed_audio_path}")
    print()

    # Generate video
    print("ビデオを生成中...")
    video_gen = VideoGenerator(video_dir, characters)
    output_video = work_dir / "debate_video_ja.mp4"

    video_gen.generate_video(
        script=script,
        audio_path=mixed_audio_path,
        output_path=output_video,
        audio_stems_dir=audio_stems_dir
    )

    print()
    print("=" * 60)
    print("✓ ビデオ生成完了！")
    print("=" * 60)
    print(f"出力ファイル: {output_video}")
    print(f"サイズ: {output_video.stat().st_size / 1024 / 1024:.2f} MB")
    print()


if __name__ == "__main__":
    main()
