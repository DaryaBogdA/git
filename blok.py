import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_dice(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        print(f"""{self.name} выбросил 
              -----------  -----------
              |         |  |         |
              |    {dice1}    |  |    {dice2}    | 
              |         |  |         |
              -----------  -----------
                Сумма: {total}""")
        self.score += total

class DiceGame:
    def __init__(self):
        self.rounds = 6
        self.human = Player("Человек")
        self.computer = Player("Компьютер")

    def determine_first_player(self):
        return random.choice([self.human, self.computer])

    def play(self):
        print("Добро пожаловать в игру Кубики")
        current_player = self.determine_first_player()
        print(f"Первым ходит: {current_player.name}")
        
        for round_num in range(1, self.rounds + 1):
            print(f"--- Раунд {round_num} ---")
            

            if current_player == self.human:
                input("Нажмите Enter")
                self.human.roll_dice()
                print(f"Ваш счёт: {self.human.score}")
                current_player = self.computer 
            else:
                print("Компьютер ходит")
                self.computer.roll_dice()
                print(f"Счёт компьютера: {self.computer.score}")
                current_player = self.human 
        

        self.show_results()

    def show_results(self):
        print("--- Итоги игры ---")
        print(f"{self.human.name}: {self.human.score} очков")
        print(f"{self.computer.name}: {self.computer.score} очков")
        
        if self.human.score > self.computer.score:
            print("Вы победили!")
        elif self.human.score < self.computer.score:
            print("Победил компьютер!")
        else:
            print("Ничья!")


game = DiceGame()
game.play()
