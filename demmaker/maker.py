from PIL.Image import ANTIALIAS
from PIL import Image, ImageDraw, ImageFont

from demmaker.font import Font
from demmaker.template import Template


def create_demotivator(
        template: Template,
        image: Image,
        phrase: str,
        font: Font,
):
    demotivator = template.image.copy()
    demotivator_image = image.resize(template.frame.size, ANTIALIAS)
    demotivator.paste(demotivator_image, template.frame.coords)
    __draw_x_axis_centered_text(demotivator, font, phrase, template.padding)

    return demotivator


def __draw_x_axis_centered_text(img: Image, font: Font, text: str, padding: int):
    draw = ImageDraw.Draw(img)
    img_width, img_height = img.size
    text_font = ImageFont.truetype(font.font_filename, font.size)
    text_width = text_font.getsize(text)[0]

    while text_width >= img_width - padding * 2:
        text_font = ImageFont.truetype(font.font_filename, font.size)
        text_width = text_font.getsize(text)[0]
        font.size -= 1

    draw.text(
        ((img_width - text_width) / 2, font.font_y),
        text,
        font=text_font,
        align="center",
    )

    return draw
