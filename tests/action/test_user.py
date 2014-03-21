# -*- coding: utf-8 -*-
import unittest
import time

from lib.db_utils import set_connexion
from domain.service.user import UserService
from domain.model.user import User
from mongoengine import QuerySet


class UserTests(unittest.TestCase):
    """Test case for auth"""

    @classmethod
    def setUpClass(self):
        """Set Up tests"""
        set_connexion()

        #Generate Login
        ts = time.time()
        self.login = 'bminard_create%s' % ts

    def test_0_user_services(self):
        """Test user creation and get"""
        #Create new user
        user_creation = UserService().create({
            'login': self.login,
            'password_hash': 'pw4benoit',
            'email': 'user_creation_bminard@dolead.com',
            'first_name': 'Benoit',
            'last_name': 'Minard',
            'identities': '{"auth": {"ress1": True, "ress2": False}}'})
        self.assertEqual(user_creation['email'],
                         'user_creation_bminard@dolead.com')

        #Get user by id
        user = UserService().get(user_creation['id'])
        self.assertEqual(user['email'], 'user_creation_bminard@dolead.com')
        self.assertEqual(user['first_name'], 'Benoit')
        self.assertEqual(user['last_name'], 'Minard')
        self.assertEqual(user['identities'],
                         '{"auth": {"ress1": True, "ress2": False}}')

        #Edit existing user
        user_obj_edited = UserService().edit(
            user_creation['id'], {
                'login': self.login,
                'password_hash': 'pw4benoit',
                'email': 'user_edited_bminard@dolead.com',
                'first_name': 'BenoitEdited',
                'last_name': 'MinardEdited',
                'identities': '{"auth": {"ress1": True, "ress2": False, "edited": True}}'})
        user_edited = user_obj_edited
        self.assertEqual(user_edited['email'], 'user_edited_bminard@dolead.com')

        #Check user has been correctly edited
        user_get = UserService().get(user_edited['id'])
        self.assertEqual(user_get['email'], 'user_edited_bminard@dolead.com')
        self.assertEqual(user_get['first_name'], 'BenoitEdited')
        self.assertEqual(user_get['last_name'], 'MinardEdited')
        self.assertEqual(user_get['identities'],
                         '{"auth": {"ress1": True, "ress2": False, "edited": True}}')

    def test_1_user_list(self):
        # Get list user
        user_list = UserService().list()
        self.assertIsInstance(user_list, QuerySet)
        for user in user_list:
            self.assertIsInstance(user, User)
            self.assertTrue(getattr(user, 'login'))
        self.assertIn(self.login,
                      [u.login for u in user_list if u.login == self.login])

    def test_2_user_get_by_login(self):
        """Test user get by login"""
        user_get = UserService().get_by_login(self.login)

    def test_3_user_set_permission(self):
        """Test user set permission"""

