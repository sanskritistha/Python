#WAP to inout a name of 5 countries and print only those that ends with vowel
countries=input("Enter 5 countries:").split()
vowels=('a','e','i','o','u')
for country in countries:
    if country.lower().endswith(vowels):
        print(country)