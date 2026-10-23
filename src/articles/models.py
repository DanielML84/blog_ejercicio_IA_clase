from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Article(models.Model):
	class Status(models.TextChoices):
		DRAFT = 'draft', 'Borrador'
		PUBLISHED = 'published', 'Publicado'

	title = models.CharField('título', max_length=180)
	slug = models.SlugField('URL', max_length=200, unique=True, blank=True)
	excerpt = models.CharField('extracto', max_length=300, blank=True)
	body = models.TextField('contenido en Markdown')
	author = models.CharField('autoría', max_length=120)
	published_at = models.DateTimeField('fecha de publicación', default=timezone.now)
	status = models.CharField(
		'estado', max_length=12, choices=Status.choices, default=Status.DRAFT
	)
	image = models.ImageField('imagen', upload_to='articles/', blank=True)
	image_alt = models.CharField('texto alternativo', max_length=180, blank=True)
	created_at = models.DateTimeField('creado', auto_now_add=True)
	updated_at = models.DateTimeField('actualizado', auto_now=True)

	class Meta:
		ordering = ['-published_at', '-created_at']
		verbose_name = 'artículo'
		verbose_name_plural = 'artículos'

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			base_slug = slugify(self.title) or 'articulo'
			candidate = base_slug
			suffix = 2
			while Article.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
				candidate = f'{base_slug}-{suffix}'
				suffix += 1
			self.slug = candidate
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('articles:detail', kwargs={'slug': self.slug})

	@property
	def summary(self):
		if self.excerpt:
			return self.excerpt
		from django.utils.html import strip_tags
		from markdown import markdown

		return ' '.join(strip_tags(markdown(self.body)).split())[:220]


class AuthorProfile(models.Model):
	name = models.CharField('nombre', max_length=120)
	bio = models.TextField('presentación')
	updated_at = models.DateTimeField('actualizado', auto_now=True)

	class Meta:
		verbose_name = 'presentación del autor'
		verbose_name_plural = 'presentación del autor'

	def __str__(self):
		return self.name
