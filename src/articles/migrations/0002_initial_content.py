from django.db import migrations
from django.utils import timezone


def add_initial_content(apps, schema_editor):
    Article = apps.get_model('articles', 'Article')
    AuthorProfile = apps.get_model('articles', 'AuthorProfile')

    Article.objects.get_or_create(
        slug='como-perciben-el-mundo-los-robots',
        defaults={
            'title': 'Cómo perciben el mundo los robots',
            'excerpt': 'Sensores, señales y decisiones: una mirada a la percepción robótica.',
            'body': (
                'Un robot no ve el mundo como nosotros. Lo interpreta a partir de '
                'mediciones: distancias, imágenes, temperatura y movimiento.\n\n'
                '## De la señal a la decisión\n\n'
                'Cada sensor aporta una pieza distinta. Una cámara reconoce formas; '
                'un sensor de distancia calcula cuánto falta para un obstáculo; una '
                'unidad inercial estima cómo se está moviendo el sistema.\n\n'
                'El trabajo interesante ocurre al combinar esas señales. El robot '
                'construye una representación útil de su entorno y la actualiza '
                'cuando recibe nuevos datos.\n\n'
                '## Percibir también es aprender\n\n'
                'La percepción no consiste solo en registrar información. También '
                'hay que decidir qué datos son relevantes para la tarea. Un robot '
                'móvil, por ejemplo, necesita distinguir un camino libre de una '
                'zona que debe evitar.\n\n'
                'Por eso, diseñar robots capaces empieza con preguntas sencillas: '
                'qué necesitan detectar, con qué precisión y en cuánto tiempo.'
            ),
            'author': 'Equipo editorial',
            'published_at': timezone.now(),
            'status': 'published',
        },
    )
    AuthorProfile.objects.get_or_create(
        name='Autor del blog',
        defaults={
            'bio': (
                'Este espacio comparte notas y descubrimientos sobre robótica. '
                'La presentación puede reemplazarse desde Django Admin.'
            ),
        },
    )


def remove_initial_content(apps, schema_editor):
    Article = apps.get_model('articles', 'Article')
    AuthorProfile = apps.get_model('articles', 'AuthorProfile')
    Article.objects.filter(slug='como-perciben-el-mundo-los-robots').delete()
    AuthorProfile.objects.filter(name='Autor del blog').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_content, remove_initial_content),
    ]