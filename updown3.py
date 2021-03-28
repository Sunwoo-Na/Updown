import sys
import updown2
from updownbase import GetVersion as VERSION

# 입력 값 검증을 추가하고 난이도 조절 옵션을 넣은 새로운 상속 클래스
class Updown3(updown2.Updown):
  def __init__(self):
    self.modemsg = """난이도를 결정하세요:

1) EASY: 범위 1~50, 기회 제한 없음
2) MEDIUM(기본): 범위 1~100, 기회 제한 50회
3) HARD: 범위 1~500, 기회 제한 20회

입력(1~3) >> """
    self.modes = {
        1:(1, 50, sys.maxsize), # 파이썬에서는 swtich~case가 없더라고요
        2:(1, 100, 50),         # 그래서 그냥 룩업테이블 비슷하게
        3:(1, 500, 20)          # 구현해봤습니다
        }
    
    diff = input(self.modemsg)
    diff_int = 0
    if (diff.isdigit()):
      diff_int = int(diff)
    else:
      print('잘못된 입력값입니다. 기본모드로 시작합니다.')
      
    (min, max, self.max_count) = modes.get(diff_int, (1, 100, 50))
    super().__init__(min, max)

  def getinput(self):
    while True:
      answerstr = input(f'{self.count}번째 시도 >> ')
      if (answerstr.isdigit() == False):
        print(self.errmsg)
        continue        # 숫자가 아니면 다시 입력받기
      self.answer = int(answerstr)
      if self.answer < self.min or self.answer > self.max:   
        print('입력 범위를 벗어났습니다.')
        print(self.errmsg)
      else:
        break

  def start(self):
    print(f'\n업다운 게임 V{VERSION()}을(를) 시작합니다.')
    print(f'{self.min}부터 {self.max}까지의 수 중 아무거나 입력하세요.')
    while True:
      self.getinput()
      self.compare()
      self.count += 1
      if (self.count > self.max_count):
        print('입력 횟수를 초과했습니다!')
        print('GAME OVER...')
        super().exit()

  def compare(self):
    if self.answer < self.num:
      print('UP')
    elif self.answer > self.num:
      print('DOWN')
    elif self.answer == self.num: # => else로 대체 가능
      print('CORRECT')
      print(f'{self.count}번만에 맞추셨습니다.')
      if self.count == 1:
        print('잠깐만요 이거 찍은 거죠? 뭐지...? 어떻게 단번에 맞췄지..?')
      self.exit()
