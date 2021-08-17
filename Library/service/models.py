from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=64,
                            unique=True,
                            verbose_name="nazwa")
    class Meta:
        ordering = ["name",]
        verbose_name = "kategoria"
        verbose_name_plural = "kategorie"
    
    def __str__(self):
        return self.name


class Notice(models.Model):
    title = models.CharField(max_length=128,
                              default="",
                              verbose_name="title",
                              unique=True)
    autor = models.CharField(default="",
                             max_length=128,
                             verbose_name="autor",
                             blank=True)
    description = models.TextField(default="",
                                   blank=True,
                                   verbose_name="opis",)
    
    NEW = "n"
    BESTSELLER = "b"
    COMING = "c"
    STATUSES = [(NEW, "Nowy"),
                (BESTSELLER, "Bestseller"),
                (COMING, "Nadchodzące")]
    status = models.CharField(max_length=1,
                              choices=STATUSES,
                              default=NEW)
    category = models.ForeignKey(Category,
                                 null=True,
                                 blank=True,
                                 on_delete=models.PROTECT,
                                 verbose_name="kategoria",
                                 related_name="notices")
    image = models.ImageField(upload_to="notice/",
                                 null=True,
                                 blank=True,
                                 default="",
                                 verbose_name="obraz")
    
    
    class Meta:
        ordering = ["title"]
        verbose_name = "książkę"
        verbose_name_plural = "książki"
    
    def __str__(self):
        return self.title
    
    def status_name(self):
        for name in self.STATUSES:
            if self.status == name[0]:
                return name[1]
        return "?"
    
    def status_color(self):
        if self.status == self.NEW:
            return "text-warning"
        elif self.status == self.BESTSELLER:
            return "text-success"
        elif self.status == self.COMING:
            return "text-danger"
        return ""


   






