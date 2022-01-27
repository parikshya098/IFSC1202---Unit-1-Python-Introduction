x = int(input("Enter length of race in kilometers: "))
y = int(input("Enter minutes: "))
z = int(input("Enter seconds: "))

distance = x * 0.621 # 1km = 0.621371 miles
time = y / 60 + z / 3600 # converting minutes and seconds into hours

average_speed = distance / time # speed is distance divided by time
print(average_speed)