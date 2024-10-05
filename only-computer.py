from random import randrange as setrandom

class EndOfGame(BaseException):
    pass

class UpdownSolver:
    def __init__(self, min, max):
        self.intrange = list(range(min, max + 1))
        self.number = len(self.intrange)//2

    def GetResult(self, result: str):
        while True:
            if result == 'UP':
                self.intrange = self.intrange[self.intrange.index(self.number):]
                self.number = self.intrange[len(self.intrange)//2]
                return
            elif result == 'DOWN':
                self.intrange = self.intrange[:self.intrange.index(self.number)]
                self.number = self.intrange[len(self.intrange)//2]
                return
            elif result == 'CORRECT':
                raise EndOfGame

class UpdownQuizer:
    def __init__(self, minv: int, maxv: int):
        self.min, self.max = minv, maxv
        self.count = 1
        self.num = setrandom(self.min, self.max)
    
    def Compare(self, number: int) -> str:
        if number < self.num:
            return 'UP'
        elif number > self.num:
            return 'DOWN'
        elif number == self.num:
            return 'CORRECT'

class UpdownMain:
    def __init__(self):
        print('컴퓨터끼리 업다운 게임을 시작하겠습니다.')
        self.min = int(input('컴퓨터 A가 설정할 수의 최솟값을 입력하세요(예시: 1): '))
        self.max = int(input('컴퓨터 A가 설정할 수의 최댓값을 입력하세요(예시: 100): '))
        self.solve = UpdownSolver(self.min, self.max)
        self.quiz = UpdownQuizer(self.min, self.max)
    
    def Run(self): 
        print(f'컴퓨터 A가 생각한 숫자는 {self.quiz.num}입니다.')
        while True:
            print(f'[{self.quiz.count}차 시도] 컴퓨터 B가 {self.solve.number}을(를) 제시했습니다.')
            result = self.quiz.Compare(self.solve.number)
            print(f'컴퓨터 A: {result}')
            self.solve.GetResult(result)
            self.quiz.count += 1

try:
    ui = UpdownMain()
    ui.Run()
except EndOfGame:
    print(f'컴퓨터 B가 {ui.quiz.count}번 만에 맞췄습니다.')
    print('게임을 종료합니다.')