import re
import yaml
from pathlib import Path

def parse_markdown_to_dict(filepath: str):
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {filepath}")

    file_name = path.stem
    content = path.read_text(encoding="utf-8")
    lines = content.split('\n')

    book_data = {
        "book": {
            "dir": file_name,  # 초기값
            "url": "[서점으로 이동]()",
            "cover": f"../../static/images/book-cover/{file_name}.png",
            "title": "",
            "chapters": []
        }
    }

    current_chapter = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 1. 책 제목 추출 (# 제목)
        if line.startswith("# "):
            title = line.replace("# ", "").strip()
            book_data["book"]["title"] = title
            # 디렉토리 이름 자동 생성 (공백을 하이픈으로, 소문자화)

        # 2. 챕터 추출 (## n장 제목)
        elif line.startswith("## "):
            chapter_title = line.replace("## ", "").strip()
            current_chapter = {"title": chapter_title, "sections": []}
            book_data["book"]["chapters"].append(current_chapter)

        # 3. 섹션 추출 (- 섹션명)
        elif line.startswith("- ") and current_chapter is not None:
            section_title = line.replace("- ", "").strip()
            current_chapter["sections"].append(section_title)

    return book_data


def save_to_yaml(data: dict, output_path: str):
    backup = data["book"]["dir"]
    with open(f"./data/wiki-yaml/{ backup }.yaml", 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)


if __name__ == "__main__":
    input_md = "./data/raw/.md"  # 입력 파일명
    output_yaml = "input.yaml"  # 출력 파일명

    try:
        data = parse_markdown_to_dict(input_md)
        save_to_yaml(data, output_yaml)
        print(f"✨ 성공적으로 YAML이 생성되었습니다: {output_yaml}")
    except Exception as e:
        print(f"❌ 에러 발생: {e}")