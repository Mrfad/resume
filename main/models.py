from django.db import models

class About(models.Model):
    header = models.TextField()
    img = models.ImageField(upload_to="profile/", null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    githublink = models.CharField(max_length=250, null=True, blank=True)
    bday = models.DateField()
    website = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    freelance = models.CharField(max_length=100)
    long_description = models.TextField()

    def __str__(self):
        return self.title


class SkillType(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    type = models.ForeignKey(SkillType, null=True, blank=True, on_delete=models.CASCADE)
    level = models.IntegerField()

    def __str__(self):
        return self.name

class FactDescription(models.Model): 
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.description

class Fact(models.Model):
    fact_name = models.CharField(max_length=150, null=True, blank=True)
    icon = models.CharField(max_length=150, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.fact_name


class ExperienceDEtail(models.Model):
    duty = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.duty


class Experience(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    from_year = models.DateField(null=True, blank=True)
    to_year = models.DateField(null=True, blank=True)
    present = models.CharField(max_length=50, null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    duty = models.ManyToManyField(ExperienceDEtail)

    def __str__(self):
        return self.title

class College(models.Model):
    college_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.college_name

class Certification(models.Model):
    cert_name = models.CharField(max_length=250, null=True, blank=True)
    cert_date = models.CharField(max_length=250, null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.cert_name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name
