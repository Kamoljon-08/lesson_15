import requests

all__the__list = []

url = "https://countryapi.io/api/all?apikey=UCwtUfymshwxTgYQdp9jvA5DIcuSw7CabU65TMc9"
req__body = requests.get(url)
req__json = req__body.json()

def STATE__DATA():
    for i in req__json:
        print("====================================")
        print("Name:", req__json[f"{i}"]["name"])
        print("Region:", req__json[f"{i}"]["region"])
        print("Capital", req__json[f"{i}"]["capital"])
        print("Area:", req__json[f"{i}"]["area"])
        print("Population:", req__json[f"{i}"]["population"])
        print("====================================")
    NEW__MODEL(i)
    return MENU()

def STATE__REGIONS():
    for i in req__json:
        print("Region:", req__json[f"{i}"]["name"],"-->", req__json[f"{i}"]["region"])
    return MENU()

def STATE__CAPITALS():
    for i in req__json:
        print("Capital:", req__json[f"{i}"]["name"],"-->", req__json[f"{i}"]["capital"])
    return MENU()

def NEW__MODEL(i):
    all__the__list.append({
        "name": req__json[f"{i}"]["name"],
        "region": req__json[f"{i}"]["region"],
        "capital": req__json[f"{i}"]["capital"],
        "area": req__json[f"{i}"]["area"],
        "population": req__json[f"{i}"]["population"]
    })
MENU()

def MENU():
    print("1) Davlatlarning barcha datalarini ko'rish")
    print("2) Davlatlarni qaysi mitaqadaligini ko'rish")
    print("3) Davlatlarning poytaxtini ko'rish")

    menu__number = int(input("Menudan birini kiritng: "))

    if menu__number == 1:
        STATE__DATA()

    elif menu__number == 2:
        STATE__REGIONS()

    elif menu__number == 3:
        STATE__CAPITALS()

    else: 
        print("Siz sonlarni to'g'ri kiritng: ")