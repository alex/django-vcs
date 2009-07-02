from django.contrib import admin

from django_vcs.models import CodeRepository

class CodeRepositoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(CodeRepository, CodeRepositoryAdmin)
