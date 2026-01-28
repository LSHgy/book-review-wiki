# Book Review Wiki Automator
Markdown 기반의 도서 리스트를 분석하여, 로컬 환경에 체계적인 독서 노트 폴더 구조를 자동으로 생성해주는 파이썬 도구입니다.

## Key Features
- MD to YAML Parsing: 단순 텍스트로 된 목차를 구조화된 데이터로 변환합니다.  
- Automated Scaffolding: 책 제목과 챕터명을 기반으로 폴더 및 index.md 파일을 자동 생성합니다.  
- Jinja2 Templates: 깔끔하고 일관된 Markdown 레이아웃을 제공합니다.  
- Smart Links: 메인 페이지와 각 챕터 간의 상호 이동 링크를 자동으로 구성합니다.  

## Project Structure
```Plaintext
book-review-wiki/
├── src/
│   ├── core/           # 폴더 생성 핵심 로직
│   └── parser/         # YAML 변환 스크립트
├── templates/          # Markdown 템플릿 (.j2)
├── data/               # 
│   ├── raw/            # 원본 도서 리스트 (Input)
│   └── wiki-yaml/      # 폴더 생성 설정 YAML 파일
├── wiki/               # 생성된 독서 노트 (Output)
└── main.py             # 통합 관리 CLI
```

### Quick Start
#### 1. 환경 설정
```bash
# 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 의존성 설치
pip install PyYAML Jinja2
```
#### 2. 사용 방법  
`main.py`를 통해 모든 작업을 수행할 수 있습니다.

A. **원천 데이터로부터 YAML 및 폴더 구조 한 번에 생성**
```bash
python main.py all -i ./data/raw/your-book.md
```

B. **단계별 실행**
```bash
# 1. YAML 생성: -i(req, 파싱대상) -o(출력파일)
python main.py parse -i ./data/raw/your-book-list.md -o input.yaml

# 2. 폴더 및 파일 생성
python main.py build -c input.yaml
```

### Input Format Example
원본 Markdown 파일(data/raw/*.md)은 아래와 같은 규칙을 따라야 합니다.
```markdown
# 책 제목
## 1장 챕터명
- 세부 섹션 1
- 세부 섹션 2
```

### Customization
Templates: templates/ 폴더 내의 .j2 파일을 수정하여 독서 노트의 디자인을 바꿀 수 있습니다.

Config: config.yaml에서 결과물이 저장될 경로 등을 설정할 수 있습니다
