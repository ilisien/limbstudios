from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

class PageWMsgs(Page):
    info_text = RichTextField(blank=True)
    warn_text = RichTextField(blank=True)
    err_text = RichTextField(blank=True)

    content_panels = Page.content_panels + ["info_text","warn_text","err_text"]

    class Meta:
        abstract = True

class HomePage(PageWMsgs):
    limbs = models.JSONField(default=list,blank=True)

    content_panels = PageWMsgs.content_panels + ["limbs"]