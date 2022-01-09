import json
from django.http import response
from rest_framework import serializers, status
from django.test import TestCase, Client
from django.urls import reverse
from taskapp.models import Person
from taskapp.serializers import PersonSerializer


# initialize theAPIClient app
client = Client()

class GetAllPersonTest(TestCase):
    """ Test module for GET all person API """
    def setUp(self):
        self.person1 = Person.objects.create(name='Person1', email='p1@gmail.com', age=29, phone=9876787656, address='Pune')
        self.person2 = Person.objects.create(name='Person2', email='p2@gmail.com', age=28, phone=8766547888, address='Mumabai')
        self.person3 = Person.objects.create(name='Person3', email='p3@gmail.com', age=27, phone=9876457654, address='Nagpur')
        self.person4 = Person.objects.create(name='Person4', email='p4@gmail.com', age=26, phone=8876787650, address='Katol')

        
        # create Person
        self.valid_payload = {
            'name' : 'Person1',
            'email' : 'p1@gmail.com',
            'age' : 23,
            'phone' : 6758493754,
            'address' : 'Pune'}
        self.invalid_payload = {
           'name' : '',
            'email' : 'p2@gmail.com',
            'age' : 27,
            'phone' : 7858493754,
            'address' : 'Nagpur'}
        # update Person
        # self.valid_payload = {
        #     'id' : 1,
        #     'name' : 'Person11',
        #     'email' : 'p1@gmail.com',
        #     'age' : 43,
        #     'phone' : '6758493754',
        #     'address' : 'Pune'}
        # self.invalid_payload = {
        #    'name' : '',
        #     'email' : 'p22@gmail.com',
        #     'age' : 27,
        #     'phone' : 7858493754,
        #     'address' : 'Nagpur'}
        

    # def test_get_all_person(self):
    #     # "get API response
    #     response = client.get(reverse('get_post_person'))
    #     # get data from db
    #     person = Person.objects.all()
    #     serializer = PersonSerializer(person, many=True)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # def test_get_valid_single_Person(self):
    #     response = client.get(reverse('get_delete_update_person', kwargs={'pk': self.person1.pk}))
    #     person = Person.objects.get(pk=self.person1.pk)
    #     serializer = PersonSerializer(person)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # def test_get_invalid_single_Person(self):
    #     response = client.get(reverse('get_delete_update_person', kwargs={'pk': 30}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # post -- Person
    # def test_create_valid_Person(self):
    #     response = client.post(reverse('get_post_person'),
    #                 data=json.dumps(self.valid_payload),
    #                 content_type= 'application/json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_create_invalid_Person(self):
    #     response = client.post(
    #         reverse('get_post_person'),
    #         data=json.dumps(self.invalid_payload),
    #         content_type='application/json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # update Person details
    # def test_valid_update_person(self):
    #     response = client.put(reverse('get_delete_update_person', kwargs={'pk': self.person1.pk}),
    #         data=json.dumps(self.valid_payload),
    #         content_type='application/json')
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    # def test_invalid_update_Person(self):
    #     response = client.put(reverse('get_delete_update_person', kwargs={'pk' : self.person1.pk}),
    #         data = json.dumps(self.invalid_payload),
    #         content_type='application/json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    # def test_valid_delete_Person(self):
    #     response = client.delete(reverse('get_delete_update_person',kwargs={'pk' : self.person1.pk}))
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    # def invalid_delete_Person(self):
    #     response = client.delete(reverse('get_delete_update_person', kwargs={'pk': 30}))
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    

    def tearDown(self) -> None:
        pass

    
    
  