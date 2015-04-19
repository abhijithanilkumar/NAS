from django.contrib import admin
from .models import Student, SemFee

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
  list_display = ['rno', 'rank']
 
class SemFeeAdmin(admin.ModelAdmin):
  list_display = ['cat', 'tutfee', 'admfee']

admin.site.register(Student, StudentAdmin)
admin.site.register(SemFee, SemFeeAdmin)
