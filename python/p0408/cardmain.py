#카드 프로그램 = Card 객체 사용 
import random
class CardGame:
    def __init__(self):
        self.shapes = [ "♣","♥","◆","♠" ]
        self.numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.card_list = []
        self.my_cards = []
        self.you_cards = []
        self.score = [0] * 5
    def create_cards(self):
        for i in range(52):
            self.card_list.append({"shape": i // 13, "no": i % 13 + 1})
        random.shuffle(self.card_list)
    def distribute_cards(self):
        for i in range(5):
            self.my_cards.append(self.card_list[i])
        for i in range(5, 10):
            self.you_cards.append(self.card_list[i]) 
    def print_cards(self, cards, owner):
        print(f"[{owner} 카드]")
        for card in cards:
            print(f"{self.shapes[card['shape']]} {self.numbers[card['no'] - 1]}")
    def compare_cards(self):
        for i in range(5):
            if self.my_cards[i]['no'] > self.you_cards[i]['no']:
                self.score[i] = 1
            elif self.my_cards[i]['no'] == self.you_cards[i]['no']:
                self.score[i] = 2
            else:
                self.score[i] = 0
    def print_results(self):
        print(f"승:{self.score.count(1)}, 무:{self.score.count(2)}, 패:{self.score.count(0)}")
        for i, s in enumerate(self.score):
            if s == 2:
                card = self.my_cards[i]
                print(f"무승부: {self.shapes[card['shape']]} {self.numbers[card['no'] - 1]}")
    def play(self):
        self.create_cards()
        self.distribute_cards()
        self.print_cards(self.my_cards, "내")
        self.print_cards(self.you_cards, "상대")
        self.compare_cards()
        self.print_results()
# 실행
game = CardGame()
game.play()
    #함수 
# cardmain.py
# 카드리스트객체 호출 
# 카드객체 호출  45장
# 각각 5장을 나눠준 다음 ,비교해서 큰수가 승리하는 형태 
#




         