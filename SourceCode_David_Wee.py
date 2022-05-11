#DAVID WEE MING JUNN

def Login():
  print ("Please write down your Status.(Admin/Student)")
  Status = input("Status:   ")

  if (Status == "Student"):
    print("")
    return 10

  User_ID = input("ID:       ")
  Password = input("Password: ")

  if (Status == "Admin"):
    for x in Admin_Details:
      if x[1] == User_ID:
        for y in Admin_Details:
          if y[2] == Password:
            return 0
        break
  print("\nError, wrong details.\n")
  return -2



def Display(g):
  listing = 1
  if g == 10:
    print("   %-14s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s" %
      ("Coach Name", "Coach ID", "Pay/hr", "Phone No", "Sport Centre","Sport Name", "Rating", "Address", "Date Joined", "Date Left"))
    #number listing and printing data
    for x in Coach_Details:
      count = -1
      print("%4s." % str(listing),end = "")
      listing += 1
      for y in x:
        count += 1
        if count == 2:
          continue
        print("%-12.12s" % y, end = " ")
      print("")
    print("")

  elif g == 20:
    print("   %-14s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Student Name","Student ID", "Phone No", "Sport Centre", "Date Joined", "Date Left", "Emergency No", "Code", "Coach Rating"))
    for x in Student_Details:
      count = -1
      print("%4s." % str(listing),end = "")
      listing += 1
      for y in x:
        count +=1
        if count == 2:
          continue
        print("%-12.12s" % y, end = " ")
      print("")
  
  elif g == 30:
    print("   %-14s %-12s %-12s" % ("Sport Name","Sport ID","Sport Fee"))
    for x in Sport_Details:
      print("%4s." % str(listing),end = "")
      listing += 1
      for y in x:
        print("%-12.12s" % y, end = " ")
      print("")
  
  elif g == 40:
    print("   %-14s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Sport Centre","Sport Name", "Start Time", "End Time", "Coach Name", "Code", "Day"))
    for x in Sport_Schedule:
      print("%4s." % str(listing),end = "")
      listing += 1
      for y in x:
        print("%-12.12s" % y, end = " ")
      print("")
      


def Configure(g):
  print("Which number was it?")
  num = int(input("Number: "))
  if g == 11:
    #Entering listing number from display.
    while (num > len(Coach_Details) or num < 1):
      print("Please enter a valid number between 1 -",len(Coach_Details))
      num = int(input("Valid number: "))
    num -= 1
    print("%-14s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Coach Name", "Coach ID", "Password", "Pay/hr", "Phone No", "Sport Centre","Sport Name", "Rating", "Address", "Date Joined", "Date Left"))
    print("1.",end = "")
    for x in Coach_Details[num]:
      print("%-12.12s" % x, end = " ")
    print("\n\nWhat do you wish to configure?")
    print("Coach Name = 1, Coach ID = 2, Password =3 ...etc")
    print("Rating = 8 can't be configured.")
    category = int(input("What will the number be?: "))
    while (category > 11 or category < 1 or category == 8):
      category = int(input("Number must be within 1 and 11: "))
    category -= 1
    print("Changing ",Coach_Category[category]," ",Coach_Details[num][category],end =" ")
    string = input("to ...: ")
    #Changing element and withhold element replaced.
    while (len(string) > 12):
      string = input("Try again, must be under 12 characters: ")
    insurance = Coach_Details[num][category]
    Coach_Details[num][category] = string
    confirm = input("Is this the result you wanted? Y/N: " )
    while (confirm != "Y" and confirm != "N"):
      confirm = input("Wrong value entered, please enter Y or N: ")
    if confirm == "Y":
      del insurance
      #Code under is display after conf.
      print("%-14s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Coach Name", "Coach ID","Password", "Pay/hr", "Phone No", "Sport Centre","Sport Name", "Rating", "Address", "Date Joined", "Date Left"))
      print("1.",end = "")
      for x in Coach_Details[num]:
        print("%-12.12s" % x, end = " ")
      print("\n")
    elif confirm == "N":
      Coach_Details[num][category] = insurance
      print("The changes has been reverted.")
    

  if g == 21:
    while (num > len(Student_Details) or num < 1):
      print("Please enter a valid number between 1 -",len(Student_Details))
      num = int(input("Valid number: "))
    num -= 1
    print("%-14s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Student Name","Student ID", "Password", "Phone No", "Sport Centre", "Date Joined", "Date Left","Emergency No","Code","Coach Rating"))
    print("1.",end = "")
    for x in Student_Details[num]:
      print("%-12.12s" % x, end = " ")
    print("\n\nWhat do you wish to configure?")
    print("Student Name = 1, Student ID = 2, Password = 3 ...etc")
    category = int(input("What will the number be?: "))
    while (category > 10 or category < 1):
      category = int(input("Number must be within 1 and 10: "))
    category -= 1
    print("Changing ",Student_Category[category]," ",Student_Details[num][category],end =" ")
    string = input("to ...: ")
    while (len(string) > 12):
      string = input("Try again, must be under 12 characters: ")
    insurance = Student_Details[num][category]
    Student_Details[num][category] = string
    confirm = input("Is this the result you wanted? Y/N: " )
    while (confirm != "Y" and confirm != "N"):
      confirm = input("Wrong value entered, please enter Y or N: ")
    if confirm == "Y":
      del insurance
      #below is Display
      print("%-14s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Student Name","Student ID", "Password", "Phone No", "Sport Centre", "Date Joined", "Date Left","Emergency No","Code","Coach Rating"))
      print("1.",end = "")
      for x in Student_Details[num]:
        print("%-12.12s" % x, end = " ")
      print("\n")
    elif confirm == "N":
      Student_Details[num][category] = insurance
      print("The changes has been reverted.")

  if g == 31:
    while (num > len(Sport_Details) or num < 1):
      print("Please enter a valid number between 1 -",len(Sport_Details))
      num = int(input("Valid number: "))
    num -= 1
    print("%-14s %-12s %-12s" % ("Sport Name","Sport ID","Sport Fee"))
    print("1.",end = "")
    for x in Sport_Details[num]:
      print("%-12.12s" % x, end = " ")
    print("\n\nWhat do you wish to configure?")
    print("Sport Name = 1, Sport ID = 2, Sport Fee = 3")
    category = int(input("What will the number be?: "))
    while (category > 3 or category < 1):
      category = int(input("Number must be within 1 and 3: "))
    category -= 1
    print("Changing ",Sport_Category[category]," ",Sport_Details[num][category],end =" ")
    string = input("to ...:")
    while (len(string) > 12):
      string = input("Try again, must be under 12 characters: ")
    insurance = Sport_Details[num][category]
    Sport_Details[num][category] = string
    confirm = input("Is this the result you wanted? Y/N: " )
    while (confirm != "Y" and confirm != "N"):
      confirm = input("Wrong value entered, please enter Y or N: ")
    if confirm == "Y":
      del insurance
      print("%-14s %-12s %-12s" % ("Sport Name","Sport ID","Sport Fee"))
      print("1.",end = "")
      for x in Sport_Details[num]:
        print("%-12.12s" % x, end = " ")
    elif confirm == "N":
      Sport_Details[num][category] = insurance
      print("The changes has been reverted.")

  if g == 41:
    while (num > len(Sport_Schedule) or num < 1):
      print("Please enter a valid number between 1 -",len(Sport_Schedule))
      num = int(input("Valid number: "))
    num -= 1
    print("%-14s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Sport Centre", "Sport Name","Start Time","End Time","Coach Name","Code","Day"))
    print("1.",end = "")
    for x in Sport_Schedule[num]:
      print("%-12.12s" % x, end = " ")
    print("\n\nWhat do you wish to configure?")
    print("Sport Centre = 1, Sport Name = 2, Start Time = 3")
    print("End Time = 4, Coach Name = 5, Code = 6 Day = 7")
    category = int(input("What will the number be?: "))
    while (category > 7 or category < 1):
      category = int(input("Number must be within 1 and 7: "))
    category -= 1
    print("\nChanging ",Sport_Table[category]," ",Sport_Schedule[num][category],end =" ")
    string = input("to ...:")
    while (len(string) > 12):
      string = input("Try again, must be under 12 characters: ")
    insurance = Sport_Schedule[num][category]
    Sport_Schedule[num][category] = string
    confirm = input("Is this the result you wanted? Y/N: " )
    while (confirm != "Y" and confirm != "N"):
      confirm = input("Wrong value entered, please enter Y or N: ")
    if confirm == "Y":
      del insurance
      print("%-14s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Sport Centre", "Sport Name","Start Time","End Time","Coach Name","Code","Day"))
      print("1.",end = "")
      for x in Sport_Schedule[num]:
        print("%-12.12s" % x, end = " ")
    elif confirm == "N":
      Sport_Schedule[num][category] = insurance
      print("The changes has been reverted.")
  print("")



def Search_Specific(g):
  count = 0
  found = 0
  if g == 12:
    print("Search Coach by Coach ID or Search Coach by rating or Search Coach ratings?")
    print("By Coach ID = 1 , Coach by Rating = 2 , Coach Ratings = 3")
    num = int(input("Enter a number: "))
    while (num < 1 or num > 3):
      num =int(input("Error, Please enter a number within 1 - 3 "))
    if num == 1:
      ID = input("Type in the Coach ID: ")
      while (len(ID) != 6):
        ID = input("ID only has 6 characters. Please try again: ")
      print("")
      #x[1] represents second element in each list in list.
      for x in Coach_Details:
        if x[1] == ID :
          found += 1
          break
        count += 1
      #count is for indexing
      if found == 1:
        for y in range(len(Coach_Details[count])):
          if y == 2:
            continue
          print(Coach_Category[y]," = ",Coach_Details[count][y])
        print("It is located",count+1,"in Display Coach.")
      else:
        print("Error, element not found.")

    elif num == 2:
      listing = 1
      mylist = []
      rate = int(input("Type in the Rating, integer of 0 - 5: "))
      while (rate < 0 or rate > 5):
        rate = int(input("Integer between 0 - 5. Please try again: "))
      print("")
 
      for x in Coach_Details:
        if x[7] == "N/A":
            continue
        if int(float(x[7])) == rate:
            found += 1
            mylist.append(count)
        count += 1

      if found >= 1:
        print("   %-14s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Coach Name", "Coach ID", "Pay/hr", "Phone No", "Sport Centre","Sport Name", "Rating", "Address", "Date Joined", "Date Left"))
        for x in mylist:
          add_up = -1
          #for numbering purpose
          print("%4s." % str(listing),end = "")
          listing += 1
          # add_up for skipping password
          for y in Coach_Details[x]:
            add_up += 1
            if add_up == 2:
              continue
            print("%-12.12s" % y, end = " ")
          print("")
      else:
        print("Error, element not found.")
    
    elif num == 3:
      found = 0
      listing = 1
      print("Please write down the name of the coach with no mistakes.")
      coach = input("Write down the name here: ")
      print("")
      for x in Feedback:
        if x[0] == coach:
          found += 1
          print (str(listing)+".", end = "")
          print (x)
          listing += 1
      if found > 0:
        print("End of feedback\n")
      elif found == 0:
        print("Wrong name inserted or feedback for coach is non-existent.")
      print("")



  if g == 22:
    listing = 1
    print("Search Student by Student ID.")
    ID = input("Please enter a Student ID: ")
    while (len(ID) < 1 or len(ID) > 6):
      ID = input("Error, Please enter a correct Student ID: ")
    print("")
    for x in Student_Details:
      if x[1] == ID:
        found += 1
        student = x[0]
        break
      count += 1
      
    if found == 1:
      for y in range(len(Student_Details[count])):
        if y == 2:
          continue
        print(Student_Category[y]," = ",Student_Details[count][y])
      print("It is located",count+1,"in Display Student.")
    else:
      print("Error, element not found.")

  if g == 32:
    listing = 1
    print("Search Sport by Sport ID. Exp: TT , BB , SW etc...")
    ID = input("Please enter a sport ID: ")
    while (len(ID) < 1 or len(ID) > 12):
      ID = input("Error, Please enter a correct Sport ID: ")
    print("")
    for x in Sport_Details:
      if x[1] == ID:
        found += 1
        sport = x[0]
        break
    if found == 1:
      print("   %-14s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Sport Centre","Sport Name", "Start Time", "End Time", "Coach", "Code", "Day"))
      for x in Sport_Schedule:
        if x[1] == sport:
          print("%4s." % str(listing),end = "")
          listing += 1
          for y in x:
            print("%-12.12s" % y, end = " ")
          print("")
    else:
      print("Error, Sport ID not found.")

def Sorting(g):
  if g == 13:
    print("Do you wish to sort Coaches in ascending order by Name , Pay/hr , Sport Centre , Sport Name or Rating?.")
    sort_num = int(input("Name = 1, Pay/hr = 2 , Sport Centre = 3, Sport Name = 4 , Rating = 5: "))
    while (sort_num < 1 or sort_num > 6):
      sort_num = int(input("Error, Please enter a number within 1 - 5: "))
    if sort_num == 1 :
      #for loop is used twice to ensure all is sorted.
      for x in range(len(Coach_Details)- 1):
        count = 0
        for x in range(len(Coach_Details) - 1):
          if Coach_Details[count][0] > Coach_Details[count+1][0]:
            Coach_Details[count],Coach_Details[count+1] = \
            Coach_Details[count+1],Coach_Details[count]
          count += 1
      print(Coach_Category[sort_num-1],"has been configured to ascending order.")

    if sort_num == 2 :
      for x in range(len(Coach_Details)- 1):
        count = 0
        for x in range(len(Coach_Details) - 1):
          if Coach_Details[count][3] > Coach_Details[count+1][3]:
            Coach_Details[count],Coach_Details[count+1] = \
            Coach_Details[count+1],Coach_Details[count]
          count += 1
      print(Coach_Category[sort_num + 1],"has been configured to ascending order.")
    
    if sort_num == 3 :
      for x in range(len(Coach_Details)- 1):
        count = 0
        for x in range(len(Coach_Details) - 1):
          if Coach_Details[count][5] > Coach_Details[count+1][5]:
            Coach_Details[count],Coach_Details[count+1] = \
            Coach_Details[count+1],Coach_Details[count]
          count += 1
      print(Coach_Category[sort_num + 2],"has been configured to ascending order.")
    
    if sort_num == 4 :
      for x in range(len(Coach_Details)- 1):
        count = 0
        for x in range(len(Coach_Details) - 1):
          if Coach_Details[count][6] > Coach_Details[count+1][6]:
            Coach_Details[count],Coach_Details[count+1] = \
            Coach_Details[count+1],Coach_Details[count]
          count += 1
      print(Coach_Category[sort_num + 2],"has been configured to ascending order.")
    
    if sort_num == 5 :
      for x in range(len(Coach_Details)- 1):
        count = 0
        for x in range(len(Coach_Details) - 1):
          if Coach_Details[count][7] > Coach_Details[count+1][7]:
            Coach_Details[count],Coach_Details[count+1] = \
            Coach_Details[count+1],Coach_Details[count]
          count += 1
      print(Coach_Category[sort_num + 2],"has been configured to ascending order.")
    Display(10)

  if g == 23:
    print("Do you wish to sort Students in ascending order by name or Sport Centre?")
    sort_num = int(input("Name = 1, Sport Centre = 2 : "))
    while (sort_num < 1 or sort_num > 2):
      sort_num = int(input("Error, Please enter a number within 1 - 2: "))
    if sort_num == 1 :
      for x in range(len(Student_Details)- 1):
        count = 0
        for x in range(len(Student_Details) - 1):
          if Student_Details[count][0] > Student_Details[count+1][0]:
            Student_Details[count],Student_Details[count+1] = \
            Student_Details[count+1],Student_Details[count]
          count += 1
      print(Student_Category[sort_num-1],"has been configured to ascending order.")
    
    if sort_num == 2 :
      for x in range(len(Student_Details)- 1):
        count = 0
        for x in range(len(Student_Details) - 1):
          if Student_Details[count][4] > Student_Details[count+1][4]:
            Student_Details[count],Student_Details[count+1] = \
            Student_Details[count+1],Student_Details[count]
          count += 1
      print(Student_Category[sort_num+2],"has been configured to ascending order.")
    Display(20)

  if g == 43:
    print("Sorting Sport_Schedule by Sport Centre or Start Time.")
    print("Sport Centre = 1 , Start Time = 2")
    sort_num = int(input("Choose a number: "))
    while (sort_num < 1 or sort_num > 2):
      sort_num = int(input("Error, please enter a number within 1 - 2 : "))
    if sort_num == 1:
      for x in range(len(Sport_Schedule)- 1):
        count = 0
        for x in range(len(Sport_Schedule) - 1):
          if Sport_Schedule[count][0] > Sport_Schedule[count+1][0]:
            Sport_Schedule[count],Sport_Schedule[count+1] = \
            Sport_Schedule[count+1],Sport_Schedule[count]
          count += 1
      print(Sport_Table[0],"has been configured to ascending order.")
    
    if sort_num == 2:
      for x in range(len(Sport_Schedule)- 1):
        count = 0
        for x in range(len(Sport_Schedule) - 1):
          if Sport_Schedule[count][2] > Sport_Schedule[count+1][2]:
            Sport_Schedule[count],Sport_Schedule[count+1] = \
            Sport_Schedule[count+1],Sport_Schedule[count]
          count += 1
      print(Sport_Table[2],"has been configured to ascending order.")
    Display(40)



def Add(g):
  print ("Attempting to add records...")
  my_list = []
  if g == 14:
    for x in range(11):
      print("For ",Coach_Category[x],end = " ")
      answer = input("is...:")
      while (len(answer) < 1 or len(answer) > 12):
        print("Error! Input has to be within the length of 1 to 12.")
        answer = input("Please enter an element.")
      my_list.append(answer)
    #creating an empty list and add element in it to later be added into a list.
    Coach_Details.append(my_list)
    print("This is what you have added.")
    print("%-14s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Coach Name", "Coach ID", "Password", "Pay/hr", "Phone No", "Sport Centre","Sport Name", "Rating", "Address", "Date Joined", "Date Left"))
    print("1.",end = "")
    #This takes the last list in the main list.
    num = len(Coach_Details) - 1
    for y in Coach_Details[num]:
      print("%-12.12s" % y, end = " ")
    print("\n")
    confirm = input("Is this the result you wanted? Y/N: " )
    while (confirm != "Y" and confirm != "N"):
      confirm = input("Wrong value entered, please enter Y or N: ")
    if confirm == "Y":
      pass
    elif confirm == "N":
      del Coach_Details[len(Coach_Details)-1]
      print("The changes has been reverted.")

  if g == 24:
    for x in range(10):
      print("For ",Student_Category[x],end = " ")
      answer = input("is...: ")
      while (len(answer) < 1 or len(answer) > 12):
        print("Error! Input has to be within the length of 1 to 12.")
        answer = input("Please enter an element.")
      my_list.append(answer)
    Student_Details.append(my_list)
    print("This is what you have added")
    print("%-14s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Student Name", "Student ID", "Password", "Phone No", "Sport Centre", "Date Joined", "Date Left", "Emergency No", "Code", "Coach Rating"))
    print("1.",end = "")
    num = len(Student_Details) - 1
    for y in Student_Details[num]:
      print("%-12.12s" % y, end = " ")
    print("\n")
    confirm = input("Is this the result you wanted? Y/N: " )
    while (confirm != "Y" and confirm != "N"):
      confirm = input("Wrong value entered, please enter Y or N: ")
    if confirm == "Y":
      pass
    elif confirm == "N":
      del Student_Details[len(Student_Details)-1]
      print("The changes has been reverted.")
  
  if g == 34:
    for x in range(3):
      print("For ",Sport_Category[x],end = " ")
      answer = input("is...: ")
      while (len(answer) < 1 or len(answer) > 12):
        print("Error! Input has to be within the length of 1 to 12.")
        answer = input("Please enter an element.")
      my_list.append(answer)
    Sport_Details.append(my_list)
    print("This is what you have added")
    print("%-14s %-12s %-12s" % ("Sport Name", "Sport ID", "Sport Fee"))
    print("1.",end = "")
    num = len(Sport_Details) - 1
    for y in Sport_Details[num]:
      print("%-12.12s" % y, end = " ")
    print("\n")
    confirm = input("Is this the result you wanted? Y/N: " )
    while (confirm != "Y" and confirm != "N"):
      confirm = input("Wrong value entered, please enter Y or N: ")
    if confirm == "Y":
      pass
    elif confirm == "N":
      del Sport_Details[len(Sport_Details)-1]
      print("The changes has been reverted.")

  if g == 44:
    for x in range(7):
      print("For ",Sport_Table[x],end = " ")
      answer = input("is...: ")
      while (len(answer) < 1 or len(answer) > 12):
        print("Error! Input has to be within the length of 1 to 12.")
        answer = input("Please enter an element.")
      my_list.append(answer)
    Sport_Schedule.append(my_list)
    print("This is what you have added")
    print("%-14s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Sport Centre", "Sport Name", "Start Time", "End Time", "Coach Name","Code","Day"))
    print("1.",end = "")
    num = len(Sport_Schedule) - 1
    for y in Sport_Schedule[num]:
      print("%-12.12s" % y, end = " ")
    print("\n")
    confirm = input("Is this the result you wanted? Y/N: " )
    while (confirm != "Y" and confirm != "N"):
      confirm = input("Wrong value entered, please enter Y or N: ")
    if confirm == "Y":
      pass
    elif confirm == "N":
      del Sport_Schedule[len(Sport_Schedule)-1]
      print("The changes has been reverted.")



'''
Main Codes for Admin ends here
-------------------------------------------------------------------
'''

#Display sport details for ALL_Students
def All_Sport():
    Display(30)

#Schedule available for all student
def All_Schedule():
  mylist = []
  listing = 0
    #Code below sort by start time, sorting can be used but it needs extra input from user.
  for x in range(len(Sport_Schedule)- 1):
    count = 0
    for x in range(len(Sport_Schedule) - 1):
      if (Sport_Schedule[count][2] > Sport_Schedule[count+1][2]):
        Sport_Schedule[count],Sport_Schedule[count+1] = \
        Sport_Schedule[count+1],Sport_Schedule[count]
      count += 1

  #below is find prime sport centres
  for x in Sport_Schedule:
    if x[0] in mylist:
      continue
    mylist.append(x[0])
  for y in mylist:
    listing += 1
    print(str(listing) + "."+y, end = " ")
  print("\n")
  #Choosing,picking and display depending on sport centre.
  print("Which Sport Centre are you interested in?")
  place = int(input("Please enter a number: "))
  while (place < 1 or place > listing):
    print("Error, Please enter a number between 1 - ",listing,".")
    place = int(input("Please enter a number."))

  print("   %-14s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Sport Centre","Sport Name", "Start Time", "End Time", "Coach Name", "Code","Day"))
  listing = 1
  for z in Sport_Schedule:
    if z[0] == mylist[place-1]:
      print("%4s." % str(listing),end = "")
      listing += 1
      for q in z:
        print("%-12.12s" % q, end = " ")
      print("")
  print("")
          

#Registration for new students
def Reg_Student():
  my_list = []
  count = -1
  for x in range(10):
    # skipping two category/two input.
    count += 1
    if (count == 1 or count == 5 or count == 6 or  count == 8 or count == 9):
      my_list.append("N/A")
      continue
    confirm = "N"
    while (confirm == "N"):
      print(Student_Category[x],end = " ")
      answer = input("is...: ")
      while (len(answer) < 1 or len(answer) > 12):
        print("Input has not been saved. Input has to be within the length of 1 to 12.")
        #Providing flexibility with confirmation each element.
        answer = input("Please enter an element.")
      confirm = input("Confirm? (No typo or mistakes?) Y/N: " )
      while (confirm != "Y" and confirm != "N"):
        confirm = input("Wrong value entered, please enter Y or N: ")
      
    my_list.append(answer)
  Student_Details.append(my_list)
  print("This is what you have added")
  print("%-14s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Student Name", "Student ID", "Password", "Phone No", "Sport Centre", "Date Joined", "Date Left", "Emergency No","Code","Rating"))
  print("1.",end = "")
  num = len(Student_Details) - 1
  for y in Student_Details[num]:
    print("%-12.12s" % y, end = " ")
  print("\n")
  confirm = input("Is this the correct information? Y/N: " )
  while (confirm != "Y" and confirm != "N"):
    confirm = input("Wrong value entered, please enter Y or N: ")
  if confirm == "Y":
    print("Please take note, your ID is temporary \"-> N/A <-\"")
  elif confirm == "N":
    del Student_Details[len(Student_Details)-1]
    print("The changes has been reverted.")

#Student login for Students
#Main_ID created in main for log in students loop.
def Student_Login():
  print("Please enter your ID and Password. (Admin / Student) ")
  User_ID = input("ID:       ")
  Password = input("Password: ")
  for x in Student_Details:
    if x[1] == User_ID:
      for y in Student_Details:
        if y[2] == Password:
          return 20 , User_ID
  print ("\nError, wrong details.\n")
  return 10 , "N/A"
  


'''
Main All_Student codes end here
----------------------------------------------------------------
'''


def Find_Self():
  for x in Student_Details:
    if main_id == x[1]:
      break
    
  return x

def View_Coach():
  my_list = []
  listing = 0
  for x in Coach_Details:
    if x[0] in my_list:
      continue
    my_list.append(x[0])
  for y in my_list:
    listing += 1
    print(str(listing) + "."+y, end = " ")
  print("\n")
  print ("Please choose a Coach to view his/her details.")
  num = int(input("Please enter a number: "))
  while (num < 0 or num > len(Coach_Details)):
    print ("Error, number must be between 1 - ",len(Coach_Details))
    num = int(input("Please enter a number: "))
  print("   %-14s %-12s %-12s %-12s %-12s %-12s" % ("Coach Name", "Coach ID", "Sport Centre","Sport Name", "Rating", "Date Joined"))
  num -= 1
  listing = 1
  #Display not important parts
  count = -1
  print("   1.",end = "")
  listing += 1
  for y in Coach_Details[num]:
    count += 1
    if count == 2 or count == 3 or count == 4 or count == 8 or count == 10:
      continue
    print("%-12.12s" % y, end = " ")
  print("")
  #print all feedbacks of said coach.
  print("\nDisplayed below are feedbacks and ratings from students.\n")
  listing = 1
  count = -1
  for z in Feedback:
    if z[0] == my_list[num]:
      print (str(listing)+".", end = "")
      print (z[1]," ",z[2])
      listing += 1
  print("End of feedback\n")
  

#Display student's details
def View_Self():
  listing = 0
  for y in Student_Category:
    print("%-12s %-3s" % (y," : "), end = "")
    print(user_list[listing])
    listing += 1
    print("")


#find out what the student wants to modify.  
def Modify_Self():
  listing = 1
  found = 0
  print("What do you wish to modify?\n")
  for x in Student_Category:
    print ("%-2s." % listing,end = "")
    print (x)
    listing += 1
  print("")
  print("2, 6, 7, 9, 10 can't be configured.")
  category = int(input("Please enter a number: "))
  while (category < 1 or category > 8 or category == 2 or category == 6 or category == 7):
    category = int(input("Error, please enter a number within 1 - 8: "))
  category -= 1
  #search for list

  print("Changing ",Student_Category[category]," from",user_list[category],"to :",end = "")
  string = input("")
  while (len(string)< 1 or len(string)> 12):
    print("Error, must be more than 0 and less than 13 characters.")
    string = input("Please enter another element.")
  #replace,display
  insurance = user_list[category]
  user_list[category] = string
  print("")
  View_Self()

  confirm = input("Is this what you wanted? Y/N :  ")
  while (confirm != "Y" and confirm != "N"):
    confirm = input("Error, please enter Y or N. : ")
  if confirm == "Y":
    print("Changes has been done.")
  if confirm == "N":
    print("Changes has been reverted.")
    user_list[category] = insurance



def Self_Schedule():
  listing = 1
  print("   %-14s %-12s %-12s %-12s %-12s %-12s %-12s" % ("Sport Centre","Sport Name", "Start Time", "End Time", "Coach Name", "Code", "Day"))
  for x in Sport_Schedule:
    if user_list[8] == x[5]:
      print("%4s." % str(listing),end = "")
      listing += 1
      for y in x:
        print("%-12.12s" % y, end = " ")
      print("\n")



def Rate_Coach():
  #display if feedback has been given before.
  for z in Feedback:
    if z[3] == main_id:
      print("The following is your current feedback and rating.\n")
      print(z,"\n")
      break

  mylist = []
  proceed = 0
  for x in Sport_Schedule:
    if x[5] == user_list[8]:
      proceed = 1
      coach_name = x[4]
      print("What feedback would you like to give to your coach? , "+ coach_name + "?")
      string = input("Write down your feedback here: ")
      while (len(string) < 0 or len(string) > 200):
        print("Please limit your feedback to 200 characters.")
        string = input("Please write down your feedback: ")
      print("\nWhat rating do you want to give to your coach? ,"+coach_name +". ")
      rating = float(input("Write down the rating here, rating must be 5 and less: (Only 2 decimals max): "))
      #only receive two decimal digits.
      while (rating < 1 or rating > 5):
        print("Error rating must be 1 - 5.")
        rating = input("Write down your rating here: ")
      endrating = ""
      #to have rating with len(4)
      for i in str(rating):
        if len(endrating) == 4:
          break
        endrating += i
      mylist.append(coach_name)
      mylist.append(string)
      mylist.append(endrating)
      mylist.append(user_list[1])

      #limit one feedback per student, check if student has already gave a feedback.
      found = 0
      count = 0
      for y in Feedback:
        if y[3] == main_id:
          found += 1
          break
        count += 1

      if found == 0:
        Feedback.append(mylist)
        print("Your rating and feedback have been updated.\n")
        break
      elif found > 0:
        Feedback[count] = mylist
        print("Your rating and feedback have been updated.\n")
        break
  #update coach rating on student details
  if proceed == 1:
    user_list[9] = str(rating)
  #update average rating
    total = 0.0
    count = 0
    for y in Feedback:
      if y[0] == coach_name:
        total += float(y[2])
        count += 1
    iniaverage = total / count
    endaverage = ""
    #make average less than len(4)
    for i in str(iniaverage):
      if len(endaverage) == 4:
        break
      endaverage += i
    
    for z in Coach_Details:
      if z[0] == coach_name:
        z[7] = str(endaverage)
  elif proceed == 0:
    print("Error, you have not been assigned to a coach.")


'''
-------------------Login Students code --------------------
'''


#Opening file and getting details
def Access_File():
  data = ["Admin_Details","Coach_Category","Coach_Details","Student_Category","Student_Details","Sport_Category","Sport_Details","Sport_Table","Sport_Schedule","Feedback"]
  file = open("text.txt","r+")
  count = 0
  for line in file:
    if line == "\n":
      continue
    line = line.rstrip("\n")
    if count < 10:
      if line.startswith(data[count]):
        count += 1
        continue
    mylist = line.split(",")
    for i in mylist:
      if i == "":
        mylist.remove(i)
    if count == 1:
      Admin_Details.append(mylist)
    elif count == 2:
      for x in mylist:
        Coach_Category.append(x)
    elif count == 3:
      Coach_Details.append(mylist)
    elif count == 4:
      for x in mylist:
        Student_Category.append(x)
    elif count == 5:
      Student_Details.append(mylist)
    elif count == 6:
      for x in mylist:
        Sport_Category.append(x)
    elif count == 7:
      Sport_Details.append(mylist)
    elif count == 8:
      for x in mylist:
        Sport_Table.append(x)
    elif count == 9:
      Sport_Schedule.append(mylist)
    elif count == 10:
      Feedback.append(mylist)
  file.close()




def Enter_File():
  count = -1
  data = ["Admin_Details","Coach_Category","Coach_Details","Student_Category","Student_Details","Sport_Category","Sport_Details","Sport_Table","Sport_Schedule","Feedback"]
  file = open("text.txt","w+")
  for x in data:
    file.write(x)
    file.write("\n")
    count += 1
    if count == 0:
      for y in Admin_Details:
        for z in y:
          file.write(z)
          file.write(",")
        file.write("\n")
      file.write("\n")
    if count == 1:
      for y in Coach_Category:
        file.write(y)
        file.write(",")
      file.write("\n\n")
    if count == 2:
      for y in Coach_Details:
        for z in y:
          file.write(z)
          file.write(",")
        file.write("\n")
      file.write("\n")
    if count == 3:
      for y in Student_Category:
        file.write(y)
        file.write(",")
      file.write("\n\n")
    if count == 4:
      for y in Student_Details:
        for z in y:
          file.write(z)
          file.write(",")
        file.write("\n")
      file.write("\n")
    if count == 5:
      for y in Sport_Category:
        file.write(y)
        file.write(",")
      file.write("\n\n")
    if count == 6:
      for y in Sport_Details:
        for z in y:
          file.write(z)
          file.write(",")
        file.write("\n")
      file.write("\n")
    if count == 7:
      for y in Sport_Table:
        file.write(y)
        file.write(",")
      file.write("\n\n")
    if count == 8:
      for y in Sport_Schedule:
        for z in y:
          file.write(z)
          file.write(",")
        file.write("\n")
      file.write("\n")
    if count == 9:
      for y in Feedback:
        for z in y:
          file.write(z)
          file.write(",")
        file.write("\n")
      file.write("\n")
  file.close()
      
#Main Admin guide
def Admin():
  print("What do you wish to do? Key in an action number.")
  print("10 = Coach , 20 = Student \n30 = Sport , 40 = Sport Schedules, Exit = -1")
  print("Display = +0 / Configure = +1 / Search by Specific Category = +2 / Sort Display = +3 / Add Record = +4.\n")
  #Please display before configuration.
  print("Please display before configuration.")
  print("Action numbers not available = 33, 42")
  num = int(input("Please enter an action number: "))
  print("")
  return num

#Main All Student guide
def All_Student():
  print("What do you wish to do? Key in an action number.\n")
  print("1 = View Details of Sport , 2 = View Sport Schedule")
  print("3 = Register , 4 = Login, -1 = Exit\n")
  num = int(input("Please enter an action number: "))
  print("")
  return num

def Log_Student():
  print("What do you wish to do? Key in an action number.\n")
  print("1 = View Details of Coach , 2 = View Self Record , 3 = Modify Self Record")
  print("4 = View Self Schedule , 5 = Rating self Coach, -1 = Exit\n")
  num = int(input("Please enter an action number: "))
  print("")
  return num



#Admin = 0
#Registered Student = 10
#Log in Student = 20
while True:
  Admin_Details = []
  Coach_Category = []
  Coach_Details = []
  Student_Category = []
  Student_Details = []
  Sport_Category = []
  Sport_Details = []
  Sport_Table = []
  Sport_Schedule = []
  Feedback = []
  Access_File()
  login = Login()
  while (login == 0):
    group = Admin()
    error_action = 1
    for i in range(1,5):
      if group == (i * 10):
        error_action -= 1
        Display(group)
        break
    for i in range(1,5):
      if group == (i * 10 + 1):
        error_action -= 1
        Configure(group)
        break
    for i in range(1,5):
      if group == (i * 10 + 2):
        error_action -= 1
        Search_Specific(group)
        break
    for i in range(1,5):
      if group == (i * 10 + 3):
        error_action -= 1
        Sorting(group)
        break
    for i in range(1,5):
      if group == (i * 10 + 4):
        error_action -= 1
        Add(group)
        break
    Enter_File()
    if group == -1:
      print ("Logging out...\n")
      break
    if (error_action == 1) or (group == 33) or (group == 42):
      print("\nError! Please enter a valid number.\n")
    print("New Action...\n")

  #login, main_id is saved at the main().
  while (login == 10):
    group = All_Student()
    error_action = 1
    if group == 1:
      error_action -= 1
      All_Sport()
    if group == 2:
      error_action -= 1
      All_Schedule()
    if group == 3:
      error_action -= 1
      Reg_Student()
    if group == 4:
      error_action -= 1
      login, main_id = Student_Login()
      if login == 20:
        group = -2
    Enter_File()
    if group == -1:
      print ("Logging out...\n")
      break
    if group == -2:
      print("Loggin in...\n")
      break
    if (error_action == 1):
      print("\nError! Please enter a valid number.\n")
    print("New Action...\n")

  #user_list : User's student list.
  while (login == 20):
    error_action = 1
    group = Log_Student()
    user_list = Find_Self()
    if group == 1:
      error_action -= 1
      View_Coach()
    if group == 2:
      error_action -= 1
      View_Self()
    if group == 3:
      error_action -= 1
      Modify_Self()
    if group == 4:
      error_action -= 1
      Self_Schedule()
    if group == 5:
      error_action -= 1
      Rate_Coach()
    Enter_File()
    if group == -1:
      print ("Logging out...\n")
      break
    if (error_action == 1):
      print("\nError! Please enter a valid number.\n")
    print("New Action...\n")
