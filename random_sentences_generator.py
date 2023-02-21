import random


# Function for bold text in program guidelines
def bold_text(string):
    return "\033[1m" + string + "\033[0m"


# Function for getting random words
def get_random_word(words):
    return random.choice(words)


# Function for add word in some of sentence parts
def add_word(choice, word):
    is_successful = True
    if choice.lower() == "name":
        if word not in names:
            names.append(word)
        else:
            is_successful = False
    elif choice.lower() == "city":
        if word not in cities:
            cities.append(word)
        else:
            is_successful = False
    elif choice.lower() == "verb":
        if word not in verbs:
            verbs.append(word)
        else:
            is_successful = False
    elif choice.lower() == "detail":
        if word not in details:
            details.append(word)
        else:
            is_successful = False
    elif choice.lower() == "adverb":
        if word not in adverbs_frequency:
            adverbs_frequency.append(word)
        else:
            is_successful = False
    else:
        is_successful = False

    return is_successful


# Input for sequence of names
names = input("Add names, separating with space:").split()

# Lists with words for sentences
cities = ["London", "Paris", "Sofia", "Istanbul", "New York", "Dubai", "Mexico", "Berlin", "Rome"]
verbs = ["travels", "walks", "sleeps", "works", "plays", "loves", "goes"]
details = ["with a bus", "on a beach", "in the bed", "at home", "with a guitar", "to eat", "outside"]
adverbs_frequency = ["every day", "ones a week", "in the morning", "every night", "twice a day", "on Sundays"]

question_for_start = input(f"Do you want to start random sentences generator? {bold_text('[Y/N]')}")

while question_for_start.lower() != "n":
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

            click = input(f"Click {bold_text('[Enter]')} to generate a new one, {bold_text('[+]')} to add some word "
                          f"or press {bold_text('[N]')} to stop the generator.")

            if click == "+":
                print(f"The sentence contains a {bold_text('name')} of person, a {bold_text('city')}, "
                      f"a {bold_text('verb')}, a {bold_text('detail')} and an {bold_text('adverb')}.")
                input_choice = input("What kind of word you want to add?")
                input_word = input("And the word is:")

                result = add_word(input_choice, input_word)

                if result:
                    print("You add a word successfully. See the new sentence.")
                else:
                    print("Something goes wrong.")
                    question_for_start = input(f"Do you want to start again? {bold_text('[Y/N]')}")
                    break

            elif click.lower() == "n":
                exit(0)

    else:
        print("Invalid input. Try again...")
        question_for_start = input(f"Press {bold_text('[Y/N]')}:")
