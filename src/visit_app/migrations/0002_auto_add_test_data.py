from django.db import migrations


def create_test_data(apps, schema_editor):
    Employee = apps.get_model("visit_app", "Employee")
    Store = apps.get_model("visit_app", "Store")
    Visit = apps.get_model("visit_app", "Visit")

    employee1 = Employee.objects.create(name="Иванов Иван Иванович", phone_number="+77777777777")
    employee2 = Employee.objects.create(name="Петров Пётр Петрович", phone_number="+78888888888")
    employee3 = Employee.objects.create(name="Михайлов Михаил Михайлович", phone_number="+79999999999")

    store1 = Store.objects.create(name="Store 1", employee=employee1)
    store2 = Store.objects.create(name="Store 2", employee=employee1)
    store3 = Store.objects.create(name="Store 3", employee=employee2)

    Visit.objects.create(store=store1, employee=employee1, latitude=40.7777, longitude=30.666)
    Visit.objects.create(store=store2, employee=employee2, latitude=50.7777, longitude=40.666)
    Visit.objects.create(store=store2, employee=employee2, latitude=50.7777, longitude=40.666)
    Visit.objects.create(store=store3, employee=employee3, latitude=60.7777, longitude=50.666)


class Migration(migrations.Migration):

    dependencies = [
        ("visit_app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_test_data),
    ]
