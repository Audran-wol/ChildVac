from django.db import models


class Slider(models.Model):
    caption = models.CharField(max_length=150)
    slogan = models.CharField(max_length=120)
    image = models.ImageField(upload_to='sliders/')

    def __str__(self):
        return self.caption[:20]

    class Meta:
        verbose_name_plural = 'Slider'


class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    items = models.ManyToManyField(to='Item',)
    thumbnail = models.ImageField(upload_to='services/')
    cover = models.ImageField(upload_to='services/')
    image1 = models.ImageField(upload_to='services/', blank=True, null=True)
    image2 = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class Child(models.Model):
    name = models.CharField(max_length=120)
    parent_name = models.CharField(max_length=120)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    picture = models.ImageField(upload_to="children/", blank=True, null=True)

    def __str__(self):
        return self.name
    


class Doctor(models.Model):
    name = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)
    picture = models.ImageField(upload_to="doctors/")
    details = models.TextField()
    experience = models.TextField()
    expertize = models.ManyToManyField(to='Expertize', related_name='doctors')
    twitter = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    instagram = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name

class Vaccination(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='vaccinations')
    vaccine = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='vaccinations')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='vaccinations')
    date = models.DateField()

    def __str__(self):
        return f"{self.vaccine.title} for {self.child.name} at {self.doctor.name}"

class Expertize(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=120)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Gallery(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Galleries"
