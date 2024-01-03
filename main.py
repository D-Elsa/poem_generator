import random
import nltk

# Téléchargez la ressource "words" si elle n'est pas déjà présente
nltk.download('words')

def get_words():
    # Utilisation de la bibliothèque NLTK pour obtenir une liste de mots
    word_list = nltk.corpus.words.words()
    return word_list


def generate_poem(style, word_list):
    poem = ""

    if style == "sonnet":
        poem += generate_sonnet(word_list)
    elif style == "haiku":
        poem += generate_haiku(word_list)
    else:
        poem += generate_free_verse(word_list)

    return poem


def generate_sonnet(word_list):
    sonnet = ""
    for _ in range(14):
        sonnet += get_line_with_metaphor(word_list) + "\n"
    return sonnet


def generate_haiku(word_list):
    haiku = ""
    for _ in range(3):
        haiku += random.choice(word_list) + " "
    return haiku


def generate_free_verse(word_list):
    verse = ""
    for _ in range(10):
        verse += get_line_with_metaphor(word_list) + "\n"
    return verse


def get_line_with_metaphor(word_list):
    line = random.choice(word_list) + " is like " + random.choice(word_list)
    return line


def main():
    word_list = get_words()

    print("Bienvenue dans le générateur de poèmes en Python!")

    style = input("Choisissez le style de poème (sonnet, haiku, libre) : ").lower()

    if style not in ["sonnet", "haiku", "libre"]:
        print("Style de poème non pris en charge. Veuillez choisir sonnet, haiku ou libre.")
        return

    poem = generate_poem(style, word_list)

    print("\nVotre poème généré:")
    print(poem)


if __name__ == "__main__":
    main()
