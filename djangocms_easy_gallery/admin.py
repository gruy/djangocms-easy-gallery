# coding: utf-8
from django.contrib import admin
from django.template.response import SimpleTemplateResponse
from django.utils.html import escape, escapejs

from .models import Album, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


class AlbumAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]

    IS_POPUP_VAR = '_popup'
    TO_FIELD_VAR = '_to_field'

    class Media:
        js = (
            'djangocms_easy_gallery/html.sortable.js',
        )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['images'] = Album.objects.get(pk=object_id).images
        return super(AlbumAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def response_change(self, request, obj):
        pk_value = obj._get_pk_val()
        if self.IS_POPUP_VAR in request.POST:
            return SimpleTemplateResponse('admin/djangocms_easy_gallery/popup_response.html', {
                'pk_value': escape(pk_value),
                'obj': escapejs(obj)
            })


class ImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Album, AlbumAdmin)
admin.site.register(Image, ImageAdmin)
