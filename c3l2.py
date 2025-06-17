print("Jane's Stuff Store")

numberofitems = int(input("\nHow many items would you like to purchase? "))
total = 0
for i in range(numberofitems):
    print("Enter the price of item", i+1, " : " , end="")
    price = float(input())
    total += price

print(f"\nThe total cost of your items is ${total:.2f}")
total_average = total / numberofitems
print(f"The average cost of each item is ${total_average:.2f}")

                  
