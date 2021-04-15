def first_last_match(sentence):
    length = len(sentence)
    if len(sentence) == 0:
        print ("False")
    elif len(sentence) == 1:
        print ("True")
    elif sentence[0] == sentence[length-1]:
        print ("True")
    else:
        print ("False")
first_last_match(sentence = input(""))

