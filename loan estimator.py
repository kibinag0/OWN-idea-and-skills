


capital = float(input("Please input the capital:"))
interest = float(input("Please input the yearly interest:"))
years = float(input("Please input the duration of the year:"))




year = float(input("Which year's data would you like to see? Please put the number:"))




#Monthly payment (in the case of constant payment)
pay = capital*((interest)/(1.0-(1.0+interest)**(-years)))

interest_1st_pay = capital * interest
amort_1st_pay = pay - interest_1st_pay



#Amortization in specific year
amort_in_year = int(amort_1st_pay*((1+interest)**(year-1)))
interest_in_year = int(pay - amort_in_year)
capital_in_year = int(interest_in_year / interest)

print(amort_in_year)
print(interest_in_year)
print(capital_in_year)


print("Remaining capital; %d"%(capital_in_year))
print("Payment; %d"%(pay))














