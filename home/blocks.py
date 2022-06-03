from wagtail.core import blocks

class ContactBlock(blocks.StructBlock):
    """Contact block"""

    link = blocks.URLBlock(label='Ссылка на ресурс')
    name = blocks.CharBlock(max_length=128, label='Название ресурса')
    
    class Meta:
        """Meta information."""
        template = 'blocks/contact_block.html'
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        icon = 'user'

class SkillBlock(blocks.StructBlock):
    """Skills block"""

    skill_parent = blocks.CharBlock(max_length=32, label='Область')
    skill_child = blocks.CharBlock(max_length=256, label='Темы в области')
    
    class Meta:
        """Meta information."""
        template = 'blocks/skill_block.html'
        verbose_name = 'Скилл'
        verbose_name_plural = 'Скилы'
        icon = 'order_up'  

class ExtraBlock(blocks.StructBlock):
    """Extra block"""

    extra_parent = blocks.CharBlock(max_length=32, label='Тема')
    extra_child = blocks.CharBlock(max_length=256, label='Дополнительная информация')
    
    class Meta:
        """Meta information."""
        template = 'blocks/extra_block.html'
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = 'Дополнительная информация'
        icon = 'snippet'
