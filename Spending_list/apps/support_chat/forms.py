from django import forms

from Spending_list.apps.support_chat.models import SupportRequests


class SupportChatForm(forms.ModelForm):
    class Meta:
        model = SupportRequests
        fields = ('message', 'user')
