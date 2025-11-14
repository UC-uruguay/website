#!/usr/bin/env python3
"""Test script to generate avatar images."""
from pathlib import Path

from src.video.avatar_generator import AvatarGenerator

# Character configurations
CHARACTERS = {
    "chatgpt": {
        "ai_name": "ChatGPT",
        "persona_name": "GPT Professor",
        "company": "OpenAI"
    },
    "gemini": {
        "ai_name": "Gemini",
        "persona_name": "Gemini Explorer",
        "company": "Google"
    },
    "claude": {
        "ai_name": "Claude",
        "persona_name": "Claude Thinker",
        "company": "Anthropic"
    }
}


def main():
    """Generate test avatars."""
    # Create output directory
    output_dir = Path("data/test_avatars")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Initialize generator
    generator = AvatarGenerator(output_dir)

    # Generate all avatars
    print("Generating personified avatars with logo-based heads...")
    avatars = generator.generate_all_avatars(CHARACTERS)

    print("\n=== Avatar Generation Complete ===")
    for speaker, path in avatars.items():
        print(f"{speaker}: {path}")

    print(f"\nAll avatars saved to: {output_dir}")
    print("Please check the images to verify the design.")


if __name__ == "__main__":
    main()
