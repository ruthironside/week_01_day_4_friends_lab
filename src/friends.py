def get_name(name):
   return name["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    for snack in person["favourites"]["snacks"]:
        if snack == food:
            return True
    return False

def add_friend(person, friend):
    person["friends"].append(friend)

def remove_friend(person, friend):
    person["friends"].remove(friend)

def total_money(list):
    monies = 0
    for person in list:
        monies += person["monies"]
    return monies
    
def l_money(ler, lee, amount):
    ler["monies"] -= (amount)
    lee["monies"] += (amount)

def all_favourite_foods(list):
    food = []
    for person in list:
        for snack in list["favourites"]:
            food.append(person["snacks"])
    return food