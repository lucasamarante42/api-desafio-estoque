from rest_framework.test import APITestCase
from django.conf import settings
from django.urls import reverse
from rest_framework import status
from .models import EstoqueReserva
from .serializers import EstoqueReservaSerializer

class EstoqueReservaTests(APITestCase):

	valid_body = {
		'id_produto': 1,
		'quantidade': 1,
		'dt_expiracao': '2023-09-25',
		'status': 'Reservado',
	}

	invalid_body = {
		'id_produto': 100,
		'quantidade': 2.90,
		'dt_expiracao': '2023-01-32',
		'status': None,
	}

	EstoqueReserva.objects.create(id_produto=1, quantidade=5)
	EstoqueReserva.objects.create(id_produto=2, quantidade=7)

	def test_post_with_valid(self):
		url = reverse('get_post')
		response = self.client.post(url, self.valid_body)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_post_with_invalid(self):
		url = reverse('get_post')
		response = self.client.post(url, self.invalid_body)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_get_all(self):
		url = reverse('get_post')
		response = self.client.get(url)

		Imovels = EstoqueReserva.objects.all()
		serializer = EstoqueReservaSerializer(Imovels, many=True)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)