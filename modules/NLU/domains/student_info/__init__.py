from vityBot.modules.NLU.domains.student_info import student_info
from vityBot.modules.NLU.domains.student_info import get_data


def get_user():
    # should modify to get username and password
    try:
        user = student_info.Student()
    except get_data.InvalidCredentials as e:
            print(e.message)
    except get_data.LoginError as e:
            print(e.message)

    return user
