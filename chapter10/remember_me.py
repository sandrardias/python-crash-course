import json

#username = input("What's your name? ")
username = 'sandias'

filename = 'username.json'
with open(filename, 'w') as file_object:
	json.dump(username, file_object)
	print(f"We will remember you when you come back, {username}!")
