import random

def generate_pet_name():
    first_names = ["Coco", "Bella", "Luna", "Lucy", "Daisy", "Lily", "Molly", "Sophie", "Chloe", "Zoe"]
    last_names = ["Paws", "Whiskers", "Fluffy", "Tail", "Furball", "Snuggles", "Pawprint", "Meow", "Bark", "Woof"]
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    return f"{first_name} {last_name}"

def main():
    print("Welcome to the Pet Name Generator!")
    input("Press Enter to generate a name...")
    
    pet_name = generate_pet_name()
    print(f"Your pet's name is: {pet_name}")

if __name__ == "__main__":
    main()