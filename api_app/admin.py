from django.contrib import admin
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.utils.html import format_html

from .models import Article
from django.urls import path
# Register your models here.



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','font_size_html_display', 'date')
    list_filter = ('date',)
    change_list_template = "admin/change_admin.html"

  # readonly_fields = ('body_preview',)
    def get_urls(self):
        urls= super().get_urls()
        custom_urls = [
            path('fontsize/<int:size>/', self.change_font_size)
        ]
        return custom_urls + urls


    def change_font_size(self, request,size):
        self.model.objects.all().update(font_size= size)
        self.message_user(request, 'font size done')
        return HttpResponseRedirect("../")

    def font_size_html_display(self,obj):

        return format_html(
            f'<span style="font-size: {obj.font_size}px;"> {obj.font_size}</span>'
        )

admin.site.register(Article,ArticleAdmin )
admin.site.unregister(Group)