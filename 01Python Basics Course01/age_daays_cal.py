def caldays(m1,d1,m2,d2):
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sumday=0
    if(daysOfMonths[m1-1]<d1):
       sumday =sumday+(d1-daysOfMonths[m1-1])
    else:
        sumday =sumday+(daysOfMonths[m1-1]-d1)
        
    print("sumday ==")
    print(sumday)
    
    if(daysOfMonths[m2-1]<d2):
       sumday =sumday+d2+(d2-daysOfMonths[m2-1])
    else:
       sumday =sumday+d2+(daysOfMonths[m2-1]-d2)
        
    print("sumday ==")
    print(sumday)
    
    m1=m1+1
    m2=m2-1
    if m1<0 or m2<0:
        return sumday
    else:
        while(m1<m2):
            sumday=sumday+daysOfMonths[m1]
            m1=m1+1
    
    return (sumday)
        
        
       
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 365*(year2-year1)+(year2-year1)/4 
    print("days ==")
    print(days)
    if month1<month2:
        days=days+caldays(month1,day1,month2,day2)
    else:
        days=days+caldays(month2,day2,month1,day1)
        
    print("days ==")
    print(days)
    return days
    
    

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
