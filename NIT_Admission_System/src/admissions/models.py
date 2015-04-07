from django.db import models

# Create your models here

class Student(models.Model):
  rno = models.IntegerField("JEE(Main) Roll No.")
  rank = models.IntegerField("JEE(Main) Rank")

class SemFee(models.Model):
  year = models.IntegerField("Current Year")
  dasa = models.IntegerField("DASA/SAARC Fees")
  daysch = models.IntegerField("Day-Scholar Fees")
  hostel = models.IntegerField("Hosteller Fees")
