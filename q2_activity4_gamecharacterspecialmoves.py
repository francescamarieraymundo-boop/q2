
# 1. Create the three classes

class Warrior:
    def special_move(self):
        print("Warrior swings a mighty sword!")


class Mage:
    def special_move(self):
        print("Mage casts a powerful spell!")


class Archer:
    def special_move(self):
        print("Archer shoots a precise arrow!")


# 2. Create the perform_move() function

def perform_move(character):
    character.special_move()


# 3. Create one object of each class

warrior = Warrior()
mage = Mage()
archer = Archer()


# 4. Store the objects in a list

characters = [warrior, mage, archer]


# 5. Use a loop to perform each character's special move

for character in characters:
    perform_move(character)
