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
import math




class PIMS:
    result_test_number = []
    result_number = []
    test_result = {}

#pim = {}
pim = PIMS()



class TestNumberModel(models.Model):
    test_number_name = models.CharField(max_length=100, help_text='Enter a name')
    test_number = models.IntegerField(default=0, help_text='Enter a value min:0 max:100')
    #test_number = models.FloatField(default=0.0)
    test_number_one = models.IntegerField(default=0, help_text='Enter a value min:0 max:100')
    test_number_two = models.IntegerField(default=0, help_text='Enter a value min:0 max:100')

    time_test_number = models.DateTimeField(auto_now_add=True, blank=True)

    #pim[id]=PIMS()
    #pim = PIMS()


    def __str__(self):
        return self.test_number

    #def get(self, request):
    #    # <view logic>
    #    return HttpResponse('test_number')

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('testnumber-detail', args=[str(self.id)])

    @property
    def calcul(self):
        result_calcul = self.test_number + 1 #math.sqrt(self.test_number)
        result_calcul_one = self.test_number_one + 2
        result_calcul_two = self.test_number_two +3
        time_result_calcul = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")#models.DateTimeField(auto_now_add=True, blank=True)
        #print(time_result_calcul)
        ##### model PIMS saved as pickle
        pim.result_test_number.append([self.test_number,self.test_number_one,self.test_number_two])#{'test_number':self.test_number,'test_number_one':self.test_number_one,'test_number_two':self.test_number_two})
        #pim.result_test_number.append({'test_number': self.test_number, 'time_test_number': self.time_test_number.strftime("%Y-%m-%d %H:%M:%S")})
        #pim.result_test_number.append({'test_number':self.test_number, 'test_number_one':self.test_number_one, 'test_number_two':self.test_number_two})
        pim.result_number.append([result_calcul,result_calcul_one,result_calcul_two])#{'result_calcul':result_calcul,'result_calcul_one':result_calcul_one,'result_calcul_two':result_calcul_two})
        #pim.result_number.append({'result_calcul':result_calcul,'result_calcul_one':result_calcul_one,'result_calcul_two':result_calcul_two})
        pim.test_result[self.test_number] = {'result_calcul': result_calcul, 'time_result_calcul': time_result_calcul}#self.time_test_number}
        new_model(args=pim).save()
        #####
        return result_calcul, result_calcul_one, result_calcul_two


    @property
    def multiple_ten(self):
        return self.test_number * 10

    #def log(x):
    #    return math.log(x)

    #@property
    #def increment(self, *args, **kwargs):
    #    self.test_number = self.test_number + 1
    #    #self.save()
    #    super().save(*args, **kwargs)
    #    return self.test_number

    def calc(self, *args, **kwargs):
        #resul_calcul = self.calcul
        '''
        time_result_calcul = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")#models.DateTimeField(auto_now_add=True, blank=True)
        #print(time_result_calcul)
        ##### model PIMS saved as pickle
        pim.result_test_number.append(self.test_number)
        #pim.result_test_number.append({'test_number': self.test_number, 'time_test_number': self.time_test_number.strftime("%Y-%m-%d %H:%M:%S")})
        pim.result_number.append(resul_calcul)
        pim.test_result[self.test_number] = {'result_calcul': resul_calcul, 'time_result_calcul': time_result_calcul}#self.time_test_number}
        new_model(args=pim).save()
        #####
        '''
        self.test_number = self.calcul[0]
        self.test_number_one = self.calcul[1]
        self.test_number_two = self.calcul[2]
        #self.test_number = resul_calcul
        #super().save(*args, **kwargs)
        return self.test_number, self.test_number_one, self.test_number_two

    def save(self, *args, **kwargs):
        #self.test_number = self.calcul()
        super().save(*args, **kwargs)


##### save as dictionary
#class Dicty(models.Model):
#    name      = models.CharField(max_length=50)
#
#class KeyVal(models.Model):
#    container = models.ForeignKey(Dicty, db_index=True)
#    key       = models.CharField(max_length=240, db_index=True)
#    value     = models.CharField(max_length=240, db_index=True)

##### save as json
#from jsonfield import JSONField
#class MyModel(models.Model):
#    json = JSONField(null=True)
#
#MyModel.objects.filter(json__isnull=True)

##### save as picke
from django.db import models
from picklefield.fields import PickledObjectField

# Create your models here.
class new_model(models.Model):
    args = PickledObjectField()