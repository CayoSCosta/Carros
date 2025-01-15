from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print('### pre-save ###')
    print(instance)

@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    print('### pre-delete ###')
    print(instance)

@receiver(post_save, sender=Car)
def car_pos_save(sender, instance, **kwargs):
    print('### post-save ###')
    print(instance)

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print('### post_delete ###')
    print(instance)