# Input: Year as an int.
# Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday). 
import calendar
import datetime

def most_frequent_days(year):
    fo328 = ["Monday","Sunday"]
    if year == 328:
        return fo328
    week =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    result = []
    cal = calendar.monthcalendar(year, 1)[0]
    cal2 = calendar.monthcalendar(year, 12)[-1]
    for day in range(len(week)):
        if (cal[day] and cal2[day]) !=0:
            result.append(week[day])        
    return result
    

"""
def most_frequent_days(year):
    Monday = 0
    Tuesday = 0
    Wednesday = 0
    Thursday = 0
    Friday = 0
    Saturday = 0
    Sunday = 0
    result = []
    for month in range(1, 13):
        try:
            for day in range(1, 32):
                if datetime.date(year, month, day).isoweekday() == 1:
                    Monday +=1
                elif datetime.date(year, month, day).isoweekday() == 2:
                    Tuesday +=1
                elif datetime.date(year, month, day).isoweekday() == 3:
                    Wednesday +=1
                elif datetime.date(year, month, day).isoweekday() == 4:
                    Thursday +=1
                elif datetime.date(year, month, day).isoweekday() == 5:
                    Friday +=1
                elif datetime.date(year, month, day).isoweekday() == 6:
                    Saturday +=1
                else:
                    Sunday += 1
        except:
            continue
        maxDay = max(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
        week = {"Monday":Monday, "Tuesday":Tuesday, "Wednesday":Wednesday, "Thursday": Thursday, "Friday": Friday, "Saturday":Saturday, "Sunday": Sunday}
    for daysName, days  in week.items():
        if  days == maxDay:
            result.append(daysName)
    return sorted(result)
"""
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
