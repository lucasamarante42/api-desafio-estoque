
from .models import MovimentoProduto
from django.db.models import Sum, F

class MovimentoProdutoRepositories():

	@staticmethod
	def rp_get_all():
		return MovimentoProduto.objects.all()

	@staticmethod
	def rp_get_by_id(pk):
		try:
			return MovimentoProduto.objects.get(pk=pk)
		except MovimentoProduto.DoesNotExist:
			return None

	@staticmethod
	def rp_get_stock_balance_by_id_product(id_product=None):
		return MovimentoProduto.objects.filter(id_produto=id_product) \
				.aggregate(stock_balance=Sum(F('quantidade_entrada') - F('quantidade_saida')))