from django.db import models

# Create your models here

class Student(models.Model):
    rno = models.IntegerField("JEE(Main) Roll No.", unique = True)
    rank = models.IntegerField("JEE(Main) Rank", unique = True)

class SemFee(models.Model):
    CATEGORY_LIST = (('GN', 'Gen/OBC'),      
                       ('SC', 'SC/ST'),            
                      )
    
    cat = models.CharField("Student Category", max_length=30, choices=CATEGORY_LIST, default='GH')
    tutfee = models.IntegerField("Tution Fees", null=True, blank=True)
    libfee = models.IntegerField("Library Fees", null=True, blank=True)
    cccfee = models.IntegerField("Central Computing Facility Fees", null=True, blank=True)
    sacfee = models.IntegerField("Student Activities Fee", null=True, blank=True)
    insufee = models.IntegerField("Group Insturance Converage of Students", null=True, blank=True)
    secfee = models.IntegerField("Security Deposit (Refundable)", null=True, blank=True)
    devfee = models.IntegerField("Institute Development Contribution", null=True, blank=True)
    convofee = models.IntegerField("Convocation Fee", null=True, blank=True)
    poolfee = models.IntegerField("Swimming Pool Fee", null=True, blank=True)
    camdevfee = models.IntegerField("Campus Development Fee", null=True, blank=True)
    alumfee = models.IntegerField("Alumni Association", null=True, blank=True)
    admfee = models.IntegerField("Hostel Admission Fee", null=True, blank=True)
    rent = models.IntegerField("Hostel Rent", null=True, blank=True)
