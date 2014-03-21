from lib.hash_utils import HashUtils
from domain.model.user import User


class AuthenticationService(object):

    def authenticate(self, login, password_hash):
        """Check the login and password hash match"""
        user_obj = User.objects(login=login).first()
        if user_obj is None:
            return None
        if user_obj.passkey != HashUtils().salt_password(login, password_hash):
            return False
        return user_obj.to_dict()
