from rest_framework import serializers
from .models import MovimentoProduto
from .business import MovimentoProdutoBusiness
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

	def validate(self, data):
		if data['quantidade_entrada'] < 0 or data['quantidade_saida'] < 0:
			raise serializers.ValidationError("Quantidade entrada/saída não pode ser menor que zero!")

		if data['quantidade_entrada'] > 0 and data['quantidade_saida'] > 0:
			raise serializers.ValidationError("Não é permitido os dois campos serem maior que zero!")

		if data['quantidade_entrada'] == 0 and data['quantidade_saida'] == 0:
			raise serializers.ValidationError("Não é permitido os dois campos serem igual a zero!")

		qs_stock_balance = MovimentoProdutoBusiness.bs_get_stock_balance_by_id_product(id_product=data['id_produto'])
		stock_balance = int(qs_stock_balance.get('stock_balance') or 0)

		if data['quantidade_saida'] > stock_balance:
			raise serializers.ValidationError("O produto não possui saldo no estoque!")

		return data