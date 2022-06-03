from django.db import models

from wagtail.core.models import Page
from wagtail.core import fields
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel, MultiFieldPanel
from wagtailmetadata.models import MetadataPageMixin

from home.blocks import ContactBlock, SkillBlock, ExtraBlock

class HomePage(MetadataPageMixin, Page):
    """
    Home page
    """
    name = models.CharField(max_length=128, default="John Doe", blank=False, verbose_name='Имя')
    profession = models.CharField(max_length=128, default="Developer.", blank=False, verbose_name='Род деятельности')

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('profession'),
    ]

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главные страницы'
    
    parent_page_types = []
    subpage_types = ['home.AboutPage', 'home.CvPage', 'posts.PostsIndexPage']


class AboutPage(MetadataPageMixin, Page):
    """
    About page
    """
    text = fields.RichTextField(default="Something about me.", verbose_name='Рассказ о себе')
    contacts = fields.StreamField(block_types=[
        ('contact', ContactBlock())
    ], blank=True, verbose_name='Контакты')
    content_panels = Page.content_panels + [
        FieldPanel('text'),
        StreamFieldPanel('contacts'),
    ]

    class Meta:
        verbose_name = 'Страница About'
        verbose_name_plural = 'Страницы About'
    
    parent_page_types = ['home.HomePage']
    subpage_types = []


class CvPage(MetadataPageMixin, Page):
    """
    CV page
    """
    born_link = models.URLField(default='https://en.wikipedia.org/wiki/Moscow', verbose_name='Ссылка на город')
    born_city = models.CharField(max_length=128, default='Moscow', verbose_name='Название города')
    born_country = models.CharField(max_length=128, default='Russia', verbose_name='Название страны')

    skills = fields.StreamField(block_types=[
        ('skill', SkillBlock())
    ], blank=True, verbose_name='Скиллы')

    extra = fields.StreamField(block_types=[
        ('extra', ExtraBlock())
    ], blank=True, verbose_name='Дополнительная информация')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('born_link', help_text='WikiPedia link to your city'),
            FieldPanel('born_city'),
            FieldPanel('born_country')
        ], heading='Место рождения'),
        StreamFieldPanel('skills', heading='Скиллы'),
        StreamFieldPanel('extra', heading='Дополнительная информация'),
    ]

    class Meta:
        verbose_name = 'Страница CV'
        verbose_name_plural = 'Страницы CV'
    
    parent_page_types = ['home.HomePage']
    subpage_types = []
        
