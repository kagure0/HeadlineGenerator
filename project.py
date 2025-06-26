# importing the random module
import random

# Creating Lists
subjects = [
    "Modi",
    "A man",
    "Monkey",
    "Panda",
    "Aliens",
    "A dog in a suit",
    "Time traveler",
    "Elon Musk",
    "Robot chef",
    "A flying cat",
    "Talking potato",
    "Grandma with a jetpack",
    "Invisible boy",
    "Dancing skeleton",
    "AI overlord",
    "Angry toaster",
    "Superhero without powers",
    "Undercover penguin",
    "Haunted teddy bear",
    "Ghost with a megaphone"
]

actions = [
    "was riding a dinosaur",
    "declared war on pigeons",
    "invented invisible food",
    "gave a motivational speech",
    "started dancing randomly",
    "built a rocket out of garbage",
    "stole all the bananas",
    "painted the sky",
    "opened a portal to another dimension",
    "proposed to the moon",
    "teleported using a washing machine",
    "challenged a robot to arm wrestling",
    "coded a video game using bananas",
    "screamed at a mirror for 3 hours",
    "accidentally became president",
    "won a cooking contest with lava",
    "turned the Eiffel Tower into a slide",
    "played cricket with aliens",
    "installed Windows on the moon",
    "wrote a love letter to gravity"
]

places = [
    "at Red Fort",
    "in Mumbai",
    "on the moon",
    "inside a volcano",
    "in a McDonald's parking lot",
    "at a secret underwater lab",
    "on top of Mount Everest",
    "at Delhi Metro Station",
    "in a haunted library",
    "in the middle of the Sahara desert",
    "inside the White House kitchen",
    "underneath the Statue of Liberty",
    "on a UFO hovering over Goa",
    "in a subway full of zombies",
    "at Hogwarts",
    "in an abandoned spaceship",
    "in Antarctica wearing shorts",
    "on Mars during a tea party",
    "inside a virtual reality glitch",
    "at the bottom of the Pacific Ocean"
]

# Implementing the headline generator
while True:
    subject = random.choice(subjects)
    act = random.choice(actions)
    place = random.choice(places)

    print(f"\n📰 Breaking News: {subject} {act} {place}!")

    user_input = input("\nDo you want to continue? (yes/no): ").strip().lower()
    if user_input == "no":
        print("\nThanks for using the Fake Headline Generator! Goodbye 👋")
        break
