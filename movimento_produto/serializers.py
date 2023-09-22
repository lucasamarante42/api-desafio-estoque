from rest_framework import serializers
from .models import MovimentoProduto
from estoque_geral.utils import show_message_errors

dict_extra_kwargs = {
	'id_produto': show_message_errors(description_field='id_produto'),
	'quantidade_entrada': show_message_errors(description_field='quantidade_entrada'),
	'quantidade_saida': show_message_errors(description_field='quantidade_saida'),
	'dt_criacao': show_message_errors(description_field='dt_criacao'),
	'dt_atualizacao': show_message_errors(description_field='dt_atualizacao')
}

class MovimentoProdutoSerializer(serializers.ModelSerializer):

	class Meta:
		model = MovimentoProduto
		fields = '__all__'

		extra_kwargs = dict_extra_kwargs