import random
import time
from pathlib import Path

from PIL import Image
from typer import Typer, Option

from demmaker import create_demotivator, Template, Frame, Font
from utils import get_random_image, get_random_phrase, get_images_paths, save_image

app = Typer()


@app.command(help="DemMaker - генератор демотиваторов")
def create(
        template_path: Path = Option("assets/template.jpg", help="Путь к шаблону демотиватора"),
        images_folder: Path = Option("assets/images", help="Путь к картинкам для мемов"),
        phrases_path: Path = Option("assets/phrases.txt", help="Путь к файлу с фразами"),
        font_path: Path = Option("assets/times.ttf", help="Путь к шрифту"),
        font_size: int = Option(45, help="Размер шрифта"),
        seed: str = Option(time.time(),
                           help="Seed для создания картинки (По умолчанию берется время)",
                           show_default=False),
        output_folder: Path = Option("results", help="Куда сохранять демотиваторы"),
        count: int = Option(1, help="Сколько демотиваторов сгенерировать"),
):
    random.seed(seed)

    output_folder.mkdir(exist_ok=True)

    template_image = Image.open(template_path)
    template_image_width, template_image_height = template_image.size
    template = Template(
        image=template_image,
        width=template_image_width,
        height=template_image_height,
        frame=Frame(x_start=75, y_start=45, x_end=499, y_end=373),
        padding=10,
    )

    font = Font(font_filename=str(font_path), size=font_size, font_y=390)

    with open(phrases_path, encoding="utf-8") as phrases_file:
        phrases = phrases_file.readlines()

    images_paths = get_images_paths(images_folder)

    for _ in range(count):
        image = get_random_image(images_paths)
        phrase = get_random_phrase(phrases)
        demotivator_image = create_demotivator(template, image, phrase, font)
        save_image(demotivator_image, output_folder)


if __name__ == "__main__":
    app()
