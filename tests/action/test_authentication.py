# -*- coding: utf-8 -*-
import unittest
import time
import json

from lib.db_utils import set_connexion
from domain.service.authentication import AuthenticationService
from domain.service.user import UserService


class AuthenticationTests(unittest.TestCase):
    """Test case for auth"""

    def test_authentify(self):
        """Test authentication"""
        set_connexion()

        #Generate Login
        ts = time.time()
        login = 'bm%s' % ts

        #Create new user
        user_obj = UserService().create({'login': login,
                                         'password_hash': 'pw4benoit',
                                         'email': 'b.m@gmail.com',
                                         'first_name': 'b',
                                         'last_name': 'm',
                                         'identities': '{"auth": {"pipo": "pouet", "plouf": "waf"}}'})
        user_creation = user_obj
        self.assertEqual(user_creation['login'], login)

        #Login
        user = AuthenticationService().authenticate(login, 'pw4benoit')
        self.assertEqual(user['email'], 'b.m@gmail.com')
        self.assertEqual(user['first_name'], 'b')
        self.assertEqual(user['last_name'], 'm')
        self.assertEqual(user['identities'], json.loads('{"auth": {"pipo": "pouet", "plouf": "waf"}}'))
