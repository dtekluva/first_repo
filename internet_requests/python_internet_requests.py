import requests

response = requests.get("http://checklight.pythonanywhere.com/streets")
data = response.json()

for street in data["streets"]:
    print(street)
    print()

for street in data["streets"]:
    print(street["name"].ljust(30), "|", street["lga"].ljust(15))
    # print()

adenuga_taiwo = data["streets"][13]
print(adenuga_taiwo)



for number, street in enumerate(data["streets"]):
    print(number, street["name"])

selected_street_number = int(input("Please enter a street by number from the above :\n> "))
selected_street = False

for number, street in enumerate(data["streets"]):
    if number == selected_street_number:
        selected_street = street

print(selected_street["last_light"])