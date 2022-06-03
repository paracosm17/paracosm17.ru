# Generated by Django 4.0.4 on 2022-05-15 12:31

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_aboutpage_cvpage_homepage_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutpage',
            options={'verbose_name': 'Страница About', 'verbose_name_plural': 'Страницы About'},
        ),
        migrations.AlterModelOptions(
            name='cvpage',
            options={'verbose_name': 'Страница CV', 'verbose_name_plural': 'Страницы CV'},
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Главная страница', 'verbose_name_plural': 'Главные страницы'},
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='body',
        ),
        migrations.RemoveField(
            model_name='cvpage',
            name='body',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='contacts',
            field=wagtail.core.fields.StreamField([('contact', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.URLBlock(label='Ссылка на ресурс')), ('name', wagtail.core.blocks.CharBlock(label='Название ресурса', max_length=128))]))], blank=True, verbose_name='Контакты'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='text',
            field=wagtail.core.fields.RichTextField(default='Something about me.', verbose_name='Рассказ о себе'),
        ),
        migrations.AddField(
            model_name='cvpage',
            name='born_city',
            field=models.CharField(default='Moscow', max_length=128, verbose_name='Название города'),
        ),
        migrations.AddField(
            model_name='cvpage',
            name='born_country',
            field=models.CharField(default='Russia', max_length=128, verbose_name='Название страны'),
        ),
        migrations.AddField(
            model_name='cvpage',
            name='born_link',
            field=models.URLField(default='https://en.wikipedia.org/wiki/Moscow', verbose_name='Ссылка на город'),
        ),
        migrations.AddField(
            model_name='cvpage',
            name='extra',
            field=wagtail.core.fields.StreamField([('extra', wagtail.core.blocks.StructBlock([('extra_parent', wagtail.core.blocks.CharBlock(label='Тема', max_length=32)), ('extra_child', wagtail.core.blocks.CharBlock(label='Дополнительная информация', max_length=256))]))], blank=True, verbose_name='Дополнительная информация'),
        ),
        migrations.AddField(
            model_name='cvpage',
            name='skills',
            field=wagtail.core.fields.StreamField([('skill', wagtail.core.blocks.StructBlock([('skill_parent', wagtail.core.blocks.CharBlock(label='Область', max_length=32)), ('skill_child', wagtail.core.blocks.CharBlock(label='Темы в области', max_length=256))]))], blank=True, verbose_name='Скиллы'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='name',
            field=models.CharField(default='John Doe', max_length=128, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='profession',
            field=models.CharField(default='Developer.', max_length=128, verbose_name='Род деятельности'),
        ),
    ]