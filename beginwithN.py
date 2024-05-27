#wap to input name of 5 countries and print only those names that begin with "N"
countries=input("enter the name of a country").split()
for country in countries:
 if country.lower().startswith('n'):
    print(country)
     
