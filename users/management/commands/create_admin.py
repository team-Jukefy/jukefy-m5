from typing import Any, Optional
from users.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError


class Command(BaseCommand):
    help = "Create random users"

    def add_arguments(self, parser):
        parser.add_argument(
            "-u",
            "--username",
            type=str,
            help="Define um username",
        )

        parser.add_argument(
            "-p",
            "--password",
            type=str,
            help="Define uma senha",
        )

        parser.add_argument(
            "-e",
            "--email",
            type=str,
            help="Define um email",
        )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        username = options["username"] or "admin"
        password = options["password"] or "admin1234"
        email = options["email"] or f"{username}@example.com"

        try:
            User.objects.create_superuser(
                username=username,
                password=password,
                email=email,
            )
        except IntegrityError as err:
            if err.__str__().count("username") > 0:
                raise CommandError(f"Username `{username}` already taken.")
            if err.__str__().count("email") > 0:
                raise CommandError(f"Email `{email}` already taken.")

        self.stdout.write(
            self.style.SUCCESS(f"Admin `{username}` successfully created!")
        )
