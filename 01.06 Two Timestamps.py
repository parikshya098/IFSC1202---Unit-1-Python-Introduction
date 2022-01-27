first = "First Timestamp"
print(first)
a = int(input("Enter hours: "))
b = int(input("Enter minutes: "))
c = int(input("Enter seconds: "))

second = "Second Timestamp"
print(second)
x = int(input("Enter hours: "))
y = int(input("Enter minutes: "))
z = int(input("Enter seconds: "))

print( x * 3600 + y * 60 + z - a * 3600 - b * 60 - c)