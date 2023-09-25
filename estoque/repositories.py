
from .models import Estoque
from produto.repositories import ProdutoRepositories

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
	def rp_create_obj(dict_data=None):
		return Estoque(id_produto=dict_data.get('id_produto'),
						quantidade=dict_data.get('quantidade'))

	@staticmethod
	def rp_save(dict_data=None):
		obj = EstoqueRepositories.rp_create_obj(dict_data=dict_data)
		obj.save()
		return obj

	@staticmethod
	def rp_create_or_update_by_id_product(id_product=None, field=None, value=None):
		obj = EstoqueRepositories.rp_get_by_id_product(id_product=id_product)
		if obj:
			setattr(obj, field, value)
			obj.save()
			return obj
		else:
			qs_product = ProdutoRepositories.rp_get_by_id(id_product)
			return EstoqueRepositories.rp_save(dict_data={'id_produto': qs_product, 'quantidade': value})