from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from receitas.models import Despesa


class ReceitasTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('despesas-list')
        self.receita1 = Despesa.objects.create(
            descricao="Carro", categoria="T", valor=800, data='2022-09-01'
        )
        self.receita2 = Despesa.objects.create(
            descricao="Mercado", categoria="A", valor=500, data='2022-05-02'
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
            'descricao': 'Luz',
            'valor': 60,
            'categoria': 'M',
            'data': '05-05-2022'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        """
        Teste requisição DELETE
        """
        response = self.client.delete('/despesas/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put(self):
        """
        Teste requisição PUT
        """
        data = {
            'descricao': 'Carro',
            'valor': 200,
            'categoria': '',
            'data': '05-05-2022'
        }
        response = self.client.put('/despesas/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_duplicado(self):
        """
        POST duplicado
        """
        data = {
            'descricao': 'Mercado',
            'categoria': "M",
            'valor': 500,
            'data': '09-05-2022'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)