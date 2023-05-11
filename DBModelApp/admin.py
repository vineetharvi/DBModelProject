from django.contrib import admin
from DBModelApp.models import Employee

# Register your models here...
admin.site.register(Employee)
admin.site.register(EmployeeAdmin)
#admin.site.register(Employee);
#model(table) for adming-interface but-not mysql-table

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr'];

    admin.site.register(Employee,EmployeeAdmin);