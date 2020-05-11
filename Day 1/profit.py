cost_price = int(input("Enter cost price: "))
selling_price = int(input("Enter selling price: "))
profit = selling_price - cost_price
print("The profit is: " + str(profit))

#what should be the sp if profit is to be maximised by 5% of original profit
# sp - cp = p
# p_new = p + (p*5/100)
# sp_new - cp = p + (p*5/100)
new_selling_price = profit + profit*5/100 + cost_price
print("Selling price required to gain profit of 5"+"% "+"of inital profit is: " + str(new_selling_price))