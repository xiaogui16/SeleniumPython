import random

class GetUser(object):
    def get_range_user():
        user_info = ''.join(random.sample('1234567890abcdefghijklmn',8))
        return user_info