#  write a program to findout from which country user should buy IPhone. two countries are US & UK. assume person is indian. 
# usd = 87.07 $699
# bgp = 117.37 £699

''' 
steps
1) Create two variable and take input from user 
    input1=MRP of iphone in USD
    inpur2=MRP of iphone in BGP
2) Convert both input to INR
    USD_to_INR=input1*87.07
    BGP_to_INR=input2*117.37
3)Find which one is less
    if USD_to_INR > BGP_to_INR:
        print(Better to purchase from US)
    else:
        print(Better to purchase from UK)
'''

iphone_mrp_us = int(input("Enter the MRP of iPhone in us (in USD $): "))
iphone_mrp_uk = int(input("Enter the MRP of iPhone in UK (in GBP £): "))

usd_to_inr = iphone_mrp_us*87.07
print("price of iphone in usd:",usd_to_inr)

bgp_to_inr = iphone_mrp_uk*117.37
print("price of iphone in UK:",bgp_to_inr)

if usd_to_inr<bgp_to_inr:
    print("better to purchase from USA")
else:
    print("better to purchase from UK")


