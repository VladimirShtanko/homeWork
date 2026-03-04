from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Users(AbstractUser):
    ROLE_CHOICES = [
        ('cl', 'Клиент'),
        ('organ', 'Организация'),
        ('man', 'Менеджер'),
        ('anonym', 'Незарегистрированный'),
    ]

    role = models.CharField('Роль', max_length=10, choices=ROLE_CHOICES, default='cl')


    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='Группы, к которым принадлежит пользователь.'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Разрешения, предоставленные пользователю.'
    )

    def __str__(self):
        return '{}'.format(f'{self.username}')