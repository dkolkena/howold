#!/usr/bin/env python3

import imdb
from colorama import init, Fore, Back, Style

init(autoreset=True) # Adds color to stdout logging

ia = imdb.IMDb()

def main():
    
    my_search = 'Cheers'
    s_result = ia.search_movie(my_search, results=5)
    print(Style.BRIGHT + 'Here are the top 5 entries for "{}":'.format(my_search))
    for item in s_result:
        print('{} [ID:{}]'.format(item['long imdb canonical title'], item.movieID))
    
    entry = ia.get_movie(s_result[0].movieID)
    show_year = int(entry['year'])
    print(Style.BRIGHT + "\nHere's the info for the first entry:")
    print(entry.summary() + '\n')

    print(Style.BRIGHT + "Here's the age info for the first 12 cast members:")
    for person in entry['cast'][:12]:
        myactor = ia.get_person(person.personID)
        actor_birth_year = int(myactor['birth date'].split('-')[0])
        age = str(show_year - actor_birth_year)
        print('{} was born in {}, and was {} years old when {} came out in {}.'.format(
            myactor['name'], 
            actor_birth_year, 
            age, 
            entry, 
            entry['year'])
            )

if __name__ == "__main__":
  main()
