import datetime
from django.db import models
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone


class ToDoList(models.Model):
    #id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    #check = models.BooleanField(default=False)
    #pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
    #class Meta:
    #    ordering = ["pub_date"]
        #app_label = 'numberform'

    #def was_published_recently(self):
    #    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Item(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    class Meta:
        ordering = ["choice_text"]
        #app_label = 'numberform'

##########

class TestNumberModel(models.Model):
    test_number = models.IntegerField(default=0)

    def __str__(self):
        return self.test_number

    #def get(self, request):
    #    # <view logic>
    #    return HttpResponse('test_number')

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('testnumber-detail', args=[str(self.id)])

    @property
    def multiple_ten(self):
        return self.test_number * 10