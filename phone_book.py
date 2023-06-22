import sys
print('Phone Book Program')
phone_dict = {}
option = 0

while option != '4':
	option = input('1. Add a new contact\n2. Search for a contact\n3. List all contacts\n4. Exit\n\nEnter your choice: ')
	if option == '1':
		name = input('Enter name: ')
		phone = input('Enter phone number: ')
		phone_dict[name] = phone
		print('\nContact added successfully!\n\n')

	if option == '2':
		name = input('Enter name: ')
		if name in phone_dict.keys():
			print('Phone number: ',phone_dict[name],'\n')
	if option == '3':
		for name in phone_dict.keys():
			print(name,': ', phone_dict[name],'\n')	

	if option == '4':
		print('Goodbye!')
		sys.exit()