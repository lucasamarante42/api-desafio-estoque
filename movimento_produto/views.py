from time import sleep
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import MovimentoProdutoSerializer
from .business import MovimentoProdutoBusiness
from .filters import MovimentoProdutoFilter

from rest_framework_tracking.mixins import LoggingMixin

"""
 View genérica RetrieveUpdateDestroyAPIView => utilizado para método GET, PUT e DELETE (por ID)

 Classe: get_delete_update

 Variáveis:
	queryset => consulta na base de dados
	serializer_class => serializer do model
"""
class get_delete_update(LoggingMixin, RetrieveUpdateDestroyAPIView):

	def should_log(self, request, response):
		return (request.method == 'GET' and response.status_code != 200) or request.method != 'GET'

	queryset = MovimentoProdutoBusiness.bs_get_all()
	serializer_class = MovimentoProdutoSerializer

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
			obj = serializer.save()
			if obj:
				MovimentoProdutoBusiness.bs_update_stock_balance_by_id_product(id_product=obj.id_produto_id)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)