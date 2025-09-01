
class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(f"{self.name}, {self.name}!")

    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {self.types}")
        print(f"Description: {self.description}")


Bulbasaur = Pokemon(1, "Bulbasaur", [
    "Grass", "Poison"], "For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.", False)
Charmander = Pokemon(4, "Charmander", [
    "Fire"], "It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail.", False)
Squirtle = Pokemon(7, "Squirtle", [
    "Water"], "When it retracts its long neck into its shell, it squirts out water with vigorous force.", True)

Bulbasaur.speak()
Bulbasaur.display_details()
print(" ")
Charmander.speak()
Charmander.display_details()
print(" ")
Squirtle.speak()
Squirtle.display_details()
