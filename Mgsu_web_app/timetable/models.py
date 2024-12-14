from django.db import models

# Create your models here.
from django.utils import timezone
 
class Timetable(models.Model): # Создаём новый класс, который будет служить для блога моделью, указывая все необходимые элементы.
   week_type = models.CharField(max_length=30)#Чётность недели
   time_range = models.CharField(max_length=30)#Время пары Пример: (10:00 11:20)
   subject_name = models.CharField(max_length=300) #Название пары
   subject_type = models.CharField(max_length=30)#Вид пары
   teacher = models.CharField(max_length=200)#Преподаватель
   location = models.CharField(max_length=100)#Место проведения


   def __str__(self): # С помощью функции меняем то, как будет представлена запись в модели.
       return self.subject_name # Указываем, что она будет идентифицироваться с помощью своего заголовка.
'''
   class Meta:
       verbose_name_plural = "Timetables" # Указываем правильное написание для множественного числа слова Timetable.   

'''