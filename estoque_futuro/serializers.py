from rest_framework import serializers
from .models import EstoqueFuturo
from estoque_geral.utils import show_message_errors, data_mapping_to_serializer, data_perform_update

from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin

dict_extra_kwargs = {
	'id_produto': show_message_errors(description_field='id_produto'),
	'quantidade': show_message_errors(description_field='quantidade'),
	'dt_disponivel': show_message_errors(description_field='dt_disponivel'),
	'dt_criacao': show_message_errors(description_field='dt_criacao'),
	'dt_atualizacao': show_message_errors(description_field='dt_atualizacao')
}

class EstoqueFuturoListSerializer(serializers.ListSerializer):
	def update(self, instance, validated_data):

		# Maps for id->instance and id->data item.
		data_mapping = data_mapping_to_serializer('id', validated_data)

		# Perform updates.
		return data_perform_update(self, instance, data_mapping)

class EstoqueFuturoSerializers(serializers.ModelSerializer):
	id = serializers.IntegerField()

	class Meta:
		model = EstoqueFuturo
		list_serializer_class = EstoqueFuturoListSerializer
		fields = '__all__'
		extra_kwargs = dict_extra_kwargs

class EstoqueFuturoSerializer(serializers.ModelSerializer):

	class Meta:
		model = EstoqueFuturo
		fields = '__all__'

		extra_kwargs = dict_extra_kwargs


class BulkEstoqueFuturoSerializer(BulkSerializerMixin, serializers.ModelSerializer):

	class Meta(object):
		model = EstoqueFuturo
		fields = '__all__'

		list_serializer_class = BulkListSerializer
		update_lookup_field = 'id'