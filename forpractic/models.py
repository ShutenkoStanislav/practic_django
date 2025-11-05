from django.db import models


class Ganre(models.Model):
    ganre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.ganre

class Games(models.Model):
    title = models.CharField(max_length=256)
    conn = models.ManyToManyField(Ganre)
    year = models.IntegerField()
    rating = models.DecimalField(decimal_places=2, max_digits=5)




# Створіть Django модель для системи управління
# персональною колекцією ігор. Кожна гра повинна мати
# назву, жанр (використовуйте Many-to-Many відносини),
# рік випуску та рейтинг. Створіть кілька екземплярів жанрів
# та ігор.
