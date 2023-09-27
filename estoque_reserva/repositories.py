
from .models import EstoqueReserva
from estoque_geral.utils import get_type_date
from django.db.models import Sum, F

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

	@staticmethod
	def rp_get_by_id_product_and_expiration_date_and_status(id_product=None, add_sum_aggregate=None):
		queryset = EstoqueReserva.objects.all().filter(id_produto=id_product, dt_expiracao__gt=get_type_date('date'), status='EM ABERTO')

		if add_sum_aggregate:
			queryset = queryset.aggregate(sum_quantity=Sum(F('quantidade')))

		return queryset

	@staticmethod
	def rp_save_bulk_update(list_obj=None, list_fields=None):
		EstoqueReserva.objects.bulk_update(list_obj, list_fields)