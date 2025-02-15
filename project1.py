import random
import string
adjectives = ['slow', 'fast','clean', 'dirty','curly', 'straight','difficult', 'easy','good', 'bad','early', 'late','fat', 'thin','full', 'empty',  'hot', 'cold',  'happy', 'sad', 'unhappy',  'hardworking', 'lazy',  'modern', 'traditional',  'new', 'old',  'nice', 'nasty','attractive',  'bald',  'beautiful',  'chubby',  'clean',  'dazzling',  'drab',  'elegant',  'fancy',  'fit',  'flabby',  'glamorous',  'gorgeous',  'handsome',  'long',  'magnificent',  'muscular',  'plain',  'plump',  'quaint',  'scruffy','Red',  'Orange',  'Yellow',  'Green',  'Blue',  'Purple',  'Rainbow',  'Tricolor',  'Lime',  'Goldenrod',  'Violet',  'Lavender',  'Fuchsia',  'Cerise',  'Pink',  'Black',  'Brown',  'White','Curvy',  'Miniature',  'Thickset',  'Emaciated',  'Minute',  'Tiny',  'Illimitable',  'Sizable',  'Bulky',  'Mammoth',  'Strapping',  'Enormous',  'Obese',  'Towering',  'Fleshy',  'Petite',  'Underweight',  'Compact','Alive',  'Annoying',  'Bad',  'Beautiful',  'Better',  'Brainy',  'Breakable',  'Busy',  'Careful',  'Clever',  'Clumsy',  'Crazy',  'CuriousDead',  'Different',  'Difficult',  'Doubtful',  'Easy',  'Expensive',  'Concerned','Curvy',  'Miniature',  'ThicksetEmaciated',  'Minute',  'Tiny',  'Illimitable',  'Sizable',  'Bulky',  'Mammoth',  'Strapping',  'Enormous',  'Obese','Towering',  'Fleshy',  'Petite',  'Underweight',  'Compact','cooing',  'deafening',  'faint',  'harsh',  'high-pitched',  'hissing',  'hushed',  'husky',  'loud',  'melodic',  'moaning',  'mute',  'noisy',  'purring',  'quiet',  'raspy',  'resonant',  'screeching',  'shrill','ancient',  'brief',  'early',  'fast',  'future',  'late',  'long',  'modern',  'old',  'old-fashioned',  'prehistoric',  'quick',  'rapid',  'short',  'slow',  'swift',  'young','ancient','brief',  'early',  'fast',  'future',  'late',  'long',  'modern',  'old',  'old-fashioned',  'prehistoric',  'quick',  'rapid',  'short',  'slow',  'swift',  'young']
nouns = ["Tiger", "Dragon", "Wolf", "Eagle", "Lion", "Panther", "Shark", "Falcon", "Bear", "Phoenix",'Avatar','Quest','Level',  'Achievement',  'Leaderboard',  'Profile',  'Challenge',  'Gamer',  'Guild',  'Team',  'Battle',  'Arena',  'Trophy',  'Badge',  'Friend',  'Score',  'Mission',  'World',  'Game',  'Platform',  'Stream',  'Post',  'Content',  'Follower',  'Comment',  'Chat',  'Emoji',  'Reaction',  'Feed','Streamer']
def generate_username(length=15, add_numbers=False, add_special_chars=False):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    if add_numbers:
        number = str(random.randint(1, 9999))
        adjective += number  
    if add_special_chars:
        special_char = random.choice(string.punctuation)
        noun += special_char  
    username = adjective + noun
    if len(username) > length:
        username = username[:length]
    return username
def save_usernames_to_file(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to {filename}")
def main():
    print("Welcome to the Username Generator!")
    length = int(input("Enter desired username length (default is 15): ") or 15)
    add_numbers = input("Include numbers in username? (yes/no): ").lower() == "yes"
    add_special_chars = input("Include special characters in username? (yes/no): ").lower() == "yes"
    num_usernames = int(input("How many usernames would you like to generate? "))
    usernames = [generate_username(length, add_numbers, add_special_chars) for _ in range(num_usernames)]
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)
    save_option = input("Do you want to save these usernames to a file? (yes/no): ").lower()
    if save_option == "yes":
        save_usernames_to_file(usernames)
if __name__ == "__main__":
    main()
