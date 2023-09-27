from rest_framework.test import APITestCase
from django.conf import settings
from django.urls import reverse
from rest_framework import status
from .models import Estoque
from .serializers import EstoqueSerializer
from produto.repositories import ProdutoRepositories

class EstoqueTests(APITestCase):

	valid_body = {
		'id_produto': 1,
		'quantidade': 1
	}

	invalid_body = {
		'id_produto': 100,
		'quantidade': 2.90
	}

	qs_produto = ProdutoRepositories.rp_get_all()
	Estoque.objects.create(id_produto=qs_produto[0], quantidade=5)
	Estoque.objects.create(id_produto=qs_produto[1], quantidade=7)

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

		Imovels = Estoque.objects.all()
		serializer = EstoqueSerializer(Imovels, many=True)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)