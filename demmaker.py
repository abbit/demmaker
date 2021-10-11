from pathlib import Path

from PIL.Image import ANTIALIAS
from PIL import Image, ImageDraw, ImageFont, ImageOps

DEFAULT_WIDTH = 760
DEFAULT_HEIGHT = 580
DEFAULT_BORDER = 4
DEFAULT_FONT_SIZE = 45


def create_demotivator(
        image: Image,
        phrase: str,
        font_path: Path,
        width: int = DEFAULT_WIDTH,
        height: int = DEFAULT_HEIGHT,
        border: int = DEFAULT_BORDER,
        max_font_size: int = DEFAULT_FONT_SIZE,
):
    demotivator, inner_img_width, inner_img_height = _create_image(image, width, height, border)

    font = _get_font(font_path, inner_img_width, phrase, max_font_size)
    _draw_text(demotivator, font, phrase)

    return demotivator


def _calculate_inner_image_size(width: int, height: int):
    return int(width * 0.8), int(height * 0.7)


def _create_image(user_img: Image, width: int, height: int, border: int) -> Image:
    img = Image.new('RGB', (width, height + 50), color='black')
    inner_img = user_img.convert("RGBA").resize(_calculate_inner_image_size(width, height), ANTIALIAS)
    inner_img = ImageOps.expand(inner_img, border=border, fill='#000000')
    inner_img = ImageOps.expand(inner_img, border=border, fill='#ffffff')
    inner_img_width, inner_img_height = inner_img.size
    img.paste(inner_img, (int((width - inner_img_width) / 2), int((height - inner_img_height) / 4)))

    return img, inner_img_width, inner_img_height


def _get_font(font_path: Path, inner_img_width: int, text: str, max_font_size: int) -> ImageFont:
    font_size = max_font_size

    font_path_str = str(font_path.absolute())

    text_font = ImageFont.truetype(font_path_str, font_size)
    text_width, _ = text_font.getsize(text)
    while text_width > inner_img_width:
        font_size -= 1
        text_font = ImageFont.truetype(font_path_str, font_size)
        text_width, _ = text_font.getsize(text)

    return text_font


def _draw_text(img: Image, font: ImageFont, text: str):
    draw = ImageDraw.Draw(img)
    img_width, img_height = img.size
    text_width, _ = font.getsize(text)

    draw.text(
        ((img_width - text_width) / 2, int(img_height * 0.8)),
        text,
        font=font,
        align="center",
    )

    return draw
