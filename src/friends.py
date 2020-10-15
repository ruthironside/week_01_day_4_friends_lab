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
    print(len(person["friends"]))

def remove_friend(person, friend):
    person["friends"].remove(friend)
    print(len(person["friends"]))