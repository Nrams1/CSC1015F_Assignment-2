# first day
# neo ramotlou
# 15 march 2018

Year = int(input('Enter the first year: \n'))
Y2 = int(input('Enter the second year: \n'))

for Year in range ( Year ,(Y2+1)):
    day = (Year - 1)%4
    day = 1 +5*day
    day = day +4*((Year-1)%100)
    day = day +6*((Year-1)%400)
    day = day%7
    
        
    if day ==0:                  
        day = 'Sunday.'
    elif day ==1:
        day = 'Monday.'
    elif  day ==2:
        day = 'Tuesday.'
    elif day ==3:
        day = 'Wednesday.'
    elif day ==4:
        day = 'Thursday.'
    elif day ==5:
        day = 'Friday.'
    elif day ==6:
        day = 'Saturday.'
    
    # for Y2 in range
    print ('The 1st of January', Year,'falls on a',day)
                  
                  