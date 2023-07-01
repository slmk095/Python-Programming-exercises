def testme(passfield):
	flag_l = False
	flag_n = False
	while len(passfield)>6:
		for i in passfield:
			# if string has letter
			if i.isalpha():
				flag_l = True

			# if string has number
			if i.isdigit():
				flag_n = True

		# returning and of flag
		# for checking required condition
		return flag_l and flag_n

	else:
		return 0