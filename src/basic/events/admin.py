from django.contrib import admin


class EventTimeInline(admin.StackedInline):
    model = EventTime
    fk = 'event'


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'place', 'created')
    inlines = [
        EventTimeInline
    ]
admin.site.register(Event, EventAdmin)