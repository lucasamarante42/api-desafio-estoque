
from .models import EstoqueFuturo

class EstoqueFuturoRepositories():

	@staticmethod
	def rp_get_all():
		return EstoqueFuturo.objects.all()

	@staticmethod
	def rp_get_by_id(pk):
		try:
			return EstoqueFuturo.objects.get(pk=pk)
		except EstoqueFuturo.DoesNotExist:
			return None

	@staticmethod
	def rp_get_by_id_product(id_product=None):
		try:
			return EstoqueFuturo.objects.get(id_produto=id_product)
		except EstoqueFuturo.DoesNotExist:
			return None

	@staticmethod
	def rp_get_in_bulk(lst_ids=None):
		return EstoqueFuturo.objects.in_bulk(id_list=lst_ids, field_name='id')