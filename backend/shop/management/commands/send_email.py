from django.core.mail import send_mail
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'init default data for testing'

    def send(self):
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['vildan.maydanovich.valeev@gmail.com'],
            fail_silently=False,
        )

    def handle(self, *args, **options):
        self.send()
        return 'SENDED Email'

