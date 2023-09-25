
from .repositories import EstoqueReservaRepositories
from estoque_geral.utils import mount_list_ids

class EstoqueReservaBusiness:

	@staticmethod
	def bs_get_all():
		return EstoqueReservaRepositories.rp_get_all()

	@staticmethod
	def bs_get_by_id(pk):
		return EstoqueReservaRepositories.rp_get_by_id(pk)

	@staticmethod
	def bs_get_by_ids(array_obj=None):
		return EstoqueReservaRepositories.rp_get_in_bulk(lst_ids=mount_list_ids(array_obj=array_obj))