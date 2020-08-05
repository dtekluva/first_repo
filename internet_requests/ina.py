import requests

response = requests.get("http://checklight.pythonanywhere.com/streets")

data = response.json()
streets_list = data["streets"]
selected_street = None

# print(data['streets'][13]['history']['time_line'])

# for street in streets_list:
#     print(street["name"][0].ljust(25),"|", street["state"].ljust(6), "|", street["status"])

#     if street["name"] == "Adenuga Taiwo":
#         selected_street = street


# street_timeline = selected_street['history']['time_line']
# print(street_timeline)

# for timeline in data['streets'][13]['history']['time_line']:
#     # print(timeline)
#     # print(timeline['period'])
#     print(str(timeline["id"]).ljust(25),"|", timeline["time"].ljust(25),"|", str(timeline["period"]).ljust(6), "|", timeline["status"])

################################################################

# print(str("ID").ljust(25),"|", "TIME".ljust(25),"|", str("PERIOD").ljust(6), "|", "STATUS")
# print()
# for timeline in street_timeline:
#     # print(timeline)
#     # print(timeline['period'])

#     print(str(timeline["id"]).ljust(25),"|", 
#                 timeline["time"].ljust(25),"|", 
#                 str(round(timeline["period"]/3600, 2)).ljust(6), "|", 
#                 timeline["status"])

def print_all_streets(*streets_list):
    print(streets_list)

print_all_streets(*streets_list)