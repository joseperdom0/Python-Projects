import random
import os
import time

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel", "abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward",
             "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard",
             "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing",
             "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl",
             "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking",
             "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled",
             "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm",
             "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic",
             "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy",
             "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy",
             "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit",
             "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz",
             "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx",
             "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka",
             "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes",
             "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx",
             "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied"]

chosen_word = random.choice(word_list)
print(''' _                                                   
| |__    __ _  _ __    __ _  _ __ ___    __ _  _ __  
| '_ \  / _` || '_ \  / _` || '_ ` _ \  / _` || '_ \ 
| | | || (_| || | | || (_| || | | | | || (_| || | | |
|_| |_| \__,_||_| |_| \__, ||_| |_| |_| \__,_||_| |_|
                      |___/                          ''')

time.sleep(1)
game_word = []
wrong_guesses = []
lives = 6
for _ in range(len(chosen_word)):
    game_word.append("_")

game_over = False
print(' '.join(game_word))
while not game_over:
    guess = input("Guess a letter: ").lower()

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            game_word[index] = letter
    if guess not in chosen_word:
        lives -= 1
        wrong_guesses.append(guess)

    print(stages[lives])
    print(' '.join(game_word))
    print(f"Lives left: {lives}")
    print(f"Wrong guesses: {' '.join(wrong_guesses)}")
    if "_" not in game_word:
        game_over = True
        print("You win!")
    if lives < 1:
        game_over = True
        print("You lose!")
        print(f"Your word was: {chosen_word}")
