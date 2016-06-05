from __future__ import unicode_literals

from django.db import models

plot_func = {'scatter': lambda self: self.objects.all()}

class Chartable(models.Model):
    @classmethod
    def chart(self, plot='scatter'):
        return plot_func[plot](self)
    class Meta:
        abstract = True
