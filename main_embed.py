#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
임베딩 툴 실행 스크립트
"""

import os
import sys
from embedding_tool import EmbeddingTool

def main():
    # 설정
    input_dir = "/home/james4u1/NXJ_Parser_Text/output"
    output_dir = "/home/james4u1/NXJ_Embed/emb"
    model_name = "intfloat/multilingual-e5-small"
    batch_size = 64
    
    # 출력 디렉토리 생성
    os.makedirs(output_dir, exist_ok=True)
    
    print("=" * 60)
    print("문서 임베딩 툴 실행")
    print("=" * 60)
    print(f"입력 디렉토리: {input_dir}")
    print(f"출력 디렉토리: {output_dir}")
    print(f"모델: {model_name}")
    print(f"배치 크기: {batch_size}")
    print("=" * 60)
    
    # 임베딩 툴 실행
    try:
        tool = EmbeddingTool(model_name)
        tool.process(input_dir, output_dir, batch_size)
        print("\n임베딩 프로세스가 성공적으로 완료되었습니다!")
        
    except Exception as e:
        print(f"\n오류 발생: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 