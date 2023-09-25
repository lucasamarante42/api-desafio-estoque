
from .models import EstoqueReserva

class EstoqueReservaRepositories():

	@staticmethod
	def rp_get_all():
		return EstoqueReserva.objects.all()

	@staticmethod
	def rp_get_by_id(pk):
		try:
			return EstoqueReserva.objects.get(pk=pk)
		except EstoqueReserva.DoesNotExist:
			return None

	@staticmethod
	def rp_get_by_id_product(id_product=None):
		try:
			return EstoqueReserva.objects.get(id_produto=id_product)
		except EstoqueReserva.DoesNotExist:
			return None

	@staticmethod
	def rp_get_in_bulk(lst_ids=None):
		return EstoqueReserva.objects.in_bulk(id_list=lst_ids, field_name='id')