current_users=["Collins","Buullion","Logical","Martin","Wendy"]
new_user=["Grace","Buullion","Famous","Martin","Nisy"]

for user in new_user:
    if user.lower() in [user.lower for user in current_users]:
        print(f'The username {user} is not available. Please entera new username')
    else:
        print(f"The Username {user} is available")

# the second assignment
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
     print(num)
