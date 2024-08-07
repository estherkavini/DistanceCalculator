import csv

#Data to be put in CSV file
data = [
    ["Name", "Latitude", "Longitude"],
    ["Alta", 69.96887, 23.27165],
    ["Anchorage", 61.21806, -149.90028],
    ["Jakarta", -6.21462, 106.84513],
    ["London", 51.50853, -0.12574],
    ["Longyearbyen", 78.22334, 15.64689],
    ["North pole", 90, 0],
    ["Oslo", 59.91273, 10.74609],
    ["South pole", -90, 0],
    ["Troll research station", -72.00194, 2.53389],
    ["Vardø", 70.37048, 31.11066],
]

with open('places.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)
