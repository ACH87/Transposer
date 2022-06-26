from urllib import request
from bs4 import BeautifulSoup
from src.Tab.Bar import Bar
import requests as r

"""
File to scrape internet for tab music
"""
#TODO MAKE SURE WE KEEP TRACK OF NOTES RELATIVE TO BAR
#TODO KEEP TRACK OF STRING
#TODO GET DATASET USING HREF TAG IN SONGTERR SEARCH

response = r.get('https://tabs.ultimate-guitar.com/tab/pink-floyd/wish-you-were-here-chords-44555')
page_source = BeautifulSoup(response.content.decode('utf-8'), "html.parser")
print(page_source.find_all("span"))
#
# notes = []
# bar = Bar()
#
# for line in page_source.find_all('svg', {'class': 'n'}):
#     l = line.find_all('text', {'class': ['v', 'm']} )
#     curr_x = 0
#     for c in l:
#         if c.get('class') == ['m']:
#             notes.append(bar)
#             # bar.print_notes()
#             bar = Bar()
#         else:
#             if curr_x == c.get('x'):
#                 bar.add_chord(c.text)
#             else:
#                 curr_x = c.get('x')
#                 bar.add_note(c.text)
#
# print(notes[0])
