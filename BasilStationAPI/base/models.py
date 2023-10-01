from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Watered(models.Model):
    note_text = models.CharField("additional notes", max_length=300)
    watered_date = models.DateTimeField("date watered", auto_now_add=True)
    # watered by = models. ForeignKey ("person watering", )
    
    def was_watered_recently (self):
        return self.watered_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        #return "Plant was watered at the {}, message:'{}', ".format(self.watered_date.date(), self.note_text)
        return "Plant with id: {}".format(self.id)