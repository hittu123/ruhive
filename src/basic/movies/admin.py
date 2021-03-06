from django.contrib import admin


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Genre, GenreAdmin)


class StudioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Studio, StudioAdmin)


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Movie, MovieAdmin)