import random
from random import randint

# testi

class NumberGuessingGame:

    def __init__(self):
        self.count = 0
        self.number = self.generate_random_number()
        
       
    def generate_random_number(self):

        return random.randint(1,10)
        
      
    def ask_number(self):
        self.guess = int(input("Anna numero välillä 1-10: "))
        return self.guess
              
    def add_guess_count(self):
        self.count += 1
        return self.count
        
           
    def main_game_loop(self):
        while True:
            guess = self.ask_number()
       
            if guess == self.number:
                print("Numero oikein")
                print(f"Arvauksia yhteensä {self.add_guess_count()}")
                self.add_guess_count()
                break
            elif guess < self.number:
                
                print("Liian pieni")
                print(f"Arvauksia tehty {self.add_guess_count()}")
                self.add_guess_count()
            else:
                
                print("Liian suuri")
                print(f"Arvauksia tehty {self.add_guess_count()}")

        

        

game = NumberGuessingGame()

game.main_game_loop()
