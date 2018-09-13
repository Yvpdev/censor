text = input("text: ")
word = input("word: ")
def censor(text, word):
    j = len(word)
    return( text.replace(word, j * "*"))
    

print (censor(text, word))



