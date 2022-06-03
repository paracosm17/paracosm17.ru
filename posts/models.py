from django.db import models

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.search import index
from wagtailmetadata.models import MetadataPageMixin

from posts.blocks import PythonCodeBlock

class PostsIndexPage(MetadataPageMixin, Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        context['count'] = len(blogpages)
        return context
    
    class Meta:
        """Meta information."""

        verbose_name = "Посты"
        verbose_name_plural = "Посты"
    
    parent_page_types = ['home.HomePage']
    subpage_types = ['posts.PostPage']

class PostPage(MetadataPageMixin, Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField(block_types=[
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('pythoncode', PythonCodeBlock())
    ], blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
        ], heading="Blog information"),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]

    class Meta:
        """Meta information."""

        verbose_name = "Пост"
        verbose_name_plural = "Посты"
    
    parent_page_types = ['posts.PostsIndexPage']
    subpage_types = []
