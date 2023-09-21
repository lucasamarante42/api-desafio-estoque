
from rest_framework import status
from rest_framework.response import Response
from estoque_geral.utils import default_message_request

__all__ = [
	'CreateMultipleObjectMixin',
	'UpdateMultipleObjectMixin'
]

class CreateMultipleObjectMixin(object):
	"""
    Mixin para criação de múltiplos objetos
    """
	def create_bulk(self, request, *args, **kwargs):
		try:
			data = request.data
			serializer = self.get_serializer(data=data, many=True)

			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		except Exception as e:
			return Response(default_message_request(status.HTTP_500_INTERNAL_SERVER_ERROR), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateMultipleObjectMixin(object):
	"""
    Mixin para atualização de múltiplos objetos
    """
	def update_bulk(self, request, *args, **kwargs):
		try:
			partial = kwargs.pop('partial', False)
			data = request.data
			instances = self.bussiness_class.bs_get_by_ids(data)
			serializer = self.get_serializer(data=data, instance=instances, many=True, partial=partial)

			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		except Exception as e:
			return Response(default_message_request(status.HTTP_500_INTERNAL_SERVER_ERROR), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
