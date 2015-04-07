from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from admissions.models import Student, SemFee
from datetime import datetime

def calc_fee(obj):
    refobj = SemFee.objects.get(year = datetime.now().year)
    if obj.category == "DA":
        obj.fees = refobj.dasa
    if obj.category == "GH":
        obj.fees = refobj.hostel
    if obj.category == "GD":
        obj.fees = refobj.daysch
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
    rno = models.IntegerField("JEE(Main) Roll No.", default=0)
    rank = models.IntegerField("JEE(Main) Rank", default=0)
    branch = models.CharField("Branch Chosen", max_length=200, choices=BRANCH_LIST, default='NC')
    CATEGORY_LIST = (('GD', 'Day Scholar'),
                     ('GH', 'Hosteller'),
                     ('DA', 'DASA/SAARC'),
                    )
    category = models.CharField("Student Category", max_length=30, choices=CATEGORY_LIST, default='GH')
    fees = models.IntegerField("Fees To Be Payed", default=0)
    
    
    def is_eligible(self):
        for e in Student.objects.all():
            if e.rno == self.rno and e.rank ==self.rank:
              self = calc_fee(self)
              return True
        return False
    is_eligible.boolean = True
    is_eligible.short_description = "Eligible?"

    '''def calc_fee(obj):
        refobj = SemFee.objects.get(year = datetime.now().year)
        if obj.category == "DA":
            obj.fees = refobj.dasa
        if obj.category == "GH":
            obj.fees = refobj.hostel
        if obj.category == "GD":
            obj.fees = refobj.daysch
        return obj'''
            
    
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
