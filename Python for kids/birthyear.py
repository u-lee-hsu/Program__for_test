year= input('Please Enter Year of birth:')
if not bool(year.rstrip()):
	print('You need to enter a value for your year of birth')
if bool(year.rstrip()):
    print('Your birth year is %s'%year)
