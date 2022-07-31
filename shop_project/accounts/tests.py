from django.test import TestCase
from django.contrib.auth import get_user_model

class UserManagerTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='Test001', 
                                        email='test001@test.ru',
                                        date_of_birth = '1989-10-25',
                                        password='test')
        self.assertEqual(str(user), 'Test001')
        self.assertEqual(user.username, 'Test001')
        self.assertEqual(user.email, 'test001@test.ru')
        self.assertEqual(user.date_of_birth, '1989-10-25')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(username='')
        with self.assertRaises(ValueError):
            User.objects.create_user(username='', email='test001@test.ru',
                                    password='foo')
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username='SuperUserTest001',
                    email='SuperUsertest001@test.ru',
                    date_of_birth = '1989-10-25', password='test')
        self.assertEqual(str(admin_user), 'SuperUserTest001')
        self.assertEqual(admin_user.username, 'SuperUserTest001')
        self.assertEqual(admin_user.email, 'SuperUsertest001@test.ru')
        self.assertEqual(admin_user.date_of_birth, '1989-10-25')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(username='SuperUserTest001',
                                        email='SuperUsertest001@test.ru',
                                        password='test',
                                        is_superuser=False)

