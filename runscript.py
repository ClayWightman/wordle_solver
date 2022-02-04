import json

def get_five_letter_words_from_dictionary():
    five_letter_words = {}
    with open('dictionary.json') as f:
        all_words = json.load(f)
        for word in all_words:
            if len(word) == 5:
                five_letter_words[word] = 0
    with open('five_letter_words.json', 'w') as f:
        json.dump(five_letter_words, f)


def get_weight_of_letters():
    letter_values = {'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0}
    with open('five_letter_words.json') as f:
        words = json.load(f)
        for word in words:
            for letter in word:
                letter_values[letter] += 1
    print(letter_values)
            
def get_weight_of_words_without_duplicate_letters():
    letter_weight = {'a': 8392, 'b': 2089, 'c': 2744, 'd': 2811, 'e': 7800, 'f': 1238, 'g': 1971, 'h': 2284, 'i': 5067, 'j': 376, 'k': 1743, 'l': 4246, 'm': 2494, 'n': 4043, 'o': 5219, 'p': 2299, 'q': 139, 'r': 5143, 's': 6537, 't': 4189, 'u': 3361, 'v': 878, 'w': 1171, 'x': 361, 'y': 2521, 'z': 474}
    words_with_weight = {}
    with open('five_letter_words.json') as f:
        words = json.load(f)
        for word in words:
            word_weight = 0
            for letter in set(word):
                word_weight += letter_weight[letter]
            words_with_weight[word] = word_weight
    with open('words_with_weight_without_duplicate_letters.json', 'w') as f:
        json.dump(words_with_weight, f)



def get_weight_of_words():
    letter_weight = {'a': 8392, 'b': 2089, 'c': 2744, 'd': 2811, 'e': 7800, 'f': 1238, 'g': 1971, 'h': 2284, 'i': 5067, 'j': 376, 'k': 1743, 'l': 4246, 'm': 2494, 'n': 4043, 'o': 5219, 'p': 2299, 'q': 139, 'r': 5143, 's': 6537, 't': 4189, 'u': 3361, 'v': 878, 'w': 1171, 'x': 361, 'y': 2521, 'z': 474}
    words_with_weight = {}
    with open('five_letter_words.json') as f:
        words = json.load(f)
        for word in words:
            word_weight = 0
            for letter in word:
                word_weight += letter_weight[letter]
            words_with_weight[word] = word_weight
    with open('words_with_weight.json', 'w') as f:
        json.dump(words_with_weight, f)


def get_best_starting_words():
    best_words = []
    with open('words_with_weight_without_duplicate_letters.json') as f:
        words = json.load(f)
        current_best = 0
        for word in words:
            word_value = words[word]
            if word_value == current_best:
                best_words.append(word)
            elif word_value > current_best:
                current_best = word_value
                best_words = [word]
    print(best_words)

def remove_words_without_exact_letter_match(words, index, letter):
    new_words = {}
    for word in words:
        if word[index] == letter:
            new_words[word] = words[word]
    return new_words


def remove_words_without_letter(words, letter):
    new_words = {}
    for word in words:
        if letter in word:
            new_words[word] = words[word]
    return new_words

def remove_words_with_letter(words, index, letter):
    new_words = {}
    for word in words:
        if word[index] != letter:
            new_words[word] = words[word]
    return new_words

def get_guess_word(words):
    current_best = 0
    guess_word = 'error couldnt find better guess word'
    for word in words:
        if words[word] >= current_best:
            current_best = words[word]
            guess_word = word
    return guess_word


def play_wordle():
    with open('words_with_weight.json') as f:
        words = json.load(f)
    turns = 0
    success_string = input("Input word 'arose' then input success values:")
    guess_word = 'arose'
    turns += 1

    while turns < 6 and success_string != '22222':
        if success_string == 'N':
            guess_word = get_guess_word(words)
        inx = 0
        for num in success_string:
            if num == '2':
                words = remove_words_without_exact_letter_match(words, inx, guess_word[inx])
            elif num == '1':
                words = remove_words_without_letter(words, guess_word[inx])
            elif num == '0':
                words = remove_words_with_letter(words, inx, guess_word[inx])
            inx += 1
        guess_word = get_guess_word(words)
        words.pop(guess_word)
        success_string = input(f"Input word #{guess_word} then input success values")
    print('congrats!  You found the word!')




#get_five_letter_words_from_dictionary()
#get_weight_of_letters()
#get_weight_of_words_without_duplicate_letters()
#get_weight_of_words()
#get_best_starting_words()
play_wordle()