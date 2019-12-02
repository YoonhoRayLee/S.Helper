from django.contrib import admin
from .models import Scholarship

# Register your models here.
@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
  list_display = ('name','school','grade','year','credit','income',
                  'impaired','merit','major','regular_decision',
                  'period','benefit','spec','stype')
