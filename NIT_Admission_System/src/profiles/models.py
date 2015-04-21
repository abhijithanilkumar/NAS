from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from admissions.models import Student, SemFee
from datetime import datetime

def calc_fee(obj):
    refobj = SemFee.objects.get(cat = obj.category)
    obj.tutfee = refobj.tutfee
    obj.libfee = refobj.libfee
    obj.cccfee = refobj.cccfee
    obj.sacfee = refobj.sacfee
    obj.insufee = refobj.insufee
    obj.secfee = refobj.secfee
    obj.devfee = refobj.devfee
    obj.convofee = refobj.convofee
    obj.poolfee = refobj.poolfee
    obj.camdevfee = refobj.camdevfee
    obj.alumfee = refobj.alumfee
    if obj.category2 == "GD":
        obj.admfee = 0
        obj.rent = 0
    else:
        obj.admfee = refobj.admfee
        obj.rent = refobj.rent
    if obj.category2 == "DA":
        obj.dasa = refobj.dasa
    else:
        obj.dasa = 0
    obj.totfee = obj.tutfee + obj.libfee + obj.cccfee + obj.sacfee + obj.insufee + obj.secfee + obj.devfee + obj.convofee + obj.poolfee + obj.camdevfee + obj.alumfee + obj.admfee + obj.rent + obj.dasa
    return obj

class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    slug = models.SlugField(max_length=32, unique=True, blank=True,
                            editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    challan = models.ImageField('Challan', upload_to='profile_pics/%Y-%m-%d/',null=True,blank=True)
    BRANCH_LIST = (('NC', 'Not Chosen'),
                   ('CH', 'Chemical Engineering'),
                   ('CO', 'Computer Engineering'),
                   ('CV', 'Civil Engineering'),
                   ('EC', 'Electronics and Communications Engineering'),
                   ('EE', 'Elelctrical and Electronics Engineering'),
                   ('IT', 'Information Technology'),
                   ('ME', 'Mechanical Engineering'),
                   ('MN', 'Mining Engineering'),
                   ('MT', 'Materials and Metallurgical Engineering'),
                   )
    rno = models.IntegerField("JEE(Main) Roll No.", null=True,  blank=True)
    rank = models.IntegerField("JEE(Main) Rank", null=True, blank=True)
    branch = models.CharField("Branch Chosen", max_length=50, choices=BRANCH_LIST, null=True, blank=True)
    CATEGORY_LIST = (('GN', 'Gen/OBC'),
                     ('SC', 'SC/ST'),
                    )
    CATEGORY_LIST_2 = (('GD', 'Day Scholar'),
                     ('GH', 'Hosteller'),
                     ('DA', 'DASA/SAARC'),
                    )
    category = models.CharField("Category", max_length=30, choices=CATEGORY_LIST, default='GN')
    category2 = models.CharField("Student Category", max_length=30, choices=CATEGORY_LIST_2, default='GH')
    
    tutfee = models.IntegerField("Tution Fees", null=True, blank=True)     
    libfee = models.IntegerField("Library Fees",null=True, blank=True)                                                          
    cccfee = models.IntegerField("Central Computing Facility Fees",null=True, blank=True)                                       
    sacfee = models.IntegerField("Student Activities Fee",null=True, blank=True)                                                
    insufee = models.IntegerField("Group Insturance Coverage of Students",null=True, blank=True)                               
    secfee = models.IntegerField("Security Deposit (Refundable)",null=True, blank=True)                                         
    devfee = models.IntegerField("Institute Development Contribution",null=True, blank=True)                                    
    convofee = models.IntegerField("Convocation Fee",null=True, blank=True)
    poolfee = models.IntegerField("Swimming Pool Fee",null=True, blank=True)                                                    
    camdevfee = models.IntegerField("Campus Development Fee",null=True, blank=True)
    alumfee = models.IntegerField("Alumni Association",null=True, blank=True)                                                   
    admfee = models.IntegerField("Hostel Admission Fee",null=True, blank=True)                                                  
    rent = models.IntegerField("Hostel Rent",null=True, blank=True)
    totfee = models.IntegerField("Total Amount to be Payed",null=True, blank=True)
    dasa = models.IntegerField("Dasa Fee",null=True, blank=True)

    def is_eligible(self):
        for e in Student.objects.all():
            if e.rno == self.rno and e.rank ==self.rank:
              self = calc_fee(self)
              return True
        return False
    is_eligible.boolean = True
    is_eligible.short_description = "Eligible?"

            
    
    email_verified = models.BooleanField("Email Verified", default=False)

    def save(self, *args, **kwargs):
        if self.slug is None or len(self.slug) == 0:
            self.slug = uuid.uuid4().hex
        super(BaseProfile, self).save(*args, **kwargs)
    class Meta:
        abstract = True
  
@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)
