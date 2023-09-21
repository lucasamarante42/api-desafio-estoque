import os

PROJECT_NAME = 'challenge_geral'

def main():
	print('----- Start seed -----')
	from imovel.repositories import ImovelRepositories
	from anuncio.repositories import AnuncioRepositories
	from reserva.repositories import ReservaRepositories
	import uuid

	list_obj_imovel = [
		{'codigo_imovel': '1111POEJGK403', 'limite_hospede': 2, 'quantidade_banheiro': 2, 'aceita_pet': True, 'valor_limpeza': 100.00, 'data_ativacao': '2023-01-30'},
		{'codigo_imovel': '2222ETWJGKEW4', 'limite_hospede': 4, 'quantidade_banheiro': 3, 'aceita_pet': False, 'valor_limpeza': 50.00, 'data_ativacao': '2023-02-10'},
		{'codigo_imovel': '3333PEOFK4959', 'limite_hospede': 8, 'quantidade_banheiro': 4, 'aceita_pet': True, 'valor_limpeza': 4.00, 'data_ativacao': '2023-03-20'},
		{'codigo_imovel': '4444J039I5IK3', 'limite_hospede': 10, 'quantidade_banheiro': 1, 'aceita_pet': False, 'valor_limpeza': 26.00, 'data_ativacao': '2023-04-10'},
		{'codigo_imovel': '5555JGK45994K', 'limite_hospede': 15, 'quantidade_banheiro': 9, 'aceita_pet': True, 'valor_limpeza': 980.00, 'data_ativacao': '2023-05-02'},
	]

	list_imovel = []
	for imovel in list_obj_imovel:
		list_imovel.append(ImovelRepositories.rp_create_obj(dict_data=imovel))

	if list_imovel:
		ImovelRepositories.rp_save_bulk_create(list_obj=list_imovel)

	queryset_imovel = ImovelRepositories.rp_get_all()

	if queryset_imovel:
		list_obj_anuncio = [
			{'id_imovel': queryset_imovel[len(queryset_imovel)-1], 'plataforma_publicada': 'AirBnb', 'taxa_plataforma': 100.00},
			{'id_imovel': queryset_imovel[len(queryset_imovel)-2], 'plataforma_publicada': 'AirBnb', 'taxa_plataforma': 50.00},
			{'id_imovel': queryset_imovel[len(queryset_imovel)-3], 'plataforma_publicada': 'AirBnb', 'taxa_plataforma': 4.00}
		]

		list_anuncio = []
		for anuncio in list_obj_anuncio:
			list_anuncio.append(AnuncioRepositories.rp_create_obj(dict_data=anuncio))

		if list_anuncio:
			AnuncioRepositories.rp_save_bulk_create(list_obj=list_anuncio)

	queryset_anuncio = AnuncioRepositories.rp_get_all()

	if queryset_anuncio:
		list_obj_reserva = [
			{'codigo_reserva': str(uuid.uuid4()), 'id_anuncio': queryset_anuncio[len(queryset_anuncio)-1], 'data_check_in': '2023-01-30', 'data_check_out': '2023-02-05', 'preco_total': 100.00, 'comentario': '', 'quantidade_hospede': 2},
			{'codigo_reserva': str(uuid.uuid4()), 'id_anuncio': queryset_anuncio[len(queryset_anuncio)-2], 'data_check_in': '2023-02-02', 'data_check_out': '2023-03-30', 'preco_total': 50.00, 'comentario': '', 'quantidade_hospede': 3},
			{'codigo_reserva': str(uuid.uuid4()), 'id_anuncio': queryset_anuncio[len(queryset_anuncio)-3], 'data_check_in': '2023-03-30', 'data_check_out': '2023-04-03', 'preco_total': 4.00, 'comentario': '', 'quantidade_hospede': 4},
			{'codigo_reserva': str(uuid.uuid4()), 'id_anuncio': queryset_anuncio[len(queryset_anuncio)-4], 'data_check_in': '2023-04-30', 'data_check_out': '2023-05-02', 'preco_total': 26.00, 'comentario': '', 'quantidade_hospede': 5},
			{'codigo_reserva': str(uuid.uuid4()), 'id_anuncio': queryset_anuncio[len(queryset_anuncio)-5], 'data_check_in': '2023-05-30', 'data_check_out': '2023-06-01', 'preco_total': 96.30, 'comentario': 'OBS', 'quantidade_hospede': 22},
			{'codigo_reserva': str(uuid.uuid4()), 'id_anuncio': queryset_anuncio[len(queryset_anuncio)-6], 'data_check_in': '2023-06-30', 'data_check_out': '2023-07-01', 'preco_total': 227.00, 'comentario': 'OBS', 'quantidade_hospede': 12},
			{'codigo_reserva': str(uuid.uuid4()), 'id_anuncio': queryset_anuncio[len(queryset_anuncio)-7], 'data_check_in': '2023-07-30', 'data_check_out': '2023-08-02', 'preco_total': 568.00, 'comentario': 'OBS', 'quantidade_hospede': 14},
			{'codigo_reserva': str(uuid.uuid4()), 'id_anuncio': queryset_anuncio[len(queryset_anuncio)-8], 'data_check_in': '2023-08-30', 'data_check_out': '2023-09-03', 'preco_total': 980.00, 'comentario': 'OBS', 'quantidade_hospede': 8},
		]

		list_reserva = []
		for reserva in list_obj_reserva:
			list_reserva.append(ReservaRepositories.rp_create_obj(dict_data=reserva))

		if list_reserva:
			ReservaRepositories.rp_save_bulk_create(list_obj=list_reserva)

	print('----- Finish seed -----')


if __name__ == '__main__':
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%s.settings' % PROJECT_NAME)
	import django
	django.setup()
	main()