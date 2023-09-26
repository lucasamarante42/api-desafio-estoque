
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
	def rp_delete_by_id(pk=None, qs_obj=None):
		obj = qs_obj
		if not obj:
			obj = MovimentoProdutoRepositories.rp_get_by_id(pk)
		if obj:
			obj.delete()
			return True
		return False

	@staticmethod
	def rp_get_stock_balance_by_id_product(id_product=None):
		return MovimentoProduto.objects.filter(id_produto=id_product) \
				.aggregate(stock_balance=Sum(F('quantidade_entrada') - F('quantidade_saida')))