from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from receitas.models import Receita


class ReceitasTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('receitas-list')
        self.receita1 = Receita.objects.create(
            descricao="Salário", valor=5000, data='2022-05-05'
        )
        self.receita2 = Receita.objects.create(
            descricao="Investimentos", valor=10000, data='2022-05-05'
        )

    def test_get(self):
        """
        Teste requisição GET
        """
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        """
        Teste requisição POST
        """
        data = {
            'descricao': 'Renda Extra',
            'valor': 2000,
            'data': '05-05-2022'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        """
        Teste requisição DELETE
        """
        response = self.client.delete('/receitas/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put(self):
        """
        Teste requisição PUT
        """
        data = {
            'descricao': 'Salário',
            'valor': 2000,
            'data': '05-05-2022'
        }
        response = self.client.put('/receitas/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_duplicado(self):
        """
        POST duplicado
        """
        data = {
            'descricao': 'Investimentos',
            'valor': 4000,
            'data': '09-05-2022'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)