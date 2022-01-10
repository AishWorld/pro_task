# pro_task
1.Create a Django project (use https://pipenv.pypa.io/en/latest/)
2.Use Postgres as DB (in Docker container)
3.Add tables:
Person (name, email, age, phone, address, created datetime, modified datetime)
Employee (person_id Foreign Key, department, role, created datetime, modified datetime)
4.Django Admin views
i.one for Person and Employee models
ii.relevant fields should be separately displayed in columns

5.REST APIs to add, delete, modify single or multiple
Person(s)
Employees(s)

7.Postman file demonstrating the REST APIs
8.Tests
i.test using Django Client
ii.One test.py for each view
10. Document API using doc_url
