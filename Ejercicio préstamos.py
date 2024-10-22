#function to calculate loans
# P=Principal loan amount, N=number of month, R=monthly interest rate, M=monthly money that is owed; M=P[R(1+R)^N]/[(1+R)^N-1]
print("We´re going to calculate the monthly payment for a loan, please set this parameters: ")
P = int(input("Please introduce a sum of money to deposit "))
#We calculate the monthly interest:
Interest_years = int(input("Please state an integer for the yearly interest rate you want to depost it at "))
R = int(Interest_years/100/12)
#We calculate the number of months:
Time_years = int(input("Please introduce an integer for the time in years you want to deposit the money "))
N = int(Time_years*12)

#We take values in sorts from 1 to N taking the null value into consideration
Range_N = range(1, N+1)
M=P*[R*(1+R)**N]/[(1+R)**(N-1)]

#We make a graphic
debt_df = pd.DataFrame({"Month": Range_N, "Money":M})
print(debt_df)
#We show the sum of money that is owed
All_money = M*N
print("The final sum of mone owed is:", All_money)



