from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _
import core.models


class Car(models.Model):
    """
    Klasa samochodu
    """

    name = models.CharField(_("Nazwa"), max_length=50)
    no = models.CharField(_("Rejestracja"), max_length=50)

    def __str__(self):
        return str(f"{self.name} - {self.no}")

    class Meta:

        verbose_name = "Samochód"
        verbose_name_plural = "Samochody"


class Group(models.Model):
    """
    Grupa
    """

    name = models.CharField(_("Nazwa"), max_length=50)
    car = models.OneToOneField(Car, verbose_name=_("Samochód"), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def get_employees(self):
        """
        Zwraca liste przypisanych do grupy pracowników
        """

        return Employee.objects.filter(group=self)

    class Meta:

        verbose_name = "Grupa"
        verbose_name_plural = "Grupy"

    


class EmployeePosition(models.Model):
    """
    Typy użytkowników
    """

    name = models.CharField(
        _("Nazwa"), 
        max_length=50
        )

    color = models.CharField(_("Kolor tekstu i ikony"), max_length=10, help_text="typ HEX", default="#000000")
    bgcolor = models.CharField(_("Kolor tła"), max_length=10, help_text="typ HEX", default="#FF000000")
    icon = models.CharField(_("Ikona"), max_length=200, help_text="typ HTML", blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:

        verbose_name = "Stanowisko"
        verbose_name_plural = "Stanowiska"


class Employee(models.Model):
    """
    Klasa profilu uzytkownika z dodatkowymi parametrami
    """

    user = models.OneToOneField(
        core.models.User, 
        verbose_name=_("Konto pracownika"), 
        on_delete=models.CASCADE, 
        null=True,
        blank=True,
        help_text="Wybierz konto pracownika do podpięcia. Konto musi być zarejestrowane"
        )
    first_name = models.CharField(_("Imię"), max_length=50, blank=True)
    last_name = models.CharField(_("Nazwisko"), max_length=50, blank=True)
    birth_date = models.DateField(_("Data urodzenia"), auto_now=False, auto_now_add=False, null=True, blank=True)
    phone = models.CharField(_("Telefon"), max_length=50, blank=True)
    group = models.ForeignKey(
        Group, verbose_name=_("Grupa"), 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
        )
    position = models.ForeignKey(
        EmployeePosition, 
        verbose_name=_("Stanowisko pracownika"), 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Wybierz profil pracownika"
        )


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def first_last_name(self):
        """
        Zwraca pierwsze i drugie imie razem
        """
        try:
            return f"{self.first_name} {self.last_name}"
        except:
            return

    def has_account(self):
        """
        Zwraca czy pracownik ma konto
        """

        return True if self.user else False

    class Meta:

        verbose_name = "Pracownik"
        verbose_name_plural = "Pracownicy"
    

