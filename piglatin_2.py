def pig_it(text):
    words = text.split(" ")
    # Split sentence up
    new_words = []
    # Blank Array
    for word in words:
    # Parse Array
        if word.isalpha():
            new_word = word[1:] + word[0] + "ay"
            # Re-arrange word and add ay
            new_words.append(new_word)
        else:
            new_words.append(word)
         
         
    return " ".join(new_words)
    #Append new words together
print(pig_it('cat'))