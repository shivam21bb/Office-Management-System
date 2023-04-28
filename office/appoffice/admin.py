from django.contrib import admin

# Register your models here.
from .models import Employee,Role,Department

admin.site.register(Role)
admin.site.register(Department)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','dept','salarly','bonus','role','phone','hire_date']
admin.site.register(Employee,EmployeeAdmin)