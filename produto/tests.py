from rest_framework.test import APITestCase
from django.conf import settings
from django.urls import reverse
from rest_framework import status
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoTests(APITestCase):

	valid_body = {
		'codigo': 'MN-100',
		'descricao': 'Monitor AOC 100',
		'ativo': True
	}

	invalid_body = {
		'codigo': '',
		'descricao': 'Monitor AOC 100',
		'ativo': 'True'
	}

	Produto.objects.create(codigo='BIKE1', descricao='BICICLETA 1', ativo=True)
	Produto.objects.create(codigo='BIKE2', descricao='BICICLETA 2', ativo=True)

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

		qs = Produto.objects.all()
		serializer = ProdutoSerializer(qs, many=True)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)