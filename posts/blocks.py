from wagtail.core import blocks

class PythonCodeBlock(blocks.StructBlock):
    code = blocks.TextBlock()

    class Meta:
        template = 'blocks/python_code_block.html'
        verbose_name = 'Python код'
        verbose_name_plural = 'Python код'
        icon = 'code'
        