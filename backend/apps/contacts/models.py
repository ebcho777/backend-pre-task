from django.db import models



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    profile_photo_url = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ['id']


class Label(models.Model):
    name = models.CharField(max_length=100, verbose_name="라벨명")
    contact = models.ForeignKey(Contact, related_name='labels', on_delete=models.CASCADE, verbose_name="연락처")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "label"
        verbose_name_plural = "labels"
        unique_together = ('contact', 'name')