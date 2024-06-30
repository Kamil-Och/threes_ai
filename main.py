import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'game'))

from threes import Game
from threes import MoveDirection

def main():
    game = Game()
    
    game.start()
    
    print("Game started\n")
    print("Your board is: \n", game.board.tiles, "\n")
    
    while True:
        move_maked = False
            
        player_input = input("Enter a move: [w - up, s - down, a - left, d - right || q -exit]")
        if player_input == "w":
            game.move(MoveDirection.UP)
            move_maked = True
        elif player_input == "s":
            game.move(MoveDirection.DOWN)
            move_maked = True
        elif player_input == "a":
            game.move(MoveDirection.LEFT)
            move_maked = True
        elif player_input == "d":
            game.move(MoveDirection.RIGHT)
            move_maked = True
        elif player_input == "q":
            print("Exiting game")
            break
        else:
            print("Invalid move try again \n")
            
        if move_maked:
            print("Your board is: \n", game.board.tiles, "\n")
            print("")
            print("Score: ", game.get_score())
        
        if game.available_moves() == []:
            print("No more moves available")
            break
    


if __name__ == "__main__":
    main()