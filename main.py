# Created quiz game with admin and players. A user has to login , if player then can play
# if admin can add question
import json
import users
import game




if __name__ == '__main__':
    welcome_msg = "Welcome to Quiz Game"
    print(f"{len(welcome_msg) * '*'} {welcome_msg} {len(welcome_msg) * '*'}")

    current_player = users.login()

    while True:
        print(f"Let's play ")
        game.run_game(current_player)
