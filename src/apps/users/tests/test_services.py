"""
Tests des services users

Objectifs :
- Tester la logique métier indépendante des vues
- Tester la création d'utilisateur via service
- Tester la mise à jour du profil utilisateur
"""

from django.test import TestCase
from apps.users.models import User
from apps.users.services.user_service import create_user, update_user_profile


class UserServiceTest(TestCase):
    """
    Tests unitaires des services utilisateur
    """

    def test_create_user(self):
        """Le service create_user doit créer un utilisateur"""
        user = create_user(
            email="service@test.com",
            password="password123",
            username="service",
            first_name="Service",
            last_name="User",
        )

        self.assertIsInstance(user, User)

    def test_update_user_profile(self):
        """Le service update_user_profile doit modifier la bio"""
        user = User.objects.create_user(
            email="test@test.com",
            username="test",
            password="password123"
        )

        updated = update_user_profile(user, "New bio")
        self.assertEqual(updated.bio, "New bio")
