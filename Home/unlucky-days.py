# Input: Year as an integer.
# Output: Number of Black Fridays in the year as an integer. 

import datetime
def checkio(year):
    count = 0
    day = 13
    for month in range(1, 13):
        if datetime.date(year, month, day).isoweekday() == 5:
            count +=1
    
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"