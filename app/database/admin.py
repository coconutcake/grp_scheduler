from database.models import Employee
from django.contrib import admin
from django.contrib import admin
from django.utils.translation import gettext as _
import database.models
from django.utils.html import mark_safe
from django.utils.html import format_html
from django.db.models import Q
import core.models
from django import forms

# Register your models here.


class GroupForm(forms.ModelForm):

    userd = forms.ModelMultipleChoiceField(
        queryset=database.models.Employee.objects.all(),
        required=False,
        label="Pracownicy",
        help_text="Wybierz pracowników do podpięcia"
        )

    class Meta:
        model = database.models.Group
        fields = ['name', 'car', 'userd']

    
    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['userd'].initial = database.models.Employee.objects.filter(group=self.instance) #<- pozycje poczatkowe

    def save(self, *args, **kwargs):
        instance = super(GroupForm, self).save(commit=False)
        database.models.Employee.objects.filter(group=self.instance).update(group=None) #<- Zerowanie przypisanych grup do Employee
        self.cleaned_data['userd'].update(group=instance) #<- Zapisywanie przypisania grup do Employee
        return instance


class EmployeeAdmin(admin.ModelAdmin):
    model = database.models.Employee
    search_fields = ['first_name', 'last_name', 'user', 'phone']
    list_filter = (
        ('position', admin.RelatedOnlyFieldListFilter),
        ('group', admin.RelatedOnlyFieldListFilter),        
    )
    list_display = ['first_last_name', 'user', 'positiond']+\
        [f.name for f in model._meta.get_fields() if f.name not in ['id', 'position', 'user', 'first_name', 'last_name']]+['id']
    readonly_fields = ['superuser']
    fieldsets = (
                ('Ustawienia pracownika', {"fields":('user', 'position',)}),
                ('Dodatkowe', {"fields":('first_name', 'last_name', 'birth_date', 'phone')}),
                ('Przynależność', {"fields":('group',)}),
                ('Uprawnienia', {"fields":('superuser',)}),
                )


    def superuser(self, obj):
        """
        Zwraca czy superuser
        """

        return mark_safe(obj.user.is_superuser)



    def positiond(self, obj):
        try:
            return format_html(f'<span style=\'color:{obj.position.color if obj.position.color else "black;"}\'><b>{obj.position.name}<b><span>')
        except:
            return obj
    positiond.short_description = 'Stanowisko'

    def first_last_name(self, obj):
        """
        Zwraca Imię i Nazwisko razem
        """

        try:
            if obj.first_name or obj.last_name:
                return f"{obj.first_name} {obj.last_name}"
            else:
                return f"{obj.user}"
        except:
            return
    first_last_name.short_description = 'Imię i nazwisko'

    def has_accountd(self,obj):
        try:
            return format_html(f'<span>{"TAK" if obj.has_account() else "NIE"}')
        except:
            return 
admin.site.register(database.models.Employee,EmployeeAdmin)



class EmployeePositionAdmin(admin.ModelAdmin):
    model = database.models.EmployeePosition
    fieldsets = (
                ('Głowne', {"fields":('name',)}),
                ('Wygląd', {"fields":('color', 'bgcolor', 'icon',)}),
                )
admin.site.register(database.models.EmployeePosition,EmployeePositionAdmin)

class EmployeeInline(admin.TabularInline):
    model = Employee


class GroupAdmin(admin.ModelAdmin):
    model = database.models.Group
    form = GroupForm
    list_display = ['name', 'get_car', 'get_employees_names', 'id']
    fieldsets = (
                ('Głowne', {"fields":('name', 'car','userd')}),
                )

    def get_employees_names(self, obj):
        """
        Zwraca imiona przypisanych pracowników
        """

        try:
            return ", ".join([f"{f.first_name} {f.last_name}" for f in obj.get_employees()])
        except:
            return
    get_employees_names.short_description = 'Przypisani pracownicy'

    def get_car(self, obj):
        try:
            return f"{obj.car}"
        except:
            return
    get_car.short_description = 'Przypisany samochód'
        
        
admin.site.register(database.models.Group,GroupAdmin)


class CarAdmin(admin.ModelAdmin):
    model = database.models.Group
    search_fields = ['no', 'name']
    list_display = ['no', 'name', 'id']
    fieldsets = (
                ('Głowne', {"fields":('name', 'no',)}),
                )
admin.site.register(database.models.Car,CarAdmin)