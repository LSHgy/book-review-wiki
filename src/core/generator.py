import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


class ReviewGenerator:
    def __init__(self, yaml_path: str, template_dir: str = "templates"):
        self.yaml_path = Path(yaml_path)
        self.template_dir = Path(template_dir)
        self.env = Environment(loader=FileSystemLoader(str(self.template_dir)))
        self.data = self._load_yaml()

    def _load_yaml(self):
        with open(self.yaml_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def _create_file(self, path: Path, template_name: str, context: dict):
        """템플릿을 렌더링하여 파일을 생성합니다."""
        template = self.env.get_template(template_name)
        content = template.render(**context)

        # 부모 폴더가 없으면 생성
        path.parent.mkdir(parents=True, exist_ok=True)

        # 파일 쓰기 (이미 존재하면 덮어쓰지 않도록 설정 가능)
        if not path.exists():
            path.write_text(content, encoding='utf-8')
            print(f"📄 파일 생성됨: {path}")
        else:
            print(f"⚠️ 이미 존재함 (건너뜀): {path}")

    def generate(self):
        book_info = self.data.get('book')
        if not book_info:
            print("❌ YAML 형식이 올바르지 않습니다.")
            return

        # 1. 책 메인 디렉토리 설정
        base_dir = Path("wiki") / book_info['dir']

        # 2. 책 메인 메타데이터 파일 생성 (book.md)
        self._create_file(
            base_dir / "index.md",
            "book.md.j2",
            {"book": book_info}
        )

        # 3. 챕터별 폴더 및 파일 생성
        for chapter in book_info.get('chapters', []):
            # 폴더명 정제 (공백 제거 등)
            safe_chapter_title = chapter['title'].replace(" ", "_")
            chapter_path = base_dir / safe_chapter_title / "index.md"

            self._create_file(
                chapter_path,
                "chapter.md.j2",
                {"chapter": chapter, "book": book_info}
            )


if __name__ == "__main__":
    # 개별 실행 테스트용
    gen = ReviewGenerator("input.yaml")
    gen.generate()