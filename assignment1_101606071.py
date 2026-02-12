"""
Author: Blossom Babalola
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" # string
preferred_weight_kg = 20.5 # float
highest_reps = 25 # integer
membership_active = True # boolean

# Step c: Create a dictionary named workout_stats

#  A dictionary where
# each key is a friend's name and 
# value is a tuple of workout minutes 
# for 3 different workouts - Yoga, Running, and Weightlifting. 
workout_stats = {
    "Alex": (30, 45, 60),
    "Jamie": (20, 35, 50),
    "Taylor": (25, 40, 55),
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
new_workout_stats = {}
for name, workouts in workout_stats.items():
    total_minutes = 0
    for item in workouts:
        total_minutes += item
    updated_key = name + "_Total"
    new_workout_stats[updated_key] = total_minutes
workout_stats.update(new_workout_stats) # update the original dictionary with the new total workout minutes

# Step e: Create a 2D nested list called workout_list
workout_list = [] # An array of arrays, where each inner array contains the workout minutes for a friend and their total workout minutes.
# E.g
# [[30, 45, 60], # Alex's workouts and total
#  [20, 35, 50], # Jamie's workouts and total
#  [25, 40, 55]] # Taylor's workouts
for name, workout in workout_stats.items():
    if name.endswith("_Total"):
        continue # Skip the total workout minutes when creating the workout_list
    individual_workout = []
    for item in workout:
        individual_workout.append(item)
    workout_list.append(individual_workout)
    
# Step f: Slice the workout_list

# Extract and print the minutes for yoga and running for all friends
# Yoga and running are the first two items in each inner list
yoga_running_minutes = [workouts[0:2] for workouts in workout_list]
print("\nYoga and Running minutes for all friends:", yoga_running_minutes, "\n")

# Extract and print the minutes for weightlifting for the last 2 friends
# Weightlifting is the third item in each inner list
weightlifting_minutes = [workouts[2] for workouts in workout_list[1:]] 
print("Weightlifting minutes for the last 2 friends:", weightlifting_minutes, "\n")

# Step g: Check if any friend's total >= 120
for name, total in workout_stats.items():
    if "_Total" in name and total >= 120:
        print(f"Great job staying active, {name.split('_')[0]}! \n")

# Step h: User input to look up a friend
friend_name = input("Enter a friend's name to look up their total workout minutes: ")

foundFriend = False
for name, key in workout_stats.items():
    if friend_name.lower() == name.lower():
        foundFriend = True
        for index, item in enumerate(key):
            workout_types = ["Yoga", "Running", "Weightlifting"]
            print(f"{friend_name}'s {workout_types[index]} minutes: {item}")
        total_minutes = new_workout_stats.get(name + "_Total", "Friend not found")
        print(f"{friend_name}'s total workout minutes: {total_minutes} \n")
        break
if not foundFriend:
    print(f"Friend {friend_name} not found in the records.\n")

# Step i: Friend with highest and lowest total workout minutes

totals_only = {name: total for name, total in workout_stats.items() if "_Total" in name}

highest_workout_friend = max(totals_only, key=totals_only.get)
lowest_workout_friend = min(totals_only, key=totals_only.get)        

# Highest total workout minutes
print(f"{highest_workout_friend.split('_')[0]} has the highest total workout minutes with: {workout_stats[highest_workout_friend]}")

# Lowest total workout minutes
print(f"{lowest_workout_friend.split('_')[0]} has the lowest total workout minutes with: {workout_stats[lowest_workout_friend]}")
