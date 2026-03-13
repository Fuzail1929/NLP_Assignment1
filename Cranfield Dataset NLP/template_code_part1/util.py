# util.py

import json
import os


def read_json(path):
    """
    Read a JSON file and return its content.
    """
    with open(path, "r") as f:
        return json.load(f)


def write_json(path, data):
    """
    Write data to a JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f)


def ensure_dir(path):
    """
    Create directory if it does not exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)

# Utility file for helper functions and common imports 