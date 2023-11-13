def roll_call_dwarves(list_of_dwarves):
    for i in range(len(list_of_dwarves)):
        print(f'{i+1}. {list_of_dwarves[i]}')

def summon_captain_planet(list_of_planeteer):
    return [item.capitalize()+'!' for item in list_of_planeteer]

def long_planeteer_calls(list_of_calls):
    for word in list_of_calls:
        if(len(word)>4):
            return True
    return False

def find_the_cheese(list_of_strings):
    cheese_list=["cheddar", "gouda", "camembert"]
    for item in list_of_strings:
        if item in cheese_list:
            return item
    
