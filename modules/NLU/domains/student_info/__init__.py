import student_info

def get_user():
	# should modify to get username and password
	try:
		user = student_info.Student()
	except student_info.get_data.InvalidCredentials as e:
        	print e.message
	        exit(1)
	except student_info.get_data.LoginError as e:
        	print e.message
        	exit(1)

	return user
