# coding: utf-8
import os

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangocms_easy_gallery.models import EasyGalleryPlugin, Album


class CMSEasyGalleryPlugin(CMSPluginBase):
    model = EasyGalleryPlugin
    name = _('Easy Gallery')
    render_template = 'djangocms_easy_gallery/default.html'
    change_form_template = "djangocms_easy_gallery/plugins/eg_plugin_change_form.html"
    text_enabled = True
    admin_preview = True
    fieldsets = (
        (None, {
            'fields': (('album', 'template'),),
        }),
    )

    def _extra(self):
        return {
            'albums': Album.objects.all(),
        }

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(self._extra())
        return super(CMSEasyGalleryPlugin, self).add_view(request, form_url, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(self._extra())
        return super(CMSEasyGalleryPlugin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'images': instance.images,
        })
        self.render_template = os.path.join('djangocms_easy_gallery', instance.template)
        return context

plugin_pool.register_plugin(CMSEasyGalleryPlugin)
