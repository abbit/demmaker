import os
import random
import uuid
from pathlib import Path
from typing import List

from PIL import Image


def get_random_phrase(phrases: List[str]) -> str:
    return random.choice(phrases)


def get_random_image(images_paths: List[str]) -> Image:
    random_image_path = random.choice(images_paths)
    return Image.open(random_image_path)


def save_image(img: Image, output_folder: Path) -> None:
    output_name = str(uuid.uuid4())
    output_path = output_folder / f'{output_name}.png'
    img.save(output_path)


def get_images_paths(images_folder: Path) -> List[str]:
    images_paths = []
    for _, __, filenames in os.walk(images_folder):
        for filename in [
            f for f in filenames if f.endswith(("png", "jpg", "jpeg"))
        ]:
            images_paths.append(os.path.join(images_folder, filename))

    return images_paths