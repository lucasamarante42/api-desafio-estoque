
from .repositories import MovimentoProdutoRepositories
from estoque.repositories import EstoqueRepositories
from estoque_futuro.repositories import EstoqueFuturoRepositories
from estoque_reserva.repositories import EstoqueReservaRepositories

class MovimentoProdutoBusiness:

	@staticmethod
	def bs_get_all():
		return MovimentoProdutoRepositories.rp_get_all()

	@staticmethod
	def bs_get_by_id(pk):
		return MovimentoProdutoRepositories.rp_get_by_id(pk)

	@staticmethod
	def bs_delete(pk=None, qs_obj=None):
		return MovimentoProdutoRepositories.rp_delete_by_id(pk=pk, qs_obj=qs_obj)

	@staticmethod
	def bs_get_stock_balance_by_id_product(id_product=None):
		return MovimentoProdutoRepositories.rp_get_stock_balance_by_id_product(id_product=id_product)

	@staticmethod
	def bs_update_stock_balance_by_id_product(id_product=None):
		#Saldo do movimento de produto
		qs_stock_balance = MovimentoProdutoBusiness.bs_get_stock_balance_by_id_product(id_product=id_product)
		stock_balance = int(qs_stock_balance.get('stock_balance') or 0)

		#Sum do estoque futuro e soma ao saldo movimento do produto
		# qs_sum_quantity = EstoqueFuturoRepositories.rp_get_sum_quantity_by_id_product_and_available_date(id_product=id_product)
		# stock_balance += int(qs_sum_quantity.get('sum_quantity') or 0)

		#Consulta estoque reserva, atualiza status e subtrai ao saldo movimento do produto
		qs_reserve_stock = EstoqueReservaRepositories.rp_get_by_id_product_and_expiration_date_and_status(id_product=id_product)
		if qs_reserve_stock:
			for qs in qs_reserve_stock:
				if stock_balance - qs.quantidade > 0:
					qs.status = 'FINALIZADO'
					stock_balance -= qs.quantidade
				else:
					qs.status = 'BLOQUEADO'
					break

			EstoqueReservaRepositories.rp_save_bulk_update(list_obj=qs_reserve_stock, list_fields=['status'])

		EstoqueRepositories.rp_create_or_update_by_id_product(id_product=id_product, field='quantidade', value=stock_balance)