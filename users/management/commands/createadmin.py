from django.core.management import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            User = get_user_model()
            user = User.objects.create(
                email="testadmin@gmail.com",
                first_name="Admin",
                last_name="Admin",
            )

            user.set_password("1234")

            user.is_staff = False
            user.is_superuser = False

            user.save()

            self.stdout.write(self.style.SUCCESS(f"Successfully created user {user.email}!"))
        except Exception as e:
            print(e)

        try:
            User = get_user_model()
            user = User.objects.create(
                email="testadminsup@gmail.com",
                first_name="Admin_sup",
                last_name="Admin_sup",
            )

            user.set_password("1234")

            user.is_staff = True
            user.is_superuser = True

            user.save()

            self.stdout.write(self.style.SUCCESS(f"Successfully created user {user.email}!"))

        except Exception as e:
            print(e)



