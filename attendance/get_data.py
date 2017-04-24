import requests

base = 'https://myffcs.in:10443/campus/vellore/'
login = '/login/'
personal_details = '/personalDetails/'
edu_details = '/educationalDetails/'
exam_schedule = '/examSchedule/'
messages = '/messages/'
refresh = '/refresh/'


class LoginError(Exception):
    def __init__(self):
        self.message = 'Error logging in'


class InvalidCredentials(Exception):
    def __init__(self):
        self.message = 'Invalid login credentials'


def process_login(login_info):
    url = base + login

    res = requests.post(url, login_info.getDict())

    res_dict = res.json()

    if res_dict['status']['code'] == 12:
        raise InvalidCredentials
    elif res_dict['status']['code'] != 0:
        raise LoginError

    return res_dict


def get_course_details(login_info):
    url = base + refresh

    process_login(login_info)

    res = requests.post(url, login_info.getDict())

    res_dict = res.json()

    return res_dict