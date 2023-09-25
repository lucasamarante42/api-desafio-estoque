
from .repositories import EstoqueFuturoRepositories
from estoque_geral.utils import mount_list_ids

class EstoqueFuturoBusiness:

	@staticmethod
	def bs_get_all():
		return EstoqueFuturoRepositories.rp_get_all()

	@staticmethod
	def bs_get_by_id(pk):
		return EstoqueFuturoRepositories.rp_get_by_id(pk)

	@staticmethod
	def bs_get_by_ids(array_obj=None):
		return EstoqueFuturoRepositories.rp_get_in_bulk(lst_ids=mount_list_ids(array_obj=array_obj))