from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import ProdutoSerializer, ProdutoSerializers, BulkProdutoSerializer
from .business import ProdutoBusiness
from .filters import ProdutoFilter
from estoque_geral.utils import check_filtered_params_exists

from rest_framework_tracking.mixins import LoggingMixin
from estoque_geral.views import MultiObjectCreateAPIView, MultiObjectUpdateDestroyAPIView
from rest_framework_bulk import BulkModelViewSet

"""
 View genérica RetrieveUpdateDestroyAPIView => utilizado para método GET, PUT e DELETE (por ID)

 Classe: get_delete_update

 Variáveis:
	queryset => consulta na base de dados
	serializer_class => serializer do model
"""
class get_delete_update(LoggingMixin, RetrieveUpdateDestroyAPIView):

	queryset = ProdutoBusiness.bs_get_all()
	serializer_class = ProdutoSerializer

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

	queryset = ProdutoBusiness.bs_get_all()
	serializer_class = ProdutoSerializer

	filterset_class = ProdutoFilter

"""
 View MultiObjectCreateAPIView => utilizado para método POST
 (criação de múltiplos objetos)

 Classe: post_list

 Variáveis:
	serializer_class => serializer do model
"""
class post_list(LoggingMixin, MultiObjectCreateAPIView):

	serializer_class = ProdutoSerializer

"""
 View MultiObjectUpdateDestroyAPIView => utilizado para método PUT
 (atualização de múltiplos objetos)

 Classe: update_bulk

 Variáveis:
	bussiness_class => bussiness
	serializer_class => serializer do model
"""
class update_bulk(LoggingMixin,	MultiObjectUpdateDestroyAPIView):

	bussiness_class = ProdutoBusiness
	serializer_class = ProdutoSerializers

"""
 View BulkModelViewSet => utilizado para método GET/POST/DELETE/PUT
	=> ação em múltiplos objetos

 Classe: bulk_methods

 Variáveis:
	queryset => consulta na base de dados
	serializer_class => serializer do model
	filterset_class => filtro do model

 Métodos:
	allow_bulk_destroy => lógica para evitar a exclusão em massa sem filtro
"""
class bulk_methods(LoggingMixin, BulkModelViewSet):
	queryset = ProdutoBusiness.bs_get_all()
	serializer_class = BulkProdutoSerializer

	filterset_class = ProdutoFilter

	def allow_bulk_destroy(self, qs, filtered):
		filters = list(self.filterset_class.get_fields().keys())
		return check_filtered_params_exists(self.request.query_params, filters, filtered)