#  Input: A text for analysis as a string.
#  Output: The most frequent letter in lower case as a string. 

def checkio(text):
    text= text.lower()
    splited_text = []
    for x in text:
        if x.isalpha():
            splited_text.append(x)
    counter = []
    for x in splited_text:
        counter.append(splited_text.count(x))
    text = list(dict(sorted(zip(splited_text, counter))).items())
    text = str(sorted(text, key=lambda x: (-x[1], (x[0]))))        
    return text[3]
    




    
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
