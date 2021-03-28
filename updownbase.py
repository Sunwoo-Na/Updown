def GetVersion():
    return 4.0
    
class EndOfGame(BaseException):
  pass # exit() 함수가 말을 안 들어서 예외처리로 종료를 하려고 합니다