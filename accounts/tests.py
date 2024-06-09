from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

#get_user_model() returns the user model that is active in this project
#User.objects.create_user() creates a new user
#TestCase is a class that helps in testing the code
#self.assertEqual() is a method that checks if the two arguments are equal
#self.assertTrue() is a method that checks if the argument is true
#self.assertFalse() is a method that checks if the argument is false

class UserManagersTests(TestCase):
    #UserManagersTests is a class that tests the User model
    def test_create_user(self):
        #test_create_user() is a method that tests the create_user() method in the User model
        User= get_user_model()
        #User is a variable that stores the user model that is active in this project
        user=User.objects.create_user(
            username='pr0blemdrinker',
            email='adude@adomain.com',
            password='testpass1234',
        )
        #user is a variable that stores the new user created using the create_user() method
        self.assertEqual(user.username, 'pr0blemdrinker')
        self.assertEqual(user.email, 'adude@adomain.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        #test_create_superuser() is a method that tests the create_superuser() method in the User model
        User = get_user_model()
        #User is a variable that stores the user model that is active in this project
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='testsuperuser@domaimn.com',
            password='testpass1234',
        )
        #admin_user is a variable that stores the new superuser created using the create_superuser() method
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'testsuperuser@domaimn.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)

class SignupPageTests(TestCase):
    #SignupPageTests is a class that tests the signup view
    def test_url_exists_at_proper_location_signupview(self):
        #test_url_exists_at_proper_location_signupview() is a method that tests if the signup 
        # view exists at the proper location
        response = self.client.get('/accounts/signup/')
        #response is a variable that stores the response from the client when the signup view is accessed
        self.assertEqual(response.status_code, 200)
        #response.status_code is the status code of the response
        #200 is the status code for a successful HTTP request
        

    def test_signup_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        response=self.client.post(
            reverse('signup'),
            data={
                'username':'testuser',
                'email':'testuser@domain.com',
                'age': 21,
                'password1':'testpass1234',
                'password2':'testpass1234',
            },

        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'testuser')
        self.assertEqual(get_user_model().objects.all()[0].email, 'testuser@domain.com')

        #test_create_user() and test_create_superuser() are methods that test the create_user() 
        #and create_superuser() methods in the User model
        #create_user() creates a new user with the specified username, email, and password
        #create_superuser() creates a new superuser with the specified username, email, and password