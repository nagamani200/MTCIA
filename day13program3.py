def PrintSunday():
    print("Sunday")
    return
def PrintMonday():
    print("Monday")
def PrintTuesday():
    print("Tuesday")
        
def PrintWednesday():
    print("Wednesday")
def PrintThursday():
    print("Thursday")
def PrintFriday():
    print("Friday")
def PrintSaturday():
    print("Saturday")


     
def choice():
    print("Enter day number between 1-7")
    return
dayDict={ 1:PrintSunday , 2:PrintMonday ,3:PrintTuesday , 4:PrintWednesday ,
          4:PrintThursday ,5:PrintFriday ,6:PrintSaturday}

dayNo=int(input())
if dayNo>=1 and dayNo<=7:
    dayDict[dayNo]()
else:
    print("INVALID")
    
         
              
