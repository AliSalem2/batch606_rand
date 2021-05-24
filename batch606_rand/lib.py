from typing import Mapping
import numpy as np
from random import choice

def try_me():
    list1 = ["happy","loved","relieved","amused","joyful","excited","peaceful","satisfied"]
    list2 = ["lonely","heartbroken","gloomy","disappointed","hopeless","unhappy","lost","troubled","miserable"]
    full_list = list1 + list2
    classmates = ["Jan","Cyri","Aytac","Anton","Claire","Alessandro","Naomi","Georgios","Katarzyna","Narciso","Aikaterini","Barbara","Simon","Udoka","Nina","Felipe","Bruno","George","Juan","Ludwig","Eitan","Sandra","Luis","Florian","Alibot","Wolfgang","Torsten","Andreas","Tzu-Fan","Konstantin","Simone","Tara","Estefania","Daniil","Dominik","Tim"]
    feeling = choice(full_list)
    if feeling in list1:
        print (f"{choice(classmates)} is feeling {feeling} today")
        print ("say hi")
    else: 
        print (f"{choice(classmates)} is feeling {feeling} today")
        print ("try to motivate them")
        

if __file__ == "__main__":
    try_me()