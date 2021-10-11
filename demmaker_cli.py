from pathlib import Path

from typer import Typer, Option

from demmaker import create_demotivator
from utils import get_random_image, get_random_phrase, get_images_paths, save_image

app = Typer()


@app.command(help="DemMaker - генератор демотиваторов")
def create(
        images_folder: Path = Option("assets/images", help="Путь к папке с картинкамм"),
        phrases_path: Path = Option("assets/phrases.txt", help="Путь к файлу с фразами"),
        font_path: Path = Option("assets/times.ttf", help="Путь к шрифту"),
        output_folder: Path = Option("results", help="Куда сохранять демотиваторы"),
        count: int = Option(1, help="Сколько демотиваторов сгенерировать"),
):
    output_folder.mkdir(exist_ok=True)

    with open(phrases_path, encoding="utf-8") as phrases_file:
        phrases = phrases_file.readlines()

    images_paths = get_images_paths(images_folder)

    for _ in range(count):
        image = get_random_image(images_paths)
        phrase = get_random_phrase(phrases)
        demotivator_image = create_demotivator(image, phrase, font_path)
        save_image(demotivator_image, output_folder)


if __name__ == "__main__":
    app()
