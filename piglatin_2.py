string1=input("Enter a Sentence: ").strip()
words=string1.split()
l_words=string1.lower().split()
pig_latin=[]
 
for word in l_words:
    if word[0] in 'aeiou':
        pig_latin.append(word+'way')
    else:
        vowel_pos=0
        for w in word:
            if w in 'aeiou':
                vowel_pos=word.index(w)
                break
            else:
                pass
        pig_latin.append(word[vowel_pos:]+word[:vowel_pos]+'ay')
 
for i in range (0,len(words)-1):
    if words[i].istitle():
        pig_latin[i]=pig_latin[i].title()
 
print("Pig Latin Version is: "+" ".join(pig_latin).strip())
