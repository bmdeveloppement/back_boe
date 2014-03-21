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
        login = 'bminard%s' % ts

        #Create new user
        user_obj = UserService().create({'login': login,
                                         'password_hash': 'pw4benoit',
                                         'email': 'benoit.minard@dolead.com',
                                         'first_name': 'Benoit',
                                         'last_name': 'Minard',
                                         'identities': '{"auth": {"pipo": "pouet", "plouf": "waf"}}'})
        user_creation = user_obj
        self.assertEqual(user_creation['login'], login)

        #Login
        user = AuthenticationService().authenticate(login, 'pw4benoit')
        self.assertEqual(user['email'], 'benoit.minard@dolead.com')
        self.assertEqual(user['first_name'], 'Benoit')
        self.assertEqual(user['last_name'], 'Minard')
        self.assertEqual(user['identities'], json.loads('{"auth": {"pipo": "pouet", "plouf": "waf"}}'))
