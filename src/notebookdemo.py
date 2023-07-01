mf="example.txt"

while True:

	print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit\n")
	selection=int(input("Please select one:"))

	if selection==1:
		r = open(mf, "r")
		content = r.read()
		r.close()
		print(content)

	elif selection==2:
		text = input("Write a new note:")
		with open(mf, "a") as f:
			f.write(text)

	elif selection==3:
		with open(mf, "w") as f:
			pass
		print("Notes deleted.")

	elif selection == 4:
		print("Notebook shutting down, thank you.")
		break
