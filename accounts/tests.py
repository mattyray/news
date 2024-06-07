from django.test import TestCase
from django.contrib.auth import get_user_model

#get_user_model() returns the user model that is active in this project
#User.objects.create_user() creates a new user
#TestCase is a class that helps in testing the code
#self.assertEqual() is a method that checks if the two arguments are equal
#self.assertTrue() is a method that checks if the argument is true
#self.assertFalse() is a method that checks if the argument is false

class UserManagersTests(TestCase):
    def test_create_user(self):
        User= get_user_model()
        user=User.objects.create_user(
            username='pr0blemdrinker',
            email='adude@adomain.com',
            password='testpass1234',
        )
        self.assertEqual(user.username, 'pr0blemdrinker')
        self.assertEqual(user.email, 'adude@adomain.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='testsuperuser@domaimn.com',
            password='testpass1234',
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'testsuperuser@domaimn.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)

        #test_create_user() and test_create_superuser() are methods that test the create_user() 
        #and create_superuser() methods in the User model
        #create_user() creates a new user with the specified username, email, and password
        #create_superuser() creates a new superuser with the specified username, email, and password