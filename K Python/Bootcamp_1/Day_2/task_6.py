my_investment = float(input("Investrment = "))
my_investment_rate = float(input("Investrment Rate = "))
total_time_of_investment = 10
investment_sum = 0

for i in range(total_time_of_investment):
    my_investment += my_investment*(my_investment_rate/100)
    
print("10 Years of Investmen = ${:.2f}".format(my_investment))
