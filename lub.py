import json
from datetime import datetime

key_plant = ['cactus', 'violet', 'ficus', 'aloe', 'rosemary']
key_word = {
    'plant': ['plant'],
    'light': ['light'],
    'water': ['water'],
    'toxity': ['toxity', 'toxic', 'pet', 'child'],
    'maintenance': ['maintenance', 'care'],
    'size': ['space', 'size', 'hight', 'high'],
    'flower': ['bloom', 'flower']
}
data = []

answer = [
    'needs to be watered'
]
current_dialog = []

all_history = {}


def save_dict():
    with open('history.json', 'w') as file:
        json.dump(all_history, file)


def read_dict():
    global data
    global all_history
    with open('dict.json', 'r') as file:
        data = json.load(file)
    with open('history.json', 'r') as file:
        all_history = json.load(file)
    return all_history


def save_dialog():
    all_history[str(datetime.now())] = current_dialog
    save_dict()
    current_dialog.clear()


def analiz_question(quest):
    current_dialog.append(quest)
    rez = []
    rez_plant = ""
    for plant in key_plant:
        if plant in quest:
            rez_plant = plant
    for key in key_word.keys():
        for i in key_word[key]:
            if i in quest:
                rez.append(key)
    return rez_plant, rez


def maintenance_inf():
    h_maint = 'High-maintenance indoor plants:'
    l_maint = 'Low-maintenance indoor plants: '
    for i in data:
        if i['maintenance'] == 'high-maintenance':
            h_maint = h_maint + i['plant'] + " "
        if i['maintenance'] == 'low-maintenance':
            l_maint = l_maint + i['plant'] + " "
    return h_maint + '. ' + l_maint + '.'


def flower_inf():
    no_flower = 'Non-flowering indoor plants: '
    flower = 'Flowering indoor plants: '
    for i in data:
        if i['flower'] == 'yes':
            flower = flower + i['plant'] + " "
        if i['flower'] == 'no':
            no_flower = no_flower + i['plant'] + " "
    return flower + '. ' + no_flower + '.'


def plant_light(plant):
    for i in data:
        if i['plant'] == plant:
            return plant + " is " + i['light'] + ' plant.'


def plant_maintenance(plant):
    for i in data:
        if i['plant'] == plant:
            return plant + " is " + i['maintenance'] + ' plant.'


def plant_size(plant):
    for i in data:
        if i['plant'] == plant:
            return 'Average hight of ' + plant + " is " + i['size'] + '.'


def plant_water(plant):
    for i in data:
        if i['plant'] == plant:
            return plant + " needs to be watered " + i['water'] + '.'


def plant_toxity(plant):
    for i in data:
        if i['plant'] == plant:
            if i['toxity'] == 'yes':
                return plant + ' is toxic and can be dangerous for pets and children.'
            if i['toxity'] == 'no':
                return plant + ' isn\'t toxic plant.'


def plant_flower(plant):
    for i in data:
        if i['plant'] == plant:
            if i['flower'] == 'yes':
                return plant + ' is flowering plant.'
            if i['flower'] == 'no':
                return plant + ' isn\'t flowering plant.'


def find_in_base(plant, rez):
    if plant == "" and 'plant' not in rez:
        current_dialog.append('try again')
        return 'try again'
    if plant == "" and 'plant' in rez:
        rez_l = ""
        if 'light' in rez:
            rez_l += 'The right light level for plants is so important as too much light might hurt your plant as much as too little. Instead of thinking about where your plant will look best and fit best in terms of interior design, you need to know the needs of your indoor plants.'
        if 'water' in rez:
            rez_l += 'As a general rule, with most houseplants its best to let the top few centimetres of the compost dry out before watering. Water less during the autumn and winter and water more in spring and summer.'
        if 'toxity' in rez:
            rez_l += 'Toxic Houseplants can cause various illnesses and, in some cases, death. Although toxic plants usually cause little more than irritation, it is still important to be aware of what makes a plant poisonous so you can treat it accordingly.'
        if 'maintenance' in rez:
            rez_l += maintenance_inf()
        if 'size' in rez:
            rez_l += ""
        if 'flower' in rez:
            rez_l += flower_inf()
        else:
            rez_l += "Enter plant characteristic"
        current_dialog.append(rez_l)
        return rez_l
    if 'plant' in rez:
        rez.remove('plant')
    if len(rez) == 0:
        otvet = plant_size(plant) + plant_maintenance(plant) + plant_flower(plant) + plant_light(plant) + plant_toxity(
            plant) + plant_water(plant)
        current_dialog.append(otvet)
        return otvet
    else:
        rez_l = ""
        if 'light' in rez:
            rez_l += plant_light(plant)
        if 'water' in rez:
            rez_l += plant_water(plant)
        if 'toxity' in rez:
            rez_l += plant_toxity(plant)
        if 'maintenance' in rez:
            rez_l += plant_maintenance(plant)
        if 'size' in rez:
            rez_l += plant_size(plant)
        if 'flower' in rez:
            rez_l += plant_flower(plant)
        current_dialog.append(rez_l)
        return rez_l


if __name__ == '__main__':
    history = []
    save_dict(data, history)
