#create a function that takes name of some countries and return only those countries that contain atleast two vowels
def vow(countries):
    vowel=('a','e','i','o','u')
    a=[]
    for country in countries:
        count=0
        for char in country.lower():
          if char in vowel:
            count+=1
        if count>=2:
             a.append(country)
    return a
countries=['Nepal','nigeria','UK','Bhutan']
print(vow(countries))