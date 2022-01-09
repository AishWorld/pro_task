from taskapp.models import Person, Employee
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from taskapp.serializers import PersonSerializer, EmployeeSerializer

# Create your views here.
# Person View
@api_view(['GET',"PUT","DELETE"])
def get_delete_update_person(request, pk):
    try:
       person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    # get details of a single Person
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    # delete single Person
    if request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # update details of single Person
    if request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def get_post_person(request):
    # get all Person
    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {
            'name' : request.data.get('name'),
            'email' : request.data.get('email'),
            'age' : int(request.data.get('age')),
            'phone' :request.data.get('phone'),
            'address' : request.data.get('address'),

            }
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Employee View
@api_view(['GET',"PUT","DELETE"])
def get_delete_update_employee(request, pk):
    try:
       employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    # get details of a single Employee
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    # delete single Person
    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # update details of single Employee
    if request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def get_post_employee(request):
    # get all Person
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {
            'person_id' : request.data.get('person_id'),
            'department' : request.data.get('department'),
            'role' : request.data.get('role'),
            }
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





