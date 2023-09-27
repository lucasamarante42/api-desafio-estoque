from rest_framework import serializers
from .models import Produto
from estoque_geral.utils import show_message_errors, data_mapping_to_serializer, data_perform_update

from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin

dict_extra_kwargs = {
	'codigo': show_message_errors(description_field='codigo', max_length_field=30),
	'descricao': show_message_errors(description_field='descricao', max_length_field=200),
	'ativo': show_message_errors(description_field='ativo'),
	'dt_criacao': show_message_errors(description_field='dt_criacao'),
	'dt_atualizacao': show_message_errors(description_field='dt_atualizacao')
}

class ProdutoListSerializer(serializers.ListSerializer):
	def update(self, instance, validated_data):

		# Maps for id->instance and id->data item.
		data_mapping = data_mapping_to_serializer('id', validated_data)

		# Perform updates.
		return data_perform_update(self, instance, data_mapping)

class ProdutoSerializers(serializers.ModelSerializer):
	id = serializers.IntegerField()

	class Meta:
		model = Produto
		list_serializer_class = ProdutoListSerializer
		fields = '__all__'
		extra_kwargs = dict_extra_kwargs

class ProdutoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Produto
		fields = '__all__'

		extra_kwargs = dict_extra_kwargs


class BulkProdutoSerializer(BulkSerializerMixin, serializers.ModelSerializer):

	class Meta(object):
		model = Produto
		fields = '__all__'

		list_serializer_class = BulkListSerializer
		update_lookup_field = 'id'