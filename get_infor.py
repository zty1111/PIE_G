import os
import json


def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for key, value in data.items():
        frames = value.get("frames", [])
        bboxes = value.get("bboxes", [])
        intention = value.get("Intention", [])
        semantics = value.get("semantics", [])

        print(f"File: {file_path}")
        print(f"  Key: {key}")
        print(f"    Frames: {frames}")
        print(f"    Bboxes: {bboxes}")
        print(f"    Intention: {intention}")
        print(f"    Semantics: {semantics}")
        print("\n")


def main():
    base_folder = './group_anno'
    for set_folder in os.listdir(base_folder):
        set_path = os.path.join(base_folder, set_folder)
        if os.path.isdir(set_path):
            for json_file in os.listdir(set_path):
                if json_file.endswith('.json'):
                    json_file_path = os.path.join(set_path, json_file)
                    read_json_file(json_file_path)


if __name__ == "__main__":
    main()
