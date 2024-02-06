from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CourseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.course'
    verbose_name = _('course')
