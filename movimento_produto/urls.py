from django.urls import include, path, re_path
from . import views
from django.conf import settings

path_movimento_produto = '{}/movimento-produto'.format(settings.API_PATH)

urlpatterns = [
	re_path(r'^{}/(?P<pk>[0-9]+)$'.format(path_movimento_produto),
		views.get_delete_update.as_view(),
		name='get_delete_update'
	),
	path(path_movimento_produto,
		views.get_post.as_view(),
		name='get_post'
	)
]