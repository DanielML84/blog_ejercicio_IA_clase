from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Article, AuthorProfile


class PublicBlogTests(TestCase):
	def setUp(self):
		Article.objects.all().delete()
		AuthorProfile.objects.all().delete()
		now = timezone.now()
		self.article = Article.objects.create(
			title='Robots que aprenden',
			slug='robots-que-aprenden',
			excerpt='Una introducción a la robótica adaptativa.',
			body='## Aprender del entorno\n\nLos sensores convierten datos en decisiones.',
			author='Equipo editorial',
			published_at=now,
			status=Article.Status.PUBLISHED,
		)
		self.draft = Article.objects.create(
			title='Próximo experimento',
			slug='proximo-experimento',
			body='Contenido en preparación.',
			author='Equipo editorial',
			status=Article.Status.DRAFT,
		)

	def test_home_lists_published_articles_in_date_order(self):
		older_article = Article.objects.create(
			title='Primeros sensores',
			slug='primeros-sensores',
			body='Una nota anterior.',
			author='Equipo editorial',
			published_at=timezone.now() - timedelta(days=2),
			status=Article.Status.PUBLISHED,
		)

		response = self.client.get(reverse('articles:home'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.article.title)
		self.assertNotContains(response, self.draft.title)
		listed_articles = list(response.context['articles'])
		self.assertEqual(listed_articles, [self.article, older_article])

	def test_home_shows_context_when_no_articles_are_published(self):
		Article.objects.filter(status=Article.Status.PUBLISHED).delete()

		response = self.client.get(reverse('articles:home'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'La primera historia está por llegar.')

	def test_detail_renders_article_headings(self):
		response = self.client.get(self.article.get_absolute_url())

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.article.title)
		self.assertContains(response, '<h2>Aprender del entorno</h2>', html=True)

	def test_drafts_and_missing_articles_return_custom_404(self):
		for slug in (self.draft.slug, 'no-existe'):
			with self.subTest(slug=slug):
				response = self.client.get(reverse('articles:detail', args=[slug]))
				self.assertEqual(response.status_code, 404)
				self.assertContains(response, 'señal perdida', status_code=404)

	def test_about_page_shows_editable_profile(self):
		AuthorProfile.objects.create(
			name='Alex Robótica', bio='Investigo sistemas autónomos.\n\nMe gusta enseñar.'
		)

		response = self.client.get(reverse('articles:about'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Alex Robótica')
		self.assertContains(response, 'Me gusta enseñar.')

	def test_admin_requires_authentication(self):
		response = self.client.get('/admin/')

		self.assertEqual(response.status_code, 302)
		self.assertIn('/admin/login/', response.url)
