from django.db import models


from django.utils import timezone
 
 
class Todos(models.Model):

    user_id = models.IntegerField(blank=True, null=True)
    todo = models.CharField(max_length=100)
    todolist = models.TextField()
    
 
    class Meta:
        db_table='todo'