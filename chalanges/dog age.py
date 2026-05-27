print("Enter your dog's age:")
dog_age = int(input())
human_age = 0
if dog_age <= 1:
    human_age = 15
    print(f"Your dog's age in human years is: {human_age}")
elif dog_age <= 2:
    human_age = 15 + (dog_age - 1) * 9
    print(f"Your dog's age in human years is: {human_age}")
elif dog_age > 2:
    human_age = 24 +(dog_age - 2) * 5
    print(f"Your dog's age in human years is: {human_age}")
else:    print("Please enter a valid age for your dog.")
            