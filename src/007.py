#! /usr/bin/env python

# 작성한 파이썬 스크립트를 콘솔환경에서 실행할 때 외부에서 argument를 입력받아 이를 출력하도록 하자.

import sys
if len(sys.argv) !=2:
    print(f"python {sys.argv[0]} [sample]")
    sys.exit(1)


sample = sys.argv[1]

print(f"processing : {sample}")

# 처리 분석
print(f"end : {sample}")
