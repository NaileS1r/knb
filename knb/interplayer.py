from player import Player
class InterPlayer(Player):
    def __init__(self,name):
        super().__init__(name)
        self.win_cnt = 0

    def knb(self):
        print(f"Введите 0, для {self.knbs[0]},Введите 1, для {self.knbs[1]}, Введите 2, для {self.knbs[2]}")
        my_input = input()
        self.state = self.knbs[int(my_input)]
        return self.state