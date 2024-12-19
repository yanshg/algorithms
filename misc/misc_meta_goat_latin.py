'''
Goat Latin is a playful modification of the English language. The rules for transforming English words into Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, u):

Add "ma" to the end of the word.
Example: "apple" → "applema"
If a word begins with a consonant:

Move the first letter to the end of the word.
Add "ma" to the end of the word.
Example: "goat" → "oatma"
For each word, append a number of "a"s at the end equal to its position in the sentence (starting from 1):

First word gets one "a", the second word gets two "a"s, and so on.
Example: "The quick brown fox" → "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa"

'''

def get_goat_latin(s:str) -> str:
    vowels = "aeiou"
    words = s.strip().split()
    transformed_words = []

    for index, word in enumerate(words):
        if word[0] in vowels:
            word += 'ma'
        else:
            word = word[1:] + word[0] + 'ma'
        word += 'a' * (index+1)
        transformed_words += [ word ]
    
    return ' '.join(transformed_words)

s = " The quick brown fox "
print(get_goat_latin(s))