from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField


class HomePage(Page):
    warn_text = RichTextField(blank=True)
    limbs = models.JSONField(default=list,blank=True)

    content_panels = Page.content_panels + ["warn_text","limbs"]