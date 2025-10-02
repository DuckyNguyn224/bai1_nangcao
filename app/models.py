from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='banners/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

from django.utils import timezone

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    # New fields for product categories
    featured = models.BooleanField(default=False)
    flash_deals = models.BooleanField(default=False)
    last_minute = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='team_members/')
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    behance = models.URLField(blank=True)

    def __str__(self):
        return self.name

class ContentSection(models.Model):
    page = models.CharField(max_length=100)
    section_name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.page} - {self.section_name}"
