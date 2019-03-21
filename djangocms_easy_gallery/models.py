# coding: utf-8
import glob
import os

from django.conf import settings
from django.db import models
from django.template.loaders.app_directories import get_app_template_dirs
from django.utils.translation import ugettext, ugettext_lazy as _

from cms.models import CMSPlugin
from filer.fields.file import FilerFileField
from filer.fields.folder import FilerFolderField
from filer.fields.image import FilerImageField


def get_templates():
    templates = []
    dirs_to_scan = []

    for dir in get_app_template_dirs('templates'):
        dirs = [os.path.join(dir, name) for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name)) and name == 'djangocms_easy_gallery']
        if dirs:
            dirs_to_scan.extend(dirs)

    for dir in settings.TEMPLATES[0]['DIRS']:
        dirs = [os.path.join(dir, name) for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name)) and name == 'djangocms_easy_gallery']
        if dirs:
            dirs_to_scan.extend(dirs)
                
    for dir in dirs_to_scan:
        files = glob.glob(os.path.join(dir, '*.html'))
        for file in files:
            dir, file = os.path.split(file)
            templates.append((file, file))

    return templates


TEMPLATE_CHOICES = get_templates()


class Album(models.Model):
    title = models.CharField(verbose_name=_(u'Title'), max_length=255)

    class Meta:
        verbose_name = _('Album')
        verbose_name_plural = _('Albums')

    def __unicode__(self):
        return unicode(self.title)

    def get_meta(self):
        return self._meta

    @property
    def images(self):
        files = self.image_set.all()
        return [f.image for f in files if f.image.file_type == 'Image']

    @property
    def images_admin_preview(self):
        return self.images[:4]


class Image(models.Model):
    image = FilerImageField(verbose_name=_(u'Image'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    album = models.ForeignKey(Album)

    class Meta:
        ordering = ('order',)
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __unicode__(self):
        return u'%s %s' % (self.pk, self.album.title)


class EasyGalleryPlugin(CMSPlugin):
    album = models.ForeignKey(Album)
    template = models.CharField(
        _('template'),
        choices=TEMPLATE_CHOICES,
        max_length=255,
        default='default.html',
    )

    def __unicode__(self):
        return unicode(self.album.title)

    @property
    def images(self):
        files = self.album.image_set.all()
        self.__images = [f.image for f in files if f.image.file_type == 'Image']
        return self.__images
