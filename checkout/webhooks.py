from django.http import HttpResponse


class StripeWebhook:

    def __init__(self, request):
        self.request = request