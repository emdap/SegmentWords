
def extract():
    wordDoc = open('words.txt','r')

    words = ''

    for word in wordDoc:
        words+=word + ' '
    
    wordDoc = open('20k.txt', 'r')
    
    for word in wordDoc:
        if not(word.strip() in words):
            words+=word.strip() + ' '
 
    return words

