import os
import json
from googletrans import Translator

translator = Translator()


def translate_description(description):
    try:
        translated = translator.translate(description, src='zh-cn', dest='en')
        return translated.text
    except Exception as e:
        print(f"Error translating {description}: {e}")
        return description


def process_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 遍历每个键（如set01_video_0001_g01）
    for key in data:
        if "semantics" in data[key]:
            for semantic in data[key]["semantics"]:
                if "description" in semantic:
                    original_desc = semantic["description"]
                    translated_desc = translate_description(original_desc)
                    semantic["description"] = translated_desc

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    base_folder = './group_anno'
    for set_folder in os.listdir(base_folder):
        set_path = os.path.join(base_folder, set_folder)
        if os.path.isdir(set_path):
            for json_file in os.listdir(set_path):
                if json_file.endswith('.json'):
                    json_file_path = os.path.join(set_path, json_file)
                    process_json_file(json_file_path)
                    print(f"Processed {json_file_path}")


if __name__ == "__main__":
    main()
