# Created quiz game with admin and players. A user has to login , if player then can play
# if admin can add question
import json
import users
import game

if __name__ == '__main__':
    welcome_msg = "Welcome to Quiz Game"
    print(f"{len(welcome_msg) * '*'} {welcome_msg} {len(welcome_msg) * '*'}")

    while True:
        current_player = users.login()
        user = ""
        for k in current_player.keys():
            user = k
            break
        print(f"\nLet's play {current_player[user]['full_name']} !\n")

        game.run_game(user, current_player)

        while True:
            MENU = """
            Ce vei face acum ?
            1. Play Again
            2. Log out
            3. Exit
            Choose one: """
            player_pick = input(MENU)
            match player_pick:
                case "1":
                    game.run_game(user, current_player)
                case "2":
                    break
                case "3":
                    exit()
