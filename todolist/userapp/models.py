from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    avatar = models.ImageField(verbose_name="аватар", blank=True, upload_to="users")
    age = models.PositiveIntegerField(verbose_name="возраст", default=18)
    phone = models.CharField(verbose_name="телефон", max_length=20, blank=True)
    city = models.CharField(verbose_name="город", max_length=30, blank=True)
    email = models.EmailField(verbose_name="Почта", max_length=30, unique=True)

    # def __str__(self):
    #     return self.user_name
    #
    # class Meta:
    #     verbose_name = 'Пользователь'
    #     verbose_name_plural = 'Пользователи'


class UserProfile(models.Model):
    objects = None
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )

    user = models.OneToOneField(
        User, unique=True, null=False, db_index=True, on_delete=models.CASCADE, related_name='profile'
    )
    about = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.profile.save()
