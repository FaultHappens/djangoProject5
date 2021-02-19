from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Ticket(models.Model):
    name = models.CharField(verbose_name=_("Name of event"), max_length=30)
    start_time = models.DateTimeField(verbose_name=_("Start dateTime"))
    end_time = models.DateTimeField(verbose_name=_("End dateTime"))
    # barcode = models.

    def __str__(self):
        return self.name + " " + self.start_time.time()

class Order(models.Model):
    user = models.ForeignKey(to='user.User', verbose_name=_("Related user"), on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2)

