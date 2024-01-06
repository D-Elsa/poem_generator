import random
from nltk.corpus import wordnet as wn

def get_words():
    word_list = list(wn.words())
    return word_list

def generate_poem(word_list, style, specific_style):
    poem = ""

    if style == "sonnet":
        for _ in range(14):
            poem += get_line_with_figures(word_list, style, specific_style) + "\n"
    elif style == "haiku":
        for _ in range(3):
            poem += get_line_with_figures(word_list, style, specific_style) + "\n"
    else:
        for _ in range(10):
            poem += get_line_with_figures(word_list, style, specific_style) + "\n"

    return poem

def get_line_with_figures(word_list, style, specific_style):
    word1 = random.choice(word_list)
    word2 = random.choice(word_list)

    line = word1 + " is like " + word2

    selected_figure = specific_style.upper() if specific_style else "NONE"

    if selected_figure != "NONE":
        if selected_figure == "ALLITERATION":
            line += "\n" + generate_alliteration(word_list)
        elif selected_figure == "ASSONANCE":
            line += "\n" + add_assonance(word1, word2)
        elif selected_figure == "ANAPHORA":
            line += "\n" + add_anaphora(word1)
        elif selected_figure == "METAPHOR":
            line += "\n" + add_metaphor(word1, word2)
        elif selected_figure == "PERSONIFICATION":
            line += "\n" + add_personification(word1)
    else:
        line += "\n" + add_metaphor(word1, word2)

    return line

def generate_alliteration(word_list):
    initial_sound = random.choice([sound for sound in set(w[0] for w in word_list if w)]).lower()
    line = " ".join([word for word in word_list if word.lower().startswith(initial_sound)])
    return line

def add_assonance(word1, word2):
    return f"{word1} and {word2} sing in harmony."

def add_anaphora(word):
    return f"{word} brings joy. {word} brings peace. {word} brings love."

def add_metaphor(word1, word2):
    return f"{word1} is a journey, and {word2} is the destination."

def add_personification(word):
    return f"The stars whispered secrets to the moon, and the moon listened intently."

def main():
    word_list = get_words()

    print("Bienvenue dans le générateur de poèmes en Python!")

    style = input("Choisissez le style de poème (sonnet, haiku, libre) : ").lower()

    if style not in ["sonnet", "haiku", "libre"]:
        print("Style de poème non pris en charge. Veuillez choisir parmi les styles disponibles.")
        return

    specific_style = input("Choisissez la figure de style de poème (alliteration, assonance, anaphora, metaphor, personification) ou 'None' si aucune figure : ").lower()

    poem = generate_poem(word_list, style, specific_style)

    print("\nVotre poème généré:")
    print(poem)

if __name__ == "__main__":
    main()
