#Were going to converse with a simple chat bot

#The first part is to greet the user
name = (input(("Hey, my name is ChatBot, what is yours?"  ) ) )
print("You have a beautiful name", name)

#Follow a normal conversation taking about ages
birth_year = int(input("I was created on 2024, what year were you born? "))
birth_month = int(input("I was made in October, on which month were you born? "))
#Now we find the age difference asking the user the month they were born in
month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#We calculate the age of the user depending on the month they were born
if birth_month in month_list:
    #In October:
    if birth_month == "October":
        year_gap = 2024 - birth_year
        print("Hey,", name, "we bern on the same month. Cool. We are exactly", year_gap, "years apart")
    #For later in the year:
    if birth_month == ["November", "December"]:
        year_gap = 2023 - birth_year
        print("Hey,", name, "you were born later in the year than me, and we are", year_gap, "apart")
    #For earlier in the year:
    else:
        year_gap = int(2024 - birth_year)
        print("Hey,", name, "you were born earlier in the year than me, then we are", year_gap, "years apart")
else:
    print("Please introduce a valid month of the calendar. Maybe you made a typographic error?")



