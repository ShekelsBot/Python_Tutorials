def pigLatin (string1):
    words=string1.split() # Split word array into letters
    l_words=string1.lower().split() # Make everything lowecase
    pig_latin=[] # Make new empty array for pig latin transaltion
    
    for word in l_words:
        if word[0] in 'aeiou': # Search array for letters AEIOU
            pig_latin.append(word+'way') # Add WAY if found
        else:
            vowel_pos=0 # Counter
            for w in word: # Go though array
                if w in 'aeiou': # If vlaue matches
                    vowel_pos=word.index(w) #Write index position
                    break
                else:
                    pass
            pig_latin.append(word[vowel_pos:]+word[:vowel_pos]+'ay') #Convert word to piglatin
    
    for i in range (0,len(words)-1):
        if words[i].istitle():
            pig_latin[i]=pig_latin[i].title()
    
    print("Pig Latin Version is: "+" ".join(pig_latin))

pigLatin("shark")
pigLatin("Ant")
pigLatin("Cat")

