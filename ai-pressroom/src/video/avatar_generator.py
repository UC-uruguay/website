"""
Generate avatar images for each AI speaker.

Creates simple, clean avatar images with speaker name and themed colors.
"""
from pathlib import Path
from typing import Dict, Any, Optional

from PIL import Image, ImageDraw, ImageFont

from ..shared.logger import get_logger

logger = get_logger(__name__)


class AvatarGenerator:
    """Generate avatar images for debate speakers."""

    # Color schemes for each AI
    COLORS = {
        "chatgpt": {
            "background": "#10A37F",  # OpenAI teal
            "accent": "#1A7F64",
            "text": "#FFFFFF",
        },
        "gemini": {
            "background": "#4285F4",  # Google blue
            "accent": "#1967D2",
            "text": "#FFFFFF",
        },
        "claude": {
            "background": "#D97757",  # Anthropic orange
            "accent": "#CC5500",
            "text": "#FFFFFF",
        },
    }

    DEFAULT_SIZE = (1920, 1080)

    def __init__(self, output_dir: Path):
        """
        Initialize avatar generator.

        Args:
            output_dir: Directory to save generated images
        """
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_avatar(
        self,
        speaker: str,
        character: Dict[str, Any],
        size: tuple[int, int] = DEFAULT_SIZE
    ) -> Path:
        """
        Generate personified avatar image for a speaker.

        Creates logo-based humanoid characters without text labels.

        Args:
            speaker: Speaker name (chatgpt, gemini, claude)
            character: Character configuration
            size: Image size (width, height)

        Returns:
            Path to generated image
        """
        output_path = self.output_dir / f"avatar_{speaker}.png"

        # Always regenerate to ensure latest design
        logger.info(f"Generating personified avatar for {speaker}...")

        # Get colors
        colors = self.COLORS.get(speaker, self.COLORS["chatgpt"])

        # Create image with gradient background
        img = Image.new("RGB", size, colors["background"])
        draw = ImageDraw.Draw(img)

        # Draw gradient background
        for y in range(size[1]):
            alpha = y / size[1]
            # Blend from background to accent
            draw.line(
                [(0, y), (size[0], y)],
                fill=self._blend_color(
                    colors["background"],
                    colors["accent"],
                    alpha * 0.3
                )
            )

        # Draw personified character based on speaker (no text)
        if speaker == "chatgpt":
            self._draw_chatgpt_character(draw, size, colors)
        elif speaker == "gemini":
            self._draw_gemini_character(draw, size, colors)
        elif speaker == "claude":
            self._draw_claude_character(draw, size, colors)

        # Save image
        img.save(output_path, "PNG", quality=95)
        logger.info(f"Saved avatar to {output_path}")

        return output_path

    def generate_all_avatars(
        self,
        characters: Dict[str, Dict[str, Any]]
    ) -> Dict[str, Path]:
        """
        Generate avatars for all speakers.

        Args:
            characters: Dictionary of character configurations

        Returns:
            Dictionary mapping speaker name to avatar path
        """
        avatars = {}

        for speaker, character in characters.items():
            avatar_path = self.generate_avatar(speaker, character)
            avatars[speaker] = avatar_path

        logger.info(f"Generated {len(avatars)} avatar images")
        return avatars

    def _blend_color(
        self,
        color1: str,
        color2: str,
        alpha: float
    ) -> str:
        """
        Blend two hex colors.

        Args:
            color1: First color (hex)
            color2: Second color (hex)
            alpha: Blend factor (0-1)

        Returns:
            Blended color (hex)
        """
        # Convert hex to RGB
        c1 = tuple(int(color1[i:i+2], 16) for i in (1, 3, 5))
        c2 = tuple(int(color2[i:i+2], 16) for i in (1, 3, 5))

        # Blend
        blended = tuple(
            int(c1[i] * (1 - alpha) + c2[i] * alpha)
            for i in range(3)
        )

        # Convert back to hex
        return f"#{blended[0]:02x}{blended[1]:02x}{blended[2]:02x}"

    def _draw_3d_rounded_rect(
        self,
        draw: ImageDraw.ImageDraw,
        bbox: list,
        radius: int,
        fill_color: str,
        outline_color: str,
        width: int = 6
    ) -> None:
        """Draw a 3D-looking rounded rectangle with shadows and highlights."""
        x1, y1, x2, y2 = bbox

        # Draw shadow (offset down and right)
        shadow_offset = 8
        draw.rounded_rectangle(
            [x1 + shadow_offset, y1 + shadow_offset,
             x2 + shadow_offset, y2 + shadow_offset],
            radius=radius,
            fill="#00000030"
        )

        # Draw main shape with gradient effect
        # Create multiple layers for 3D effect
        num_layers = 5
        for i in range(num_layers):
            layer_offset = i * 2
            alpha = i / num_layers
            layer_color = self._blend_color("#FFFFFF", fill_color, alpha * 0.3)

            draw.rounded_rectangle(
                [x1 + layer_offset, y1 + layer_offset,
                 x2 - layer_offset, y2 - layer_offset],
                radius=radius,
                fill=layer_color,
                outline=outline_color if i == 0 else None,
                width=width if i == 0 else 0
            )

        # Add highlight on top-left
        highlight_size = min(60, (x2 - x1) // 3)
        draw.ellipse(
            [x1 + 20, y1 + 20,
             x1 + 20 + highlight_size, y1 + 20 + highlight_size],
            fill="#FFFFFF60"
        )

    def _draw_body_base(
        self,
        draw: ImageDraw.ImageDraw,
        cx: int,
        cy: int,
        colors: Dict[str, str]
    ) -> None:
        """Draw basic humanoid body with 3D effect."""
        # Body (torso) - rounded rectangle with 3D effect
        body_width = 200
        body_height = 300
        body_top = cy + 180

        self._draw_3d_rounded_rect(
            draw,
            [cx - body_width // 2, body_top,
             cx + body_width // 2, body_top + body_height],
            radius=40,
            fill_color="#E8E8E8",
            outline_color=colors["accent"],
            width=8
        )

        # Arms with 3D effect
        arm_width = 40
        arm_length = 250
        # Left arm
        self._draw_3d_rounded_rect(
            draw,
            [cx - body_width // 2 - arm_width - 20, body_top + 50,
             cx - body_width // 2 - 20, body_top + 50 + arm_length],
            radius=20,
            fill_color="#E8E8E8",
            outline_color=colors["accent"],
            width=6
        )
        # Right arm
        self._draw_3d_rounded_rect(
            draw,
            [cx + body_width // 2 + 20, body_top + 50,
             cx + body_width // 2 + arm_width + 20, body_top + 50 + arm_length],
            radius=20,
            fill_color="#E8E8E8",
            outline_color=colors["accent"],
            width=6
        )

        # Legs with 3D effect
        leg_width = 50
        leg_length = 280
        leg_spacing = 30
        leg_top = body_top + body_height
        # Left leg
        self._draw_3d_rounded_rect(
            draw,
            [cx - leg_width - leg_spacing, leg_top,
             cx - leg_spacing, leg_top + leg_length],
            radius=25,
            fill_color="#E8E8E8",
            outline_color=colors["accent"],
            width=6
        )
        # Right leg
        self._draw_3d_rounded_rect(
            draw,
            [cx + leg_spacing, leg_top,
             cx + leg_width + leg_spacing, leg_top + leg_length],
            radius=25,
            fill_color="#E8E8E8",
            outline_color=colors["accent"],
            width=6
        )

    def _draw_3d_sphere(
        self,
        draw: ImageDraw.ImageDraw,
        cx: int,
        cy: int,
        radius: int,
        base_color: str,
        accent_color: str
    ) -> None:
        """Draw a 3D sphere with shading and highlights."""
        import math

        # Draw shadow
        shadow_offset = 12
        draw.ellipse(
            [cx - radius + shadow_offset, cy - radius + shadow_offset,
             cx + radius + shadow_offset, cy + radius + shadow_offset],
            fill="#00000040"
        )

        # Draw gradient sphere (multiple layers for 3D effect)
        num_layers = 20
        for i in range(num_layers):
            layer_radius = radius - (i * radius / num_layers)
            # Calculate shading based on distance from center
            alpha = (i / num_layers) ** 0.7  # Exponential for smoother gradient
            layer_color = self._blend_color(base_color, accent_color, alpha)

            draw.ellipse(
                [cx - layer_radius, cy - layer_radius,
                 cx + layer_radius, cy + layer_radius],
                fill=layer_color
            )

        # Add specular highlight (top-left)
        highlight_offset_x = -radius // 3
        highlight_offset_y = -radius // 3
        highlight_radius = radius // 3

        for i in range(5):
            h_radius = highlight_radius - (i * highlight_radius / 5)
            alpha = 1 - (i / 5)
            h_color = f"#FFFFFF{int(alpha * 150):02x}"

            draw.ellipse(
                [cx + highlight_offset_x - h_radius,
                 cy + highlight_offset_y - h_radius,
                 cx + highlight_offset_x + h_radius,
                 cy + highlight_offset_y + h_radius],
                fill=h_color
            )

        # Draw outline
        draw.ellipse(
            [cx - radius, cy - radius, cx + radius, cy + radius],
            outline=accent_color,
            width=6
        )

    def _draw_chatgpt_character(
        self,
        draw: ImageDraw.ImageDraw,
        size: tuple[int, int],
        colors: Dict[str, str]
    ) -> None:
        """
        Draw ChatGPT character with OpenAI logo as head.

        Head design: 3D spherical logo with ChatGPT pattern.
        """
        import math

        cx, cy = size[0] // 2, size[1] // 2 - 200

        # Draw body first
        self._draw_body_base(draw, cx, cy, colors)

        # Head: 3D sphere with OpenAI logo pattern
        head_radius = 150

        # Draw base 3D sphere
        self._draw_3d_sphere(
            draw, cx, cy, head_radius,
            colors["background"], colors["accent"]
        )

        # Add OpenAI ChatGPT icon pattern (3 dots in triangular formation)
        pattern_radius = head_radius - 60
        dot_radius = 25

        for angle_offset in [0, 120, 240]:
            angle_rad = math.radians(angle_offset - 90)
            dot_x = cx + int(pattern_radius * math.cos(angle_rad))
            dot_y = cy + int(pattern_radius * math.sin(angle_rad))

            # Draw 3D dot
            # Shadow
            draw.ellipse(
                [dot_x - dot_radius + 3, dot_y - dot_radius + 3,
                 dot_x + dot_radius + 3, dot_y + dot_radius + 3],
                fill="#00000040"
            )
            # Main dot with gradient
            for i in range(5):
                d_radius = dot_radius - (i * dot_radius / 5)
                alpha = i / 5
                dot_color = self._blend_color("#FFFFFF", colors["accent"], alpha * 0.8)
                draw.ellipse(
                    [dot_x - d_radius, dot_y - d_radius,
                     dot_x + d_radius, dot_y + d_radius],
                    fill=dot_color
                )
            # Highlight
            draw.ellipse(
                [dot_x - dot_radius // 3, dot_y - dot_radius // 3,
                 dot_x + dot_radius // 3, dot_y + dot_radius // 3],
                fill="#FFFFFF80"
            )

    def _draw_gemini_character(
        self,
        draw: ImageDraw.ImageDraw,
        size: tuple[int, int],
        colors: Dict[str, str]
    ) -> None:
        """
        Draw Gemini character with Google Gemini star logo as head.

        Head design: 3D star with depth and shading.
        """
        import math

        cx, cy = size[0] // 2, size[1] // 2 - 200

        # Draw body first
        self._draw_body_base(draw, cx, cy, colors)

        # Head: 3D star-shaped logo
        num_points = 8
        outer_radius = 160
        inner_radius = 80

        # Calculate star points
        star_points = []
        for i in range(num_points * 2):
            angle = i * math.pi / num_points - math.pi / 2
            if i % 2 == 0:
                radius = outer_radius
            else:
                radius = inner_radius
            x = cx + int(radius * math.cos(angle))
            y = cy + int(radius * math.sin(angle))
            star_points.append((x, y))

        # Draw shadow
        shadow_offset = 12
        shadow_points = [(x + shadow_offset, y + shadow_offset)
                        for x, y in star_points]
        draw.polygon(shadow_points, fill="#00000040")

        # Draw 3D layered star
        num_layers = 8
        for layer in range(num_layers, 0, -1):
            layer_scale = layer / num_layers
            layer_points = []

            for i in range(num_points * 2):
                angle = i * math.pi / num_points - math.pi / 2
                if i % 2 == 0:
                    radius = outer_radius * layer_scale
                else:
                    radius = inner_radius * layer_scale
                x = cx + int(radius * math.cos(angle))
                y = cy + int(radius * math.sin(angle))
                layer_points.append((x, y))

            # Color gradient for depth
            alpha = 1 - (layer / num_layers) * 0.7
            layer_color = self._blend_color(
                colors["background"],
                "#FFFFFF",
                alpha
            )

            draw.polygon(layer_points, fill=layer_color)

        # Draw outline
        draw.polygon(star_points, outline=colors["accent"], width=8)

        # Add inner decorative 3D star
        inner_star_points = []
        for i in range(num_points * 2):
            angle = i * math.pi / num_points
            if i % 2 == 0:
                radius = 70
            else:
                radius = 35
            x = cx + int(radius * math.cos(angle))
            y = cy + int(radius * math.sin(angle))
            inner_star_points.append((x, y))

        # Draw inner star with 3D effect
        for layer in range(3, 0, -1):
            scale = layer / 3
            scaled_points = [
                (cx + int((x - cx) * scale), cy + int((y - cy) * scale))
                for x, y in inner_star_points
            ]
            alpha = 1 - (layer / 3) * 0.5
            layer_color = self._blend_color(colors["accent"], "#FFFFFF", alpha)
            draw.polygon(scaled_points, fill=layer_color)

        # Add central 3D sphere
        center_radius = 25
        self._draw_3d_sphere(
            draw, cx, cy, center_radius,
            colors["accent"], colors["background"]
        )

        # Add sparkles with glow
        sparkle_positions = [
            (cx - 100, cy - 120, 15),
            (cx + 100, cy - 120, 15),
            (cx - 120, cy + 80, 12),
            (cx + 120, cy + 80, 12)
        ]
        for sx, sy, size_s in sparkle_positions:
            # Glow effect
            for i in range(3):
                glow_size = size_s + (3 - i) * 3
                alpha = 60 - (i * 20)
                draw.line(
                    [sx - glow_size, sy, sx + glow_size, sy],
                    fill=f"#FFFF88{alpha:02x}",
                    width=4
                )
                draw.line(
                    [sx, sy - glow_size, sx, sy + glow_size],
                    fill=f"#FFFF88{alpha:02x}",
                    width=4
                )
            # Main sparkle
            draw.line([sx - size_s, sy, sx + size_s, sy], fill="#FFFFFF", width=3)
            draw.line([sx, sy - size_s, sx, sy + size_s], fill="#FFFFFF", width=3)

    def _draw_claude_character(
        self,
        draw: ImageDraw.ImageDraw,
        size: tuple[int, int],
        colors: Dict[str, str]
    ) -> None:
        """
        Draw Claude character with Anthropic logo as head.

        Head design: 3D sphere with neural network pattern.
        """
        import math

        cx, cy = size[0] // 2, size[1] // 2 - 200

        # Draw body first
        self._draw_body_base(draw, cx, cy, colors)

        # Head: 3D sphere with neural network pattern
        head_radius = 140

        # Draw base 3D sphere
        self._draw_3d_sphere(
            draw, cx, cy, head_radius,
            colors["background"], colors["accent"]
        )

        # Add neural network / wave pattern (Anthropic style)
        # Draw 3D flowing nodes around the sphere

        num_nodes = 6
        node_positions = []
        for i in range(num_nodes):
            angle = i * math.pi / 3
            node_x = cx + int(60 * math.cos(angle))
            node_y = cy + int(60 * math.sin(angle))
            node_positions.append((node_x, node_y))

        # Draw connecting lines with gradient (behind nodes)
        for i in range(len(node_positions)):
            for j in range(i + 1, len(node_positions)):
                if abs(i - j) <= 2:
                    # Draw gradient line
                    x1, y1 = node_positions[i]
                    x2, y2 = node_positions[j]

                    # Shadow line
                    draw.line(
                        [(x1 + 2, y1 + 2), (x2 + 2, y2 + 2)],
                        fill="#00000030",
                        width=4
                    )
                    # Main line
                    draw.line(
                        [(x1, y1), (x2, y2)],
                        fill=colors["accent"],
                        width=3
                    )

        # Draw 3D nodes at connection points
        node_radius = 12
        for node_x, node_y in node_positions:
            # Draw 3D node
            # Shadow
            draw.ellipse(
                [node_x - node_radius + 2, node_y - node_radius + 2,
                 node_x + node_radius + 2, node_y + node_radius + 2],
                fill="#00000040"
            )

            # Gradient sphere for node
            for layer in range(5):
                r = node_radius - (layer * node_radius / 5)
                alpha = layer / 5
                node_color = self._blend_color("#FFFFFF", colors["accent"], alpha * 0.6)

                draw.ellipse(
                    [node_x - r, node_y - r, node_x + r, node_y + r],
                    fill=node_color
                )

            # Highlight
            draw.ellipse(
                [node_x - node_radius // 3, node_y - node_radius // 3,
                 node_x + node_radius // 3, node_y + node_radius // 3],
                fill="#FFFFFF90"
            )

        # Add central 3D node
        center_node_radius = 18
        # Shadow
        draw.ellipse(
            [cx - center_node_radius + 2, cy - center_node_radius + 2,
             cx + center_node_radius + 2, cy + center_node_radius + 2],
            fill="#00000040"
        )

        # Gradient sphere
        for layer in range(6):
            r = center_node_radius - (layer * center_node_radius / 6)
            alpha = layer / 6
            node_color = self._blend_color(colors["accent"], "#FFFFFF", alpha * 0.5)

            draw.ellipse(
                [cx - r, cy - r, cx + r, cy + r],
                fill=node_color
            )

        # Bright highlight
        draw.ellipse(
            [cx - center_node_radius // 2.5, cy - center_node_radius // 2.5,
             cx + center_node_radius // 2.5, cy + center_node_radius // 2.5],
            fill="#FFFFFFB0"
        )
