
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

	@staticmethod
	def rp_create_obj(dict_data=None):
		return Produto(codigo=dict_data.get('codigo'),
						descricao=dict_data.get('descricao'),
						ativo=dict_data.get('ativo'))

	@staticmethod
	def rp_save_bulk_create(list_obj=None):
		Produto.objects.bulk_create(list_obj)