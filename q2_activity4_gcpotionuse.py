
# 1. Create the three classes

class HealthPotion:
    def use(self):
        print("You regain 50 HP!")


class ManaPotion:
    def use(self):
        print("You restore 30 MP!")


class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds!")


# 2. Create the apply_item() function

def apply_item(item):
    item.use()


# 3. Create one object of each class

health = HealthPotion()
mana = ManaPotion()
speed = SpeedBoost()


# 4. Store the objects in a list

potions = [health, mana, speed]


# 5. Use a loop to apply each item

for item in potions:
    apply_item(item)
