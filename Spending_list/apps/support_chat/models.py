from django.db import models

from Spending_list.apps.users.models import User


class SupportRequests(models.Model):
    message = models.CharField('Message', max_length=256)
    date_created = models.DateTimeField('Date of the message', auto_now=True)
    read = models.BooleanField('Have you read the message?', default=False, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='From the user')

    class Meta:
        verbose_name = 'Support Request'
        verbose_name_plural = 'Support Requests'

    def __str__(self):
        return self.message


class SupportResponse(models.Model):
    support_request = models.ForeignKey(SupportRequests, on_delete=models.CASCADE, verbose_name='Reply to the message')
    answer = models.CharField('Message', max_length=256)
    read = models.BooleanField('Have you read the answer?', default=False, )
    date_answer = models.DateTimeField('Response date', auto_now_add=True)

    class Meta:
        verbose_name = 'Support Response'
        verbose_name_plural = 'Support Responses'

    def __str__(self):
        return self.answer
