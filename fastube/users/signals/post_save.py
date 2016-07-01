from django.dispatch import receiver
from django.db.models.signals import post_save

import requests
from time import sleep
from users.models import User


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        sleep(3)

        base_url = 'http://api.openapi.io/ppurio/1/message/sms/dobestan'
        headers = {
            'x-waple-authorization': 'MTkyMC0xNDEzODU0NTAwMzU3LTllM2VkOTM3LTYwMTEtNGU2Zi1iZWQ5LTM3NjAxMTNlNmYyMg==',
        }
        data = {
            'send_phone': '01022205736',
            'dest_phone': instance.phonenumber,
            'msg_body': 'Thank you for registering',
        }

        response = requests.post(
                base_url,
                headers=headers,
                data=data,
        )
