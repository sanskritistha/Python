#create a function that takes a list of country name and return the countries that end with a vowel.
def vowel(countries):
  vowel=('a','e','i','o','u')
  a=[]
  for country in countries:
    if country.lower().endswith(vowel):
        a.append(country)
  return a
countries=['nepal','german','china','korea']
print(vowel(countries))
