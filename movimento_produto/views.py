from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response
from estoque_geral.utils import default_message_request
from .serializers import MovimentoProdutoSerializer
from .business import MovimentoProdutoBusiness
from .filters import MovimentoProdutoFilter

from rest_framework_tracking.mixins import LoggingMixin

"""
 View genérica RetrieveDestroyAPIView => utilizado para método GET, PUT e DELETE (por ID)

 Classe: get_delete

 Variáveis:
	queryset => consulta na base de dados
	serializer_class => serializer do model
"""
class get_delete(LoggingMixin, RetrieveDestroyAPIView):

	def should_log(self, request, response):
		return (request.method == 'GET' and response.status_code != 200) or request.method != 'GET'

	queryset = MovimentoProdutoBusiness.bs_get_all()
	serializer_class = MovimentoProdutoSerializer

	def delete(self, request, pk):
		qs_movimento = MovimentoProdutoBusiness.bs_get_by_id(pk)
		if qs_movimento:
			del_ok = MovimentoProdutoBusiness.bs_delete(qs_obj=qs_movimento)
			if del_ok:
				MovimentoProdutoBusiness.bs_update_stock_balance_by_id_product(id_product=qs_movimento.id_produto_id)
				return Response(default_message_request(status.HTTP_204_NO_CONTENT), status=status.HTTP_204_NO_CONTENT)
		return Response(default_message_request(status.HTTP_404_NOT_FOUND), status=status.HTTP_404_NOT_FOUND)

"""
 View genérica ListCreateAPIView => utilizado para método GET e POST

 Classe: get_post

 Variáveis:
	queryset => consulta na base de dados
	serializer_class => serializer do model
	filterset_class => filtro do model
"""
class get_post(LoggingMixin, ListCreateAPIView):

	def should_log(self, request, response):
		return (request.method == 'GET' and response.status_code != 200) or request.method != 'GET'

	serializer_class = MovimentoProdutoSerializer

	filterset_class = MovimentoProdutoFilter

	def get_queryset(self):
		return MovimentoProdutoBusiness.bs_get_all()

	def post(self, request):
		serializer = MovimentoProdutoSerializer(data=request.data)
		if serializer.is_valid():
			check_conditions, status_code, msg = MovimentoProdutoBusiness.bs_check_conditions(dict_data=serializer.validated_data)

			if check_conditions:
				obj = serializer.save()
				if obj:
					MovimentoProdutoBusiness.bs_update_stock_balance_by_id_product(id_product=obj.id_produto_id)
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response(default_message_request(status_code, msg), status=status_code)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)