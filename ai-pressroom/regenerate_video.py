#!/usr/bin/env python3
"""Regenerate video with updated avatar images."""
import pickle
from pathlib import Path
import yaml

from src.video.video_generator import VideoGenerator
from src.shared.logger import get_logger

logger = get_logger(__name__)

# Episode to regenerate
EPISODE_ID = "episode_20251105"
WORK_DIR = Path(f"data/work/{EPISODE_ID}")

def main():
    """Regenerate video for the episode."""
    logger.info(f"Regenerating video for {EPISODE_ID}")

    # Load character configurations
    config_dir = Path("configs")
    character_path = config_dir / "characters.yaml"

    with open(character_path, 'r', encoding='utf-8') as f:
        characters = yaml.safe_load(f)

    logger.info(f"Loaded {len(characters)} character configurations")

    # Load debate script from checkpoint
    checkpoint_path = WORK_DIR / "checkpoint_script.pkl"
    if not checkpoint_path.exists():
        logger.error(f"Checkpoint not found: {checkpoint_path}")
        return

    with open(checkpoint_path, 'rb') as f:
        debate_script = pickle.load(f)
    logger.info(f"Loaded debate script with {len(debate_script.lines)} lines")

    # Initialize video generator
    video_gen = VideoGenerator(WORK_DIR / "video", characters)

    # Set paths
    audio_path = WORK_DIR / f"{EPISODE_ID}.mp3"
    output_path = WORK_DIR / f"{EPISODE_ID}_new.mp4"
    audio_stems_dir = WORK_DIR / "audio_stems"

    # Generate video
    logger.info("Generating video with updated avatars...")
    video_path = video_gen.generate_video(
        debate_script,
        audio_path,
        output_path,
        audio_stems_dir
    )

    logger.info(f"Video regenerated successfully: {video_path}")
    print(f"\n✅ Video regenerated: {video_path}")

if __name__ == "__main__":
    main()
