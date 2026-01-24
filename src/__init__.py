# src/__init__.py

# 하위 모듈에서 주요 클래스를 끌어올려(Promotion),
# 외부에서 'from src import ReviewGenerator'로 바로 쓸 수 있게 합니다.
from .core.generator import ReviewGenerator
from .parser.generate_yaml import parse_markdown_to_dict, save_to_yaml

__all__ = ["ReviewGenerator", "parse_markdown_to_dict", "save_to_yaml"]