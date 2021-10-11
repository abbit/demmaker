from pathlib import Path
from typing import List
from argparse import ArgumentParser
import json


def extract_from_json(history_json: Path) -> List[str]:
    with open(history_json, "r") as file:
        j = json.load(file)

        return [m['text'] for m in j['messages'] if m['text']]


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("history_file", type=Path, help="chat_history.json file")
    parser.add_argument("phrases_file", type=Path, help="phrases.txt file")
    args = parser.parse_args()

    with open(args.phrases_file, "a") as phrases_file:
        new_lines = extract_from_json(args.history_file)
        for new_line in new_lines:
            phrases_file.write(f"\n{new_line}")
