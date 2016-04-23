#  Input: A text for analysis as a string (unicode for py2.7).
#  Output: The most frequent letter in lower case as a string. 

def checkio(text):
    lowctext = text.lower() #переводит строку в нижний регистр
    txtonly = [] # создает пустой список
    counted = []
    ulist = []
    fdict = {}
    mlista = []
    strfsort = []
    strfresult = []
    for x in lowctext:
        if x.isalpha( ):  #проверяет является ли елемент буквой
             txtonly += x #если буква вносит в txtonly
    for x in txtonly:
        if txtonly.count(x):
            counted.append(txtonly.count(x))
    
    ulist = zip(txtonly, counted)
    fdict = dict(ulist)
    mlista = list(fdict.items())
    strfsort = str(sorted(mlista, key=lambda x: (-x[1], (x[0]))))
    for x in strfsort:
        if x.isalpha( ):
             strfresult += x
    
    return strfresult[0]
    




    
    

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
