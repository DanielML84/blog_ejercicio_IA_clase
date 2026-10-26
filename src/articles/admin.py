from django.contrib import admin

from .models import Article, AuthorProfile


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'published_at', 'published')
	list_filter = ('published', 'published_at')
	search_fields = ('title', 'excerpt', 'body', 'author')
	prepopulated_fields = {'slug': ('title',)}
	date_hierarchy = 'published_at'
	ordering = ('-published_at',)
	fieldsets = (
		(None, {'fields': ('title', 'slug', 'excerpt', 'body')}),
		('Publicación', {'fields': ('author', 'published_at', 'published')}),
		('Imagen', {'fields': ('image', 'image_alt')}),
	)


@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
	def has_add_permission(self, request):
		return not AuthorProfile.objects.exists()
