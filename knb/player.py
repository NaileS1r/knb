import random
class Player:  ### Создать игрок InterPlayer
    def __init__(self, name):
        self.name = name
        self.win_cnt = 0
        self.knbs = ['Камень', "Ножницы", "Бумага"]

    def knb(self):  ### какой будет ход
        knb = random.choice(self.knbs)
        self.state = knb
        print('Игрок', self.name, 'выкинул', knb)
        return knb