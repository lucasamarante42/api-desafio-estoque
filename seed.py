import os

PROJECT_NAME = 'estoque_geral'

def main():
	print('----- Start seed -----')
	from produto.repositories import ProdutoRepositories
	from movimento_produto.repositories import MovimentoProdutoRepositories
	from estoque_futuro.repositories import EstoqueFuturoRepositories
	from estoque_reserva.repositories import EstoqueReservaRepositories
	import uuid

	list_obj_produto = [
		{'codigo': '100', 'descricao': 'PRODUTO 100', 'ativo': True },
		{'codigo': '200', 'descricao': 'PRODUTO 200', 'ativo': False },
		{'codigo': '300', 'descricao': 'PRODUTO 300', 'ativo': True },
		{'codigo': '400', 'descricao': 'PRODUTO 400', 'ativo': False },
		{'codigo': '500', 'descricao': 'PRODUTO 500', 'ativo': True },
	]

	list_produto = []
	for produto in list_obj_produto:
		list_produto.append(ProdutoRepositories.rp_create_obj(dict_data=produto))

	if list_produto:
		ProdutoRepositories.rp_save_bulk_create(list_obj=list_produto)

	print('----- Finish seed -----')


if __name__ == '__main__':
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%s.settings' % PROJECT_NAME)
	import django
	django.setup()
	main()