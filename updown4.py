import sys
import updown2
import updown3
from updownbase import GetVersion as VERSION
from enum import Enum, auto
import datetime

class GameMode(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()
    IMPOSSIBLE = auto()

# 새로운 모드 추가, 코드 재사용 비율 UP
class UpdownPlus(updown3.Updown3): # Updown 4.0 == UpdownPlus
  def __init__(self):
    self.modemsg, self.modes = self.getmode()
    
    diff = input(self.modemsg)
    diff_int = 0
    if (diff.isdigit()):
      diff_int = int(diff)
    else:
      print('잘못된 입력값입니다. 기본모드로 시작합니다.')
      
    (min, max, self.max_count) = self.modes.get(diff_int, (1, 100, 50))
    updown2.Updown.__init__(self, min, max)
    
    self.gamemode = {
      50: GameMode['EASY'],
      100: GameMode['MEDIUM'],
      500: GameMode['HARD'],
      1000: GameMode['IMPOSSIBLE']
    }.get(self.max, GameMode['MEDIUM'])
    
  def getmode(self):
    msg =  """난이도를 결정하세요:

1) EASY: 범위 1~50, 기회 제한 없음
2) MEDIUM(기본): 범위 1~100, 기회 제한 50회
3) HARD: 범위 1~500, 기회 제한 20회
4) IMPOSSIBLE: 범위 1~1000, 기회 제한 10회

입력(1~4) >> """
    modes = {
        1:(1, 50, sys.maxsize),
        2:(1, 100, 50),
        3:(1, 500, 20),
        4:(1, 1000, 10)
    }
    return (msg, modes)
    
  def exit(self):
    time = datetime.datetime.now().replace(microsecond = 0)
    f = open("result.txt", "a")
    f.write(f'{time}\t\t{self.gamemode.name}\t\tcount: {self.count}\n')
    f.close()
    super().exit()
