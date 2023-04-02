from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=17)
    subject = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.name

# # list
# Grade = [
#     ('excellent', 1),
#     ('average', 0),
#     ('bad', -1)
# ]
#
#
# class DRFPost(models.Model):
#     name = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     uploaded = models.DateTimeField(auto_now_add=True)
#     rating = models.CharField(choices=Grade, default='average', max_length=50)
#
#     class Meta:
#         ordering = ['uploaded']
#
#     def __str__(self):
#         return self.name
