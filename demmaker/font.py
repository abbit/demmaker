from dataclasses import dataclass


@dataclass
class Font:
    font_filename: str
    size: int
    font_y: int
