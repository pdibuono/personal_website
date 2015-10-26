from django.db import models

VISIBILITY_CHOICES = (
(0, 'Choose the dropdown to Select'),
(1, 'Ms.'),
(2, 'Mrs.'),
(3, 'Mr.'),
(4, 'Dr.'),
)

# Create your models here.
class Contact(models.Model):
    title = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)
    First_Name = models.CharField(max_length=300, default="")
    Last_Name = models.CharField(max_length=300, default="")
    email = models.EmailField(max_length=300)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
      return self.First_Name