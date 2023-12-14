import json
from dataclasses import asdict, dataclass
from typing import Dict, List

import yaml


@dataclass
class Prompt:
    """
    Prompt stores all the information of a single prompt.
    """

    name: str
    tags: List[str]
    meta: Dict[str, str]
    version: str
    text: str
    description: str

    def to_yaml(self, file: str):
        with open(file, "w") as f:
            yaml.safe_dump(asdict(self), f)

    def to_json(self, file: str):
        with open(file, "w") as f:
            json.dump(asdict(self), f)


def prompt_from_json(file: str):
    with open(file) as f:
        data = json.load(f)
        return Prompt(
            data["name"],
            data["tags"],
            data["meta"],
            data["version"],
            data["text"],
            data["description"],
        )


def from_yaml(file: str):
    with open(file) as f:
        data = yaml.safe_load(f)
        return Prompt(
            data["name"],
            data["tags"],
            data["meta"],
            data["version"],
            data["text"],
            data["description"],
        )
