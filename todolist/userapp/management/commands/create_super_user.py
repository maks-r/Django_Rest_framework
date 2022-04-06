from django.core.management.base import BaseCommand
from userapp.models import User
from authapp.models import UserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = ShopUser.objects.all()
        for user in users:
            if not len(ShopUserProfile.objects.filter(user=user)):
                users_profile = ShopUserProfile.objects.create(user=user)
                users_profile.save()