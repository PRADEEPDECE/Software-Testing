


import pytest
from django.urls import reverse
from .models import Item

@pytest.mark.django_db
def test_create_item(client):
    url = reverse('item-list')
    data = {'name': 'Test Item', 'description': 'This is a test item'}
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 201
    assert Item.objects.count() == 1

@pytest.mark.django_db
def test_get_item(client):
    item = Item.objects.create(name='Test Item', description='This is a test item')
    url = reverse('item-detail', kwargs={'pk': item.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['name'] == 'Test Item'

@pytest.mark.django_db
def test_update_item(client):
    item = Item.objects.create(name='Test Item', description='This is a test item')
    url = reverse('item-detail', kwargs={'pk': item.pk})
    data = {'name': 'Updated Item', 'description': 'This is an updated item'}
    response = client.put(url, data, content_type='application/json')
    assert response.status_code == 200
    assert Item.objects.get(pk=item.pk).name == 'Updated Item'

@pytest.mark.django_db
def test_delete_item(client):
    item = Item.objects.create(name='Test Item', description='This is a test item')
    url = reverse('item-detail', kwargs={'pk': item.pk})
    response = client.delete(url)
    assert response.status_code == 204
    assert Item.objects.count() == 0
# Create your tests here.
