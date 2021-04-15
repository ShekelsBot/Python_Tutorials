#Function to check whether a character is a vowel or not
def char_isVowel(c): 
    vowel = ['A', 'E', 'I', 'O', 'U','a','e','i','o','u']
    if c in vowel:
        return True
    else:
        return False
  
#Function to convert a word to its PigLatin form
def pigLatin(s): 
    flag = False;
    vow_index = 0
    for i in range(len(s)): 
        if (char_isVowel(s[i])):
            vow_index = i
            flag = True; 
            break; 
    if (not flag): 
        return s; 
    pigLatin = s[vow_index:] + s[0:vow_index] + "ay"
    return pigLatin 


sentence = input("Enter a Sentence") #Initialising a sentence
list = sentence.split()#Splitting the sentence into a list consisting of its words

print("The original sentence is:-") #Printing the original sentence
print(sentence)

pig_str = "" #Initialising an empty string for forming the PigLatin sentence
for word in list: #Iterating over list
    pig_str += " " + pigLatin(word)

print("The piglatin sentence is:-") #Printing the PigLatin sentence
print(pig_str)