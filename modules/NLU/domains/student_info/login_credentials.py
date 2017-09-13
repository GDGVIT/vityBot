import getpass
import re

r = re.compile('^[1-9]{2}[a-zA-Z]{3}[0-9]{4}$')


class LoginDetails:
    """
    class stores info regarding username and password
    """
    def __init__(self):
        while True:
            self.regid = raw_input('User ID: ').upper()

            if re.match(r, self.regid):
                break
            else:
                print('invalid user ID. try again')

        self.psswd = getpass.getpass('Password: ')

    def get_dict(self):
        q = dict()

        q['regNo'] = self.regid
        q['psswd'] = self.psswd

        return q
