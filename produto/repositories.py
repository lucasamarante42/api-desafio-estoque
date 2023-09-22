
from .models import Produto

class ProdutoRepositories():

	@staticmethod
	def rp_get_all():
		return Produto.objects.all()

	@staticmethod
	def rp_get_by_id(pk):
		try:
			return Produto.objects.get(pk=pk)
		except Produto.DoesNotExist:
			return None

	@staticmethod
	def rp_get_in_bulk(lst_ids=None):
		return Produto.objects.in_bulk(id_list=lst_ids, field_name='id')