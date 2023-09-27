from rest_framework import serializers
from .models import Estoque
from estoque_geral.utils import show_message_errors, data_mapping_to_serializer, data_perform_update, get_type_date, \
								convert_date
from estoque_futuro.repositories import EstoqueFuturoRepositories

from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin

dict_extra_kwargs = {
	'id_produto': show_message_errors(description_field='id_produto'),
	'quantidade': show_message_errors(description_field='quantidade'),
	'dt_criacao': show_message_errors(description_field='dt_criacao'),
	'dt_atualizacao': show_message_errors(description_field='dt_atualizacao')
}

class EstoqueListSerializer(serializers.ListSerializer):
	def update(self, instance, validated_data):

		# Maps for id->instance and id->data item.
		data_mapping = data_mapping_to_serializer('id', validated_data)

		# Perform updates.
		return data_perform_update(self, instance, data_mapping)

class EstoqueSerializers(serializers.ModelSerializer):
	id = serializers.IntegerField()

	class Meta:
		model = Estoque
		list_serializer_class = EstoqueListSerializer
		fields = '__all__'
		extra_kwargs = dict_extra_kwargs

class EstoqueSerializer(serializers.ModelSerializer):
	id_produto_codigo = serializers.ReadOnlyField(source='id_produto.codigo')
	id_produto_descricao = serializers.ReadOnlyField(source='id_produto.descricao')

	class Meta:
		model = Estoque
		fields = '__all__'

		extra_kwargs = dict_extra_kwargs


class BulkEstoqueSerializer(BulkSerializerMixin, serializers.ModelSerializer):

	class Meta(object):
		model = Estoque
		fields = '__all__'

		list_serializer_class = BulkListSerializer
		update_lookup_field = 'id'

class EstoqueInfoAllSerializer(serializers.ModelSerializer):
	id_produto_codigo = serializers.ReadOnlyField(source='id_produto.codigo')
	id_produto_descricao = serializers.ReadOnlyField(source='id_produto.descricao')

	estoque_futuro = serializers.SerializerMethodField()

	class Meta:
		model = Estoque
		fields = '__all__'

		extra_kwargs = dict_extra_kwargs

	def get_estoque_futuro(self, obj):
		if obj.id_produto.estoque_futuro.all():
			qs_future_stock = [ef for ef in obj.id_produto.estoque_futuro.all() if ef.dt_disponivel <= get_type_date('date')]
			list_future_stock = []
			if qs_future_stock:
				for qfs in qs_future_stock:
					list_future_stock.append({
						'quantidade': qfs.quantidade,
						'saldo_estoque_futuro': qfs.quantidade + obj.quantidade,
						'dt_disponivel': convert_date(value_date=qfs.dt_disponivel, format_date='%d/%m/%Y')
					})
			return list_future_stock
		return None