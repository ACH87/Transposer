from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from Dataset.Selenium_Code.Notes import Note

driver = webdriver.Chrome(r'C:\Program Files (x86)\chromedriver')
driver.get('https://www.songsterr.com/a/wsa/dance-gavin-dance-son-of-robot-tab-s448765t1')
# time.sleep(20)
driver.implicitly_wait(10)
print('finding tab')
tablature = driver.find_elements_by_xpath('//*[@id="tablature"]')

elements = tablature[0].find_elements(By.XPATH, value="./child::*")
print('finding element')
# d = c[1].find_elements(By.XPATH, value="./child::*")
notes = []
counter = 0
numbers = []
strings = []
for element in elements:
    print(counter)
    counter+= 1
    print(element.get_attribute("class") )
    if element.get_attribute("class") == 'Cw81bf':
        child_elems = element.find_elements(By.XPATH, value="./child::*")

        for child_elem in child_elems:
            if child_elem.get_attribute("class") == 'D38xz':
                strings.append(Note(child_elem.text, int(child_elem.location['x']),  int(child_elem.location['y'])))
            if child_elem.get_attribute("class") == 'h81p9 h8e1':
                numbers.append(child_elem)
                break


#remove duplicate strings
temp = []
for s in strings:
    if not temp.__contains__(s.note):
        temp.append(s.note)
    else:
        strings.remove(s)

del temp


list_of_notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
def calculate_note(strin, number):
    starting_index = list_of_notes.index(strin)
    return list_of_notes[(number+starting_index)%12]
    #TODO add code to create individual notes

for note in numbers:
    s = None
    print(note.location.x)
    print(note.location.y)
    for string in strings:
        if string.y -5 < int(note.location['y']) < string.y + 5:
            print(string.note)
            s= string.note
            break
    print(note.text)
    notes.append(calculate_note(s, int(note.text)))

for n in notes:
    print(n)