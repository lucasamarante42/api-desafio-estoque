from rest_framework.test import APITestCase
from django.conf import settings
from django.urls import reverse
from rest_framework import status
from .models import MovimentoProduto
from .serializers import MovimentoProdutoSerializer
from produto.repositories import ProdutoRepositories

class MovimentoProdutoTests(APITestCase):

	valid_body = {
		'id_produto': 1,
		'quantidade_entrada': 1,
		'quantidade_saida': 0,
	}

	invalid_body = {
		'id_produto': 100,
		'quantidade_entrada': 'A',
		'quantidade_saida': 0,
	}

	qs_produto = ProdutoRepositories.rp_get_all()
	MovimentoProduto.objects.create(id_produto=qs_produto[0], quantidade_entrada=5, quantidade_saida=0)
	MovimentoProduto.objects.create(id_produto=qs_produto[1], quantidade_entrada=7, quantidade_saida=0)

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

		qs = MovimentoProduto.objects.all()
		serializer = MovimentoProdutoSerializer(qs, many=True)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)