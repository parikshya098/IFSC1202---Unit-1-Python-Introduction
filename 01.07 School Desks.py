s1 = int(input("Enter classroom A: "))
s2 = int(input("Enter classroom B: "))
s3 = int(input("Enter classroom C: "))

division = s1 // 2 + s2 // 2 + s3 // 2 # Each desk seats 2 students. So, total number of students is divided by 2 to calculate the total number of desks required.
modulus = s1 % 2 + s2 % 2 + s3 % 2
total = division + modulus
print(total)