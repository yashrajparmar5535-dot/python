# create lambda function which return compound interest of given amount, rate, year 


compoundtrest = lambda amount,rate,year: amount - (amount/((1+rate)**year))
print(compoundtrest(5000,2,2))