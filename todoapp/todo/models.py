from django.db import models

# Create your models here.


class Tasks(models.Model):
    Task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    task_condition = models.BooleanField()

    def __str__(self):
        return self.Task_text
