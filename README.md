# NXJ Embedding Tool

문서 임베딩 및 검색을 위한 툴입니다.

## 기능

- JSON 파일에서 텍스트 데이터 추출
- intfloat/multilingual-e5-small 모델을 사용한 임베딩 생성
- FAISS를 사용한 고속 벡터 검색
- 다국어 지원 (한국어 포함)

## 설치

1. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

## 사용법

### 1. 임베딩 생성

#### 방법 1: 실행 스크립트 사용
```bash
python main_embed.py
```

#### 방법 2: 직접 실행
```bash
python embedding_tool.py --input_dir "파싱 결과 JSON 파일 디렉토리" --output_dir "임베딩 결과 JSON 파일 디렉토리"
```

#### 옵션
- `--input_dir`: 입력 JSON 파일 디렉토리 (기본값: /NXJ_Parser_Text/output)
- `--output_dir`: 출력 디렉토리 (기본값: /NXJ_Embed/emb)
- `--batch_size`: 배치 크기 (기본값: 32)
- `--model_name`: 임베딩 모델명 (기본값: intfloat/multilingual-e5-small)

### 2. 검색

```bash
python search_tool.py --query "검색할 내용"
```

#### 옵션
- `--query`: 검색 쿼리 (필수)
- `--top_k`: 반환할 결과 수 (기본값: 10)
- `--index_dir`: FAISS 인덱스 디렉토리 (기본값: /NXJ_Embed/emb)
- `--model_name`: 임베딩 모델명 (기본값: intfloat/multilingual-e5-small)

## 출력 파일

임베딩 프로세스가 완료되면 다음 파일들이 생성됩니다:

- `faiss_index.bin`: FAISS 벡터 인덱스
- `metadata.json`: 텍스트 청크 메타데이터
- `stats.json`: 통계 정보

## 예시

### 임베딩 생성
```bash
cd /~/NXJ_Embed
python main_embed.py
```

### 검색
```bash
python search_tool.py --query "의료기기 허가 심사"
```

## 구조

```
/home/james4u1/NXJ_Embed/
├── embedding_tool.py      # 메인 임베딩 스크립트
├── search_tool.py         # 검색 스크립트
├── main_embed.py       # 실행 스크립트
├── requirements.txt       # 필요한 패키지
├── README.md             # 이 파일
├── emb/                  # 임베딩 결과 저장 디렉토리
│   ├── faiss_index.bin
│   ├── metadata.json
│   └── stats.json
└── embedding.log         # 로그 파일
```

## 주의사항

1. 첫 실행 시 모델 다운로드에 시간이 걸릴 수 있습니다.
2. 대용량 데이터의 경우 충분한 메모리가 필요합니다.
3. GPU가 있다면 자동으로 사용됩니다.

## 로그

실행 로그는 `embedding.log` 파일에 저장됩니다. 