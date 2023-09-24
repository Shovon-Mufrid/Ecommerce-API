<!-- Virtual Environment Install -->
python3 -m venv venv

<!-- Package Downloads -->
pip install -r requirements.txt

<!-- Migrate & Migrations -->
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py migrate

<!-- Runserver -->
python3 manage.py runserver

<!-- Secret Key Generate -->
python3 manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

<!-- App Creation -->
python manage.py startapp NAME ./CORE/NAME

<!-- Swagger UI -->
python manage.py spectacular --file schema.yml

<!-- Coverage -->
coverage run -m pytest
coverage html

coverage html








