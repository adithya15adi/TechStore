from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import getpass


class Command(BaseCommand):
    help = "Create a Django superuser interactively"

    def handle(self, *args, **options):
        User = get_user_model()

        username = input("Username: ")
        email = input("Email: ")
        password = getpass.getpass("Password: ")

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR("Username already exists."))
            return

        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS(f"Superuser '{user.username}' created successfully.")
        )