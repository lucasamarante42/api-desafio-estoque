from django_filters import rest_framework as filters
from .models import Estoque
from estoque_geral.filter import NumberInFilter

class EstoqueFilter(filters.FilterSet):
	id = NumberInFilter(field_name='id', lookup_expr='in')
	id_produto = NumberInFilter(field_name='id_produto', lookup_expr='in')
	id_produto_codigo = filters.CharFilter(field_name='id_produto__codigo', lookup_expr='iexact')

	quantidade_maior_que = filters.DateFilter(field_name='quantidade', lookup_expr='gt')

	dt_criacao = filters.DateFilter(field_name='dt_criacao', lookup_expr='iexact')
	dt_atualizacao = filters.DateFilter(field_name='dt_atualizacao', lookup_expr='iexact')

	dt_criacao_inicial = filters.DateFilter(field_name='dt_criacao', lookup_expr='gte')
	dt_criacao_final = filters.DateFilter(field_name='dt_criacao', lookup_expr='lte')

	dt_atualizacao_inicial = filters.DateFilter(field_name='dt_atualizacao', lookup_expr='gte')
	dt_atualizacao_final = filters.DateFilter(field_name='dt_atualizacao', lookup_expr='lte')

	class Meta:
		model = Estoque
		fields = [
				'id', 'id_produto', 'id_produto_codigo', 'quantidade_maior_que',
				'dt_criacao', 'dt_atualizacao', 'dt_criacao_inicial', 'dt_criacao_final',
				'dt_atualizacao_inicial', 'dt_atualizacao_final'
				]