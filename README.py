# Numeronarvaus

# Peli kysyy käyttäjää arvaamaan numeroa väliltä 1-10, kunnes käyttäjä arvaa numeron oikein.Sitten ohjelma suljetaan.
# Mikäli numero oli liian iso tai pieni, kerrotaan käyttäjälle "liian iso" tai "liian pieni" ja kysytään uudelleen.
# Mieti miten saat ohjelman toimimaan alla olevilla metodeilla ja ohjeilla.

<<<<<<< Updated upstream
# eka versio

import math
import random
from random import randint
=======
import random
>>>>>>> Stashed changes

class NumberGuessingGame:

    def __init__(self):
<<<<<<< Updated upstream
        self.count = 0
        self.number = generate_random_number()
        
       
    def generate_random_number(self):

        return random.randint(1,10)
        
      
    def ask_number(self):
        self.guess = int(input("Anna numero välillä 1-10: "))
        return self.guess
              
    def add_guess_count(self):
        self.count += 1
=======
        self.pelin_arvo = self.generate_random_number()
        self.arvaukset = 0
       
    def generate_random_number(self):
        return random.randint(1, 10)
      
    def ask_number(self):
        return int(input("Anna arvo 1-10: "))
              
    def add_guess_count(self):
        self.arvaukset += 1
>>>>>>> Stashed changes
        
           
    def main_game_loop(self):
        while True:
<<<<<<< Updated upstream
            guess = self.ask_number()
       
            if guess == self.number:
                print("Numero oikein")
                print(f"Arvauksia yhteensä {self.count}")
                break
            elif guess < self.number:
                
                print("Liian pieni")
                print(f"Arvauksia tehty {self.count}")
            else:
                
                print("Liian suuri")
                print(f"Arvauksia tehty {self.count}")

        

        
=======
            arvoitus = self.ask_number()
            self.add_guess_count()

            if arvoitus > self.pelin_arvo:
                print("Liian iso")
            elif arvoitus < self.pelin_arvo:
                print("Liian pieni")
            else:
                print("Oikein!")
                print(f"Arvauksia: {self.arvaukset}")
                break

>>>>>>> Stashed changes

game = NumberGuessingGame()

game.main_game_loop()
