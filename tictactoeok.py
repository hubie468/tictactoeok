import random



class Player:
    def __init__(self,name,token):
        self.name= name
        self.token = token
player_1 = Player('alex', 'x')
player_2 = Player('isabel', 'o')

class game:
    def __repr__(self, board):
        self.board = board
            
    def board(self):
        board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
        print(board)

    def move(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
    #def calc_winner():
    
    #def is_full():
    
    #def is_game_over():
    '''
    {first : [left, middle, right]}
    {second : [left, middle, right]}
    {third : [left, middle, right]}

def select_letter():
    letter=""
    computer_letter=""
    letter=input("Select X or O: ")
    if letter == "x":
        computer_letter="o"
    else:
        computer_letter="x"
    return letter, computer_letter

def main():
'''
