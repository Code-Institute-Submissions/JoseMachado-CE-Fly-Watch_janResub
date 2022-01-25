""" Fly Watch home models """
from django.db import models


class Faq(models.Model):
    """ FAQ model """
    title = models.CharField(max_length=254, null=False, blank=False)
    customer_answer = models.TextField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.title
