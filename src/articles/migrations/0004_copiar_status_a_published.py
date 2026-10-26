from django.db import migrations


def status_a_published(apps, schema_editor):
    Article = apps.get_model('articles', 'Article')
    Article.objects.filter(status='published').update(published=True)


def published_a_status(apps, schema_editor):
    Article = apps.get_model('articles', 'Article')
    Article.objects.filter(published=True).update(status='published')
    Article.objects.filter(published=False).update(status='draft')


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_published'),
    ]

    operations = [
        migrations.RunPython(status_a_published, published_a_status),
    ]