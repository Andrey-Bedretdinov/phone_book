import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "phone_book.settings")
django.setup()

from contacts.models import LastName, FirstName, MiddleName, Street, Contact

additional_contacts_data = [
    # Продолжение списка contacts_data
    {"last_name": "Иванов", "first_name": "Антон", "middle_name": "Алексеевич", "street": "Гоголевский бульвар",
     "building_number": "21", "building_unit": "3", "apartment": "12", "phone": "+74957765432"},
    {"last_name": "Васильев", "first_name": "Данила", "middle_name": "Васильевич", "street": "Новый Арбат",
     "building_number": "34", "building_unit": "2", "apartment": "23", "phone": "+74959876543"},
    # ... Добавьте еще 38 контактов
]

from random import choice, randint

# Списки возможных имен, фамилий, отчеств и улиц
last_names = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов", "Попов", "Васильев", "Морозов", "Новиков",
              "Андреев"]
first_names = ["Иван", "Алексей", "Дмитрий", "Михаил", "Павел", "Антон", "Сергей", "Евгений", "Артем", "Владимир"]
middle_names = ["Иванович", "Петрович", "Алексеевич", "Дмитриевич", "Михайлович", "Сергеевич", "Владимирович",
                "Андреевич", "Евгеньевич", "Павлович"]
streets = ["Тверская ул.", "Арбат", "Кутузовский проспект", "Ленинградский проспект", "Пресненская наб.",
           "Таганская ул.", "Шоссе Энтузиастов", "Варшавское шоссе", "Рублевское шоссе", "Ленинская Слобода"]

for i in range(38):
    contact = {
        "last_name": choice(last_names),
        "first_name": choice(first_names),
        "middle_name": choice(middle_names),
        "street": choice(streets),
        "building_number": str(randint(1, 100)),
        "building_unit": str(randint(1, 5)),
        "apartment": str(randint(1, 200)),
        "phone": f"+7495{randint(1000000, 9999999)}"
    }
    additional_contacts_data.append(contact)

for contact_data in additional_contacts_data:
    last_name, _ = LastName.objects.get_or_create(last_name=contact_data["last_name"])
    first_name, _ = FirstName.objects.get_or_create(first_name=contact_data["first_name"])
    middle_name, _ = MiddleName.objects.get_or_create(middle_name=contact_data["middle_name"])
    street, _ = Street.objects.get_or_create(street_name=contact_data["street"])

    Contact.objects.create(
        last_name=last_name,
        first_name=first_name,
        middle_name=middle_name,
        street=street,
        building_number=contact_data["building_number"],
        building_unit=contact_data['building_unit'],
        apartment=contact_data['apartment'],
        phone=contact_data["phone"]
    )

print("Контакты успешно добавлены.")

