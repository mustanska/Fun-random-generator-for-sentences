import random


# Function for getting random words
def get_random_word(words):
    return random.choice(words)


# Input for sequence of names
names = input("Add names, separating with space:").split()

# Lists with words for sentences
cities = ["London", "Paris", "Sofia", "Istanbul", "New York", "Dubai", "Mexico", "Berlin", "Rome"]
verbs = ["travels", "walks", "sleeps", "works", "plays", "loves", "goes"]
details = ["with a bus", "on a beach", "in the bed", "at home", "with a guitar", "to eat", "outside"]
adverbs_frequency = ["every day", "ones a week", "in the morning", "every night", "twice a day", "on Sundays"]

question_for_start = input("Do you want to start random sentences generator? [Y/N]")

if question_for_start.lower() == "y":
    # Loop for generating sentences
    while True:
        name = get_random_word(names)
        city = get_random_word(cities)
        verb = get_random_word(verbs)
        detail = get_random_word(details)
        adverb = get_random_word(adverbs_frequency)

        sentence = f"{name} from {city} {verb} {detail} {adverb}."
        print(sentence)

        click = input("Click [Enter] to generate a new one or press [N] to stop the generator.")

        if click.lower() == "n":
            break

else:
    exit(0)
