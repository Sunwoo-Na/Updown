from random import randrange as setrandom # 랜덤 함수 import
from updownbase import EndOfGame

class Updown:
  def __init__(self, min_val, max_val):
    self.min = min_val
    self.max = max_val
    self.count = 1
    self.num = setrandom(self.min, self.max)
    self.answer = 0
    self.errmsg = f'{self.min}부터 {self.max}까지의 수를 입력해주세요.'

  def getinput(self):
    while True:
      self.answer = int(input(f'{self.count}번째 시도 >> '))
      if self.answer < self.min or self.answer > self.max:
        print('입력 범위를 벗어났습니다.')
        print(f'{self.min}부터 {self.max}까지의 수를 입력해주세요.')
        continue
      else:
        break

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
        elif self.count > 30:
          print('거 너무 감이 없으신 거 아닙니까...')
        self.exit()

  def start(self):
    print('업다운 게임을 시작합니다.')
    print(f'{self.min}부터 {self.max}까지의 수 중 아무거나 입력하세요.')
    while True:
      self.getinput()
      self.compare()
      self.count += 1

  def exit(self):
    raise EndOfGame # 원래 exit()를 사용해야 했지만...코랩에서는 exit()가 작동을 안 하네요
