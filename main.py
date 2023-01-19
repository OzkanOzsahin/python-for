from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

    #1
def shortest_names(countries):
    shortest_len = float("inf")
    shortest_names = []

    for country in countries:
        country_len = len(country)
        if country_len < shortest_len:
            shortest_len = country_len
            shortest_names = [country]
        elif country_len == shortest_len:
            shortest_names.append(country)

    return shortest_names

#2
def most_vowels(countries):
    vowels = "aeiou"
    country_vowel_counts = {}
    for country in countries:
        vowel_count = sum(1 for c in country.lower() if c in vowels)
        country_vowel_counts[country] = vowel_count
    top_countries = sorted(country_vowel_counts, key=country_vowel_counts.get, reverse=True)[:3]
    return top_countries

#3
def alphabet_set(countries):
    countries = [country.lower() for country in countries]

    letters_needed = list("abcdefghijklmnopqrstuvwxyz")
    countries_used = []
    for country in countries:
        for char in country:
            if char in letters_needed:
                letters_needed.remove(char)
                if country not in countries_used:
                    countries_used.append(country)
                if len(letters_needed) == 0:
                    return countries_used

if __name__ == "__main__":
    countries = get_countries()
    print(shortest_names(countries))
    print(most_vowels(countries))
    print(alphabet_set(countries))
    print(len(alphabet_set(countries)))                       

