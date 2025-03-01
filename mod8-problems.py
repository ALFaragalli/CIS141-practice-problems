'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''
garden_file = open("gardening_tips.txt", "w")
tip1 = "Water in the morning!"
tip2 = "Use mulch!"
tip3 = "Start with easy plants!"
garden_file.write(tip1 + "\n")
garden_file.write(tip2 + "\n")
garden_file.write(tip3 + "\n")
garden_file.close()

with open("gardening_tips.txt", "r") as gardening_file:
    for line in gardening_file:
        print(line, end="")

'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''
hiking_file = open("hiking_log.txt", "w")
hiking_file.write("")
hiking_file.close

hiking_file = open("hiking_log.txt", "a")

while True:
    hike_name = input("What is the name of the hike? Press 0 to exit. ")
    if hike_name == "0":
        break
    distance = input("What was your total distance in miles? Press 0 to exit. ")
    if distance == "0":
        break 
    hiking_file.write(hike_name + " - " + distance + "\n")
hiking_file.close()

with open("hiking_log.txt", "r") as hike_file:
    for line in hike_file:
        print(line, end="")

'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''
with open("song_lyrics.txt", "r") as lyrics_file:
    lyrics = lyrics_file.read().lower()

count = {}
for i in range(5):
    word = input(f"Enter word #{i+1}: ").lower()
    count[word] = lyrics.split().count(word)

print("Word frequency: ", count)

'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
'''
with open("poll.txt", "r") as poll_file:
    vote = poll_file.read().split(", ")

yea = vote.count("yea")
nay = vote.count("nay")

print(f"Yea votes: {yea}")
print(f"Nay votes: {nay}")
