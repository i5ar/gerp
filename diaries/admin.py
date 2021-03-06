from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.forms import Textarea, TextInput

from schedule.models.events import Event
from schedule.models.calendars import Calendar
from schedule.models.rules import Rule

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register)

from .models import ExamEvent, Contact, Attached, RegistrationEvent


@admin.register(ExamEvent)
class ExamEventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "registration",
        "address",
        "start",
        "submitted")

    def get_ordering(self, request):
        """Order by start exam."""
        return ['start']


class ExamEventInline(admin.TabularInline):
    model = ExamEvent
    extra = 1


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class AttachedInline(admin.TabularInline):
    model = Attached
    extra = 1


@admin.register(RegistrationEvent)
class RegistrationEventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "address",
        "description",
        "view_website",
        "view_attached_count",
        "cost",
        "end",
        "submitted")
    list_editable = ('cost', )
    search_fields = ['address']
    inlines = [AttachedInline, ContactInline, ExamEventInline]

    # NOTE: Override text input size in the list views
    formfield_overrides = {
        models.FloatField: {'widget': TextInput(attrs={'size': 8})},
    }

    def view_website(self, instance):
        """Truncate anchor."""
        return '<a href="{0}" target="_blank">{0:.32}...</a>'.format(
            instance.website)
    view_website.allow_tags = True
    view_website.short_description = _("Website")

    def view_attached_count(self, instance):
        """Count attached files."""
        attached_count = Attached.objects.filter(registration=instance).count()
        return '{}'.format(attached_count)
    view_attached_count.short_description = _("Attachments")

    def get_ordering(self, request):
        """Order by end and submitted status."""
        return ['end', 'submitted']


class EventWagtailAdmin(ModelAdmin):
    model = Event
    list_display = (
        'title', 'start', 'end', 'creator', 'updated_on', 'calendar', 'rule')
    list_filter = ('start', 'creator', 'calendar')
    search_fields = ('title', )
    menu_icon = 'tag'


class CalendarWagtailAdmin(ModelAdmin):
    model = Calendar
    list_display = ('name', 'slug')
    menu_icon = 'date'


class RuleWagtailAdmin(ModelAdmin):
    model = Rule
    list_filter = ('frequency', )
    list_display = ('name', 'frequency')
    menu_icon = 'locked'


class DiariesWagtailAdminGroup(ModelAdminGroup):
    items = (
        EventWagtailAdmin,
        CalendarWagtailAdmin,
        RuleWagtailAdmin)
    menu_icon = 'date'


modeladmin_register(DiariesWagtailAdminGroup)
