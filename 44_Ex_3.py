# create lambda function that return true if city passed as 1st argument exist in list passed argument as 2nd argument, if city does not exist return false 
# isCityExist('Bhavnagar',['Bombay','Baroda','rajkot']) # false
# isCityExist('rajkot',['Bombay','Baroda','rajkot']) # true 

getcity = lambda city,list : city in list
print(getcity("bhavnagar",["bhavnagar","rajkot","baroda"]))
print(getcity("Sihor",["bhavnagar","rajkot","baroda"]))
