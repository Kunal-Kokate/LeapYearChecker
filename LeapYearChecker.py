import calendar


print("Leap Year Checker. (q to quit program)")
while(True):

    x = input("Enter a year to see if it is a leap year: ")
    if x.isdigit():
            x = int(x)
            if calendar.isleap(x) == True:
                 print(f"{x} is a leap year")
            elif calendar.isleap(x) == False:
                 print(f"{x} is not a leap year")
    elif x == 'q':
          break
    else:
          print("Enter a year")
                 


