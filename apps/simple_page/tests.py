# -*- coding: utf-8 -*-

from django_webtest import WebTest
from django.core.urlresolvers import reverse
from apps.simple_page.models import Order


class HomePageTest(WebTest):
    def test_smoke(self):
        url = reverse('home_page')
        res = self.app.get(url)
        self.assertEquals(res.status_code, 200, 'Home page is unavalible')


class OrderTest(WebTest):
    csrf_checks = False

    def test_normal_data(self):
        params = {
            'email': 'ivan@mail.ru',
            'name': 'Иванов Иван',
            'address': 'г. Энгельс Рыбная улица 4',
        }
        url = reverse('order_make')
        res = self.app.post(url, params=params)

        order = Order.objects.get(**params)

        self.assertEquals(res.status_code, 201, 'Order was not created')
        self.assertIsNotNone(order.payment, 'Payment of order was not created')

    def test_wrong_data(self):
        params = {
            'email': '@mail.',
        }
        url = reverse('order_make')
        res = self.app.post(url, params=params)
        res.charset = 'utf-8'

        self.assertEquals(res.status_code, 200, 'Order made with wrong data')
        self.assertContains(res, 'email', 1)
        self.assertContains(res, 'name', 1)
        self.assertContains(res, 'address', 1)