class Game:
    def __init__(self, players, max_win):
        self.players = players
        self.max_win = max_win

    def play_round(self):
        round_set = set()
        for player in self.players:
            round_set.add(player.knb())
        if len(round_set) == 3 or len(round_set) == 1:
            print('Ничья')
        else:
            if "Ножницы" in round_set and "Камень" in round_set:
                winning_item = "Камень"
            elif "Ножницы" in round_set and "Бумага" in round_set:
                winning_item = "Ножницы"
            else:
                winning_item = "Бумага"
            for player in self.players:
                if player.state == winning_item:
                    player.win_cnt += 1
                    print(f"Победил игрок,{player.name}")

    def play_game(self):
        max_score = 0
        while max_score < self.max_win:
            max_score_list = []
            self.play_round()
            for player in self.players:
                max_score_list.append(player.win_cnt)
                max_score = max(max_score_list)
        print(f"Game over")
        for player in self.players:
            print("Игрок", player.name, "имеет", player.win_cnt, "очков")