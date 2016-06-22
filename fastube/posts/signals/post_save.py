from django.dispatch import receiver
from django.db.models.signals import post_save

from hashids import Hashids

from posts.models import Post


@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):
    if not instance.hash_id:
        hashids = Hashids(salt="hash my id", min_length=6)
        instance.hash_id = hashids.encode(instance.id)
        instance.save()
