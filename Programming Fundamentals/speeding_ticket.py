def speeding_ticket_calc():
	fine = 0
	while True:
		try:
			speed_limit = int(input('Enter speed limit: '))
			clocked_speed = int(input('Enter clocked speed: '))
			break
		except ValueError:
			print('Only numbers are allowed.  Try again.')
	if clocked_speed > speed_limit:
		speed_diff = clocked_speed - speed_limit
		fine = 50.00 + (speed_diff * 5.00)
		if clocked_speed > 90:
			fine += 200.00
		print('Total fine amount:', '$'+str(fine))
	else:
		print('Speed is within legal limits')
	
		
speeding_ticket_calc()
