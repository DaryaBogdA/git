import random

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank}  {self.suit}"

class Deck:
    def __init__(self):
        suits = ['Чирва', 'Пики', 'Крести', 'Буба']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
                  'Валет': 2, 'Дама': 3, 'Король': 4, 'Туз': 1}
        self.cards = [Card(suit, rank, values[rank]) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)
        self.score += card.value
        if self.score > 21:
            for c in self.hand:
                if c.rank == 'Туз' and self.score > 21:
                    self.score -= 10

    def __str__(self):
        return f"{self.name} имеет {', '.join(str(card) for card in self.hand)} (Очки: {self.score})"

class BlackJackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Ты")
        self.comp = Player("Компьютер")

    def play(self):
        print("Добро пожаловать в 21 очко")
        self.player.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.comp.add_card(self.deck.deal_card())
        self.comp.add_card(self.deck.deal_card())

        print(self.player)
        print(self.comp)

        while self.player.score < 21:
            choice = input("Хочешь взять еще 1 - да: ").lower()
            if choice == '1':
                self.player.add_card(self.deck.deal_card())
                print(self.player)
            else:
                break

        while self.comp.score < 17:
            self.comp.add_card(self.deck.deal_card())

        print(self.comp)

        if self.player.score > 21:
            print("Ты проиграл.")
        elif self.comp.score > 21 or self.player.score > self.comp.score:
            print("Ты выиграл!")
        elif self.player.score < self.comp.score:
            print("Компутер выиграл!")
        else:
            print("Ничья")


game = BlackJackGame()
game.play()
