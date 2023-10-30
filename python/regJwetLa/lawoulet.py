import random
import pickle


def is_valid_username(username):
    return username.islower() and ' ' not in username

def get_user_score(username):
    try:
        with open("user_scores.pkl", "rb") as file:
            user_scores = pickle.load(file)
            if username in user_scores:
                return user_scores[username]
    except FileNotFoundError:
        return 0
    return 0

def update_user_score(username, score):
    try:
        with open("user_scores.pkl", "rb") as file:
            user_scores = pickle.load(file)
    except FileNotFoundError:
        user_scores = {}

    user_scores[username] = user_scores.get(username, 0) + score

    with open("user_scores.pkl", "wb") as file:
        pickle.dump(user_scores, file)

while True:
    username = input("Entrez votre pseudo (sans espaces, en minuscules): ")
    if is_valid_username(username):
        break
    else:
        print("Pseudo invalide. Veuillez entrer un pseudo en minuscules sans espaces.")

print(f"Bienvenue, {username}! Votre score actuel est {get_user_score(username)}")

min_number = 1
max_number = 5

while True:
    number_to_guess = random.randint(min_number, max_number)
    print(f"J'ai choisi un nombre secret entre {min_number} et {max_number}.")

    attempts = 3
    score = attempts * 30

    while attempts > 0:
        guess = input(f"Il vous reste {attempts} essais. Devinez le nombre secret : ")
        try:
            guess = int(guess)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if guess < min_number or guess > max_number:
            print(f"Veuillez entrer un nombre entre {min_number} et {max_number}.")
            continue

        attempts -= 1

        if guess == number_to_guess:
            print("BRAVO ! Vous avez deviné le nombre secret.")
            print(f"Votre score pour cette partie est : {attempts * 30}")
            update_user_score(username, attempts * 30)
            print(f"Votre score total est maintenant de : {get_user_score(username)}")
            break
        elif guess < number_to_guess:
            print("Le nombre secret est plus élevé. Réessayez.")
        else:
            print("Le nombre secret est plus bas. Réessayez.")

    else:
        print(f"Désolé, vous avez épuisé toutes vos tentatives. Le nombre secret était {number_to_guess}.")

    play_again = input("Voulez-vous jouer à nouveau (appuyez sur 'K' pour quitter) ? ")
    if play_again.lower() != 'k':
        continue
    else:
        print("Au revoir!")
        break
