
from django.db import models

# Create your models here.

class Course(models.Model):
    course=models.CharField(max_length=25)
    def __str__(self):
        return self.course


class Company(models.Model):
    company=models.CharField(max_length=20)
    address1=models.CharField(max_length=20)
    address2=models.CharField(max_length=20)
    phone=models.PositiveIntegerField()
    email=models.EmailField(max_length=60)
    website=models.CharField(max_length=20)
    logo=models.ImageField(upload_to="logos")
    def __str__(self):
        return self.company


class State(models.Model):
    state=models.CharField(max_length=25)
    def __str__(self):
        return self.state

class District(models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    district=models.CharField(max_length=25)
    def __str__(self):
        return self.district

class Branch(models.Model):
    branch=models.CharField(max_length=25)
    branchcode=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    street=models.CharField(max_length=30)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=60)
    def __str__(self):
        return self.branch


class Enquiry_source(models.Model):
    enquirysourcename=models.CharField(max_length=30)
    def __str__(self):
        return self.enquirysourcename


class Follow_up_status(models.Model):
    options=(
        ("Yes","Yes"),
        ("No","No")
    )
    followupstatusname=models.CharField(max_length=30)
    followupstatus=models.CharField(choices=options,max_length=20)
    def __str__(self):
        return self.followupstatusname

class Qualification(models.Model):
    qualification=models.CharField(max_length=25)
    def __str__(self):
        return self.qualification

class Batch(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    options=(
        ("trainer1","trainer1"),
        ("trainer2","trainer2"),
        ("trainer3","trainer3")
    )
    trainer=models.CharField(choices=options,max_length=25)
    start_date=models.DateField()
    end_date=models.DateField()
    def __str__(self):
        return self.trainer

class Master_data(models.Model):
    name=models.CharField(max_length=20)
    value=models.CharField(max_length=20)
    type=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Student(models.Model):
    enquirysourcename=models.ForeignKey(Enquiry_source,on_delete=models.CASCADE)
    phone=models.IntegerField()
    # def __str__(self):
    #     return self.phone

class Academic_info(models.Model):
    options=(
        ("2000","2000"),
        ("2001","2001"),
        ("2002","2002"),
        ("2003","2003"),
        ("2004","2004"),
        ("2005","2005"),
        ("2006","2006"),
        ("2007","2008"),
        ("2009","2010"),
        ("2011","2012"),
        ("2013","2013"),
        ("2014","2014"),
        ("2015","2015"),
        ("2016","2016"),
        ("2017","2017"),
        ("2018","2018"),
        ("2019","2019"),
        ("2020","2020"),
        ("2021","2021"),
        ("2022","2022"),
    )
    college_name=models.CharField(max_length=25)
    qualification=models.ForeignKey(Qualification,on_delete=models.CASCADE)
    year_of_pass=models.CharField(choices=options,max_length=15)
    roll_no=models.CharField(max_length=20)
    registration_no=models.CharField(max_length=20)
    def __str__(self):
        return self.college_name

class Personal_info(models.Model):
    options=(
        ("male","male"),
        ("female","female"),
        ("other","other")
    )
    student=models.CharField(max_length=20)
    email=models.EmailField(max_length=60)
    address=models.CharField(max_length=25)
    dob=models.DateField
    street=models.CharField(max_length=25)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    pincode=models.CharField(max_length=25)
    gender=models.CharField(choices=options,max_length=20)
    alternative_email=models.EmailField(max_length=25)
    alternative_address=models.CharField(max_length=25)
    mobile=models.IntegerField
    city=models.CharField(max_length=25)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    whatsapp=models.IntegerField
    def __str__(self):
        return self.student


# Create your models here.
