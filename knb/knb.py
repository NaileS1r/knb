from player import Player
from interplayer import InterPlayer
from game import Game
def main():
    print('До скольки побед играем?')
    max_win = 5   ## исправить на инт инпут
    players_list= []
    print('Введите количество соперников')
    igrokov = 3   ## исправить на инпут
    print('Сыграете? Напишите: "Go", если хотите')
    otvet = input()

    if otvet == "Go":
        print("Введите ваше имя")   ### Добавить имя
        naile = InterPlayer(name = 'naile')
        players_list.append(naile)
    else:
        pass

    for i in range(1, len(igrokov)+1):
        a = Player(name = str(i))
        players_list.append(a)

    new_game = Game(players_list, max_win = max_win)
    new_game.play_game()

if __name__ == "__main__":
    main()
