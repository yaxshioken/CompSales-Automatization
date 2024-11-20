from django.db import models

class Mahsulot(models.Model):
    nomi = models.CharField(max_length=100)
    tarifi = models.TextField()
    narxi = models.DecimalField(max_digits=10, decimal_places=2)
    miqdori=models.IntegerField()
    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'
    def __str__(self):
        return self.nomi

class Sotuv(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdori = models.IntegerField()
    jami_narxi = models.DecimalField(max_digits=10, decimal_places=2)
    sana = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Sotuv'
        verbose_name_plural = 'Sotuvlar'

    def save(self, *args, **kwargs):
        self.jami_narxi = self.jami_narxi * self.miqdori
        super(Sotuv, self).save(*args, **kwargs)
    def __str__(self):
        return f"Sale of {self.mahsulot.nomi} on {self.sana}"
