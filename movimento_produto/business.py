
from .repositories import MovimentoProdutoRepositories
from estoque.repositories import EstoqueRepositories

class MovimentoProdutoBusiness:

	@staticmethod
	def bs_get_all():
		return MovimentoProdutoRepositories.rp_get_all()

	@staticmethod
	def bs_get_by_id(pk):
		return MovimentoProdutoRepositories.rp_get_by_id(pk)

	@staticmethod
	def bs_get_stock_balance_by_id_product(id_product=None):
		return MovimentoProdutoRepositories.rp_get_stock_balance_by_id_product(id_product=id_product)

	@staticmethod
	def bs_update_stock_balance_by_id_product(id_product=None):
		qs_stock_balance = MovimentoProdutoBusiness.bs_get_stock_balance_by_id_product(id_product=id_product)

		stock_balance = int(qs_stock_balance.get('stock_balance') or 0)

		EstoqueRepositories.rp_create_or_update_by_id_product(id_product=id_product, field='quantidade', value=stock_balance)