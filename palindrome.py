"""
    Question 1: Write a Python program to check if a string is a palindrome.
    Not optimize with à, é, etc...
    Need to be optimze to avoid repetition
"""

def spliting_word(word_or_sentences):
    tab = []
    for i in word_or_sentences:
        tab.append(i)
    return tab

def spliting_sentence(sentences):
    reverse_simple = sentences[::-1]
    tab = ""
    for i in reverse_simple:
        tab += i[::-1]
    return tab

def joining_word(verse_tab, reverse_tab):
    first = "".join(verse_tab)
    second = "".join(reverse_tab)

    return first,second

def joining_sentence(sentence_normal, sentence_reverse):
    print(sentence_reverse)
            

def decision(tuple_words):
    if (tuple_words[0] == tuple_words[1]):
        return True
    return False

word_or_sentences = input("Entrez votre mot/phrase : ")
sentences_or_words = word_or_sentences.split()
if (len(sentences_or_words) <= 1):
    tab_word = spliting_word(word_or_sentences)
    reverse_tab_word = tab_word[::-1]    
    tuple_decision = joining_word(tab_word, reverse_tab_word)
    print(decision(tuple_decision))
else:
    tab_word = word_or_sentences.split(" ")
    reverse_word = spliting_sentence(tab_word)
    print(decision(("".join(tab_word).upper(), reverse_word.upper())))
    