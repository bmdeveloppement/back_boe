import hashlib


class HashUtils():

    def salt_password(self, login, password_hash):
        """Salt the given password_hash (already in sha1)"""
        sha1_passkey = hashlib.sha1('%sboe_auth%s' % (login, password_hash))
        return sha1_passkey.hexdigest()
