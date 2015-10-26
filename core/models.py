from django.db import models

VISIBILITY_CHOICES = (
(0, ''),
(1, 'Ms.'),
(2, 'Mrs.'),
(3, 'Mr.'),
(4, 'Dr.'),
)

# Create your models here.
class Contact(models.Model):
    title = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
      return self.title