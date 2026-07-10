Total_bill=input(("What is the total bill?: "))
tip=input(("What percentage tip would you like to give? 10%, 12%, or 15%?: "))
people=input(("How many people to split the bill?: "))

each_person=(float(Total_bill)+(float(Total_bill)/100*float(tip)))/int(people)

print("Each person should pay: "+str(round(each_person, 2)))
print(f"Each person should pay: {round(each_person,2)}")