import argparse
from pathlib import Path
from src import ReviewGenerator
from src import parse_markdown_to_dict, save_to_yaml


def handle_parse(args):
    """MD -> YAML 변환 로직 실행"""
    input_path = Path(args.input)
    output_path = Path(args.output)

    print(f"🔍 분석 중: {input_path}...")
    data = parse_markdown_to_dict(input_path)
    save_to_yaml(data, output_path)
    print(f"✅ 설정 파일 생성 완료: {output_path}")


def handle_build(args):
    """YAML -> 폴더 구조 생성 실행"""
    print(f"🏗️ 빌드 시작: {args.config} 기반...")
    gen = ReviewGenerator(args.config)
    gen.generate()
    print("🚀 모든 폴더와 파일이 생성되었습니다!")


def main():
    parser = argparse.ArgumentParser(description="Book Review Wiki Automator")
    subparsers = parser.add_subparsers(dest="command", help="실행할 명령을 선택하세요")

    # 1. parse 명령어: MD를 읽어서 YAML 만들기
    parser_parse = subparsers.add_parser("parse", help="Markdown 파일을 YAML로 변환")
    parser_parse.add_argument("-i", "--input", required=True, help="원본 MD 파일 경로")
    parser_parse.add_argument("-o", "--output", default="input.yaml", help="저장할 YAML 파일명")

    # 2. build 명령어: YAML을 읽어서 폴더 구조 만들기
    parser_build = subparsers.add_parser("build", help="YAML 기반으로 폴더 구조 생성")
    parser_build.add_argument("-c", "--config", default="input.yaml", help="참조할 YAML 파일명")

    # 3. all 명령어: 한 번에 둘 다 실행
    parser_all = subparsers.add_parser("all", help="Parse와 Build를 한 번에 실행")
    parser_all.add_argument("-i", "--input", required=True, help="원본 MD 파일 경로")
    parser_all.add_argument("-o", "--output", default="input.yaml", help="저장할 YAML 파일명")

    args = parser.parse_args()

    if args.command == "parse":
        handle_parse(args)
    elif args.command == "build":
        handle_build(args)
    elif args.command == "all":
        handle_parse(args)
        # build용 가상 args 생성
        args.config = args.output if hasattr(args, 'output') else "input.yaml"
        handle_build(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()