
from .models import Estoque

class EstoqueRepositories():

	@staticmethod
	def rp_get_all():
		return Estoque.objects.all()

	@staticmethod
	def rp_get_by_id(pk):
		try:
			return Estoque.objects.get(pk=pk)
		except Estoque.DoesNotExist:
			return None

	@staticmethod
	def rp_get_by_id_product(id_product=None):
		try:
			return Estoque.objects.get(id_produto=id_product)
		except Estoque.DoesNotExist:
			return None

	@staticmethod
	def rp_get_in_bulk(lst_ids=None):
		return Estoque.objects.in_bulk(id_list=lst_ids, field_name='id')

	@staticmethod
	def rp_update_by_id_product(id_product=None, field=None, value=None):
		obj = EstoqueRepositories.rp_get_by_id_product(id_product=id_product)
		if obj:
			setattr(obj, field, value)
			obj.save()
			return obj
		return None