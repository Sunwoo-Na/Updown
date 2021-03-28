#
#     [OOP] updown python.ipynb
#
#     Object-Oriented Programming(OOP) version of
#     Up-Down game by 2816 Sunwoo Na.
#
# WHAT's NEW:
#   VERSION 4.0: Added IMPOSSIBLE mode and logging system
#                   새로운 모드 추가, 파일 입출력 기능 추가
#
#   VERSION 3.4: Github migration.
#   VERSION 3.3: Fixed runtime bugs.
#   VERSION 3.2: Fixed bug, stablized program.
#   VERSION 3.0: Added class Updown3
#                오류 검증 기능 추가, 난이도 설정 추가
#
#   VERSION 2.3: Optimized source code.
#   VERSION 2.2: Fixed input bug.
#   VERSION 2.0: Changed source to OOP using class
#
#   VERSION 1.0 [LEGACY]: FIRST RELEASE
#
#
#   Copyright (c) 2021 Sunwoo Na. All rights reserved.
#   본 소스 코드의 저작권은 Rolling Ress (TM) @ 나선우에게 있습니다.
#   설마 누가 이걸 도용할까 싶지만 혹시 몰라서 적어두는 저작권 문구.

import updown4
from updown2 import EndOfGame

try:
  # game = updown2.Updown() # V2.x 플레이
  # game = updown3.Updown3() # V3.x 플레이
  game = updown4.UpdownPlus() # V4.x 플레이
  game.start()
except EndOfGame:
  print('게임을 종료합니다.')