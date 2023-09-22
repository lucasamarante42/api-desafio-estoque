from django_filters import rest_framework as filters
from .models import Produto
from estoque_geral.filter import NumberInFilter

class ProdutoFilter(filters.FilterSet):
	id = NumberInFilter(field_name='id', lookup_expr='in')
	codigo = filters.CharFilter(field_name='codigo', lookup_expr='iexact')
	descricao = filters.CharFilter(field_name='descricao', lookup_expr='iexact')
	ativo = filters.BooleanFilter(field_name='ativo', lookup_expr='exact')

	iniciado_em_codigo = filters.CharFilter(field_name='codigo', lookup_expr='istartswith')
	contem_codigo = filters.CharFilter(field_name='codigo', lookup_expr='icontains')
	finalizado_em_codigo = filters.CharFilter(field_name='codigo', lookup_expr='iendswith')

	iniciado_em_descricao = filters.CharFilter(field_name='descricao', lookup_expr='istartswith')
	contem_descricao = filters.CharFilter(field_name='descricao', lookup_expr='icontains')
	finalizado_em_descricao = filters.CharFilter(field_name='descricao', lookup_expr='iendswith')

	dt_criacao = filters.DateFilter(field_name='dt_criacao', lookup_expr='iexact')
	dt_atualizacao = filters.DateFilter(field_name='dt_atualizacao', lookup_expr='iexact')

	dt_criacao_inicial = filters.DateFilter(field_name='dt_criacao', lookup_expr='gte')
	dt_criacao_final = filters.DateFilter(field_name='dt_criacao', lookup_expr='lte')

	dt_atualizacao_inicial = filters.DateFilter(field_name='dt_atualizacao', lookup_expr='gte')
	dt_atualizacao_final = filters.DateFilter(field_name='dt_atualizacao', lookup_expr='lte')

	class Meta:
		model = Produto
		fields = [
				'id', 'codigo', 'descricao', 'ativo',
				'iniciado_em_codigo', 'contem_codigo', 'finalizado_em_codigo',
				'iniciado_em_descricao', 'contem_descricao', 'finalizado_em_descricao',
				'dt_criacao', 'dt_atualizacao', 'dt_criacao_inicial', 'dt_criacao_final',
				'dt_atualizacao_inicial', 'dt_atualizacao_final'
				]