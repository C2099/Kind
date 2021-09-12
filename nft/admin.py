from django.contrib import admin
from . import models


# Register your models here.
class NFTContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'image')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name','group_id', 'nft', 'image',)


admin.site.register(models.NFTContract, NFTContractAdmin)
admin.site.register(models.Group, GroupAdmin)
