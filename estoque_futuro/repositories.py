
from .models import EstoqueFuturo
from estoque_geral.utils import get_type_date
from django.db.models import Sum, F

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

	@staticmethod
	def rp_get_sum_quantity_by_id_product_and_available_date(id_product=None):
		return EstoqueFuturo.objects.all().filter(id_produto=id_product, dt_disponivel__lte=get_type_date('date')) \
							.aggregate(sum_quantity=Sum(F('quantidade')))