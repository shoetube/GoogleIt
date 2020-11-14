#!/usr/bin/python3

import webbrowser
import sys

if len(sys.argv) == 1:
    input_query = input("What would you like to search for?: ")
elif len(sys.argv) == 2:
    input_query = sys.argv[1]
else:
    list_query = sys.argv[1:]
    input_query = ' '.join(list_query)

print(f'Searching google for "{input_query}"')
search_list = input_query.split(' ')
query = '+'.join(search_list)
webbrowser.open(f"http://www.google.com/search?q={query}")
