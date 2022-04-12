from django.core.management.base import BaseCommand
from ...models import UserProfile, User



class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            if not len(UserProfile.objects.filter(user=user)):
                users_profile = UserProfile.objects.create(user=user)
                users_profile.save()
