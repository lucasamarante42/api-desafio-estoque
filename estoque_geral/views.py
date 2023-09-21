from rest_framework.generics import GenericAPIView
from .mixins import CreateMultipleObjectMixin, UpdateMultipleObjectMixin

from django.http import HttpResponse
from oauth2_provider.views.base import TokenView
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from oauth2_provider.models import get_access_token_model
from oauth2_provider.signals import *
import json
from django.conf import settings

__all__ = [
	'MultiObjectCreateAPIView',
	'MultiObjectUpdateDestroyAPIView',
]

"""
View para criação de múltiplos objetos
"""
class MultiObjectCreateAPIView(CreateMultipleObjectMixin, GenericAPIView):

	def post(self, request, *args, **kwargs):
		return self.create_bulk(request, *args, **kwargs)

"""
View para atualização de múltiplos objetos
"""
class MultiObjectUpdateDestroyAPIView(UpdateMultipleObjectMixin, GenericAPIView):

	bussiness_class = None

	def put(self, request, *args, **kwargs):
		return self.update_bulk(request, *args, **kwargs)

	def patch(self, request, *args, **kwargs):
		kwargs['partial'] = True
		return self.update_bulk(request, *args, **kwargs)

"""
@override da View de requisição do Token
"""
class CustomTokenView(TokenView):

	@method_decorator(sensitive_post_parameters('password'))
	def post(self, request, *args, **kwargs):

		request.POST = request.POST.copy()
		request.POST['client_id'] = settings.API_CLIENT_ID
		request.POST['client_secret'] = settings.API_CLIENT_SECRET
		request.POST['grant_type'] = 'password'
		request.POST['scope'] = 'read write groups'

		url, headers, body, status = self.create_token_response(request)

		if status == 200:
			body = json.loads(body)
			access_token = body.get('access_token')
			if access_token is not None:
				token = get_access_token_model().objects.get(token=access_token)

				app_authorized.send(
					sender=self, request=request,
					token=token)

				if hasattr(token, 'user'):
					if token.user.is_active:
						body['user'] = {
							'id': token.user.id,
							'username': token.user.username,
							'email': token.user.email,
							'first_name': token.user.first_name,
							'last_name': token.user.last_name,
							'admin': token.user.is_superuser,
							'staff': token.user.is_staff,
							'ativo': token.user.is_active
						}

						if 'expires_in' in body:
							del body['expires_in']

						if 'refresh_token' in body:
							del body['refresh_token']

						if 'scope' in body:
							del body['scope']

						if 'token_type' in body:
							del body['token_type']
					else:
						body = {}
						status = 403
						body['message'] = 'O usuário não está ativo.'

					body = json.dumps(body)

		response = HttpResponse(content=body, status=status)
		for k, v in headers.items():
			response[k] = v
		return response