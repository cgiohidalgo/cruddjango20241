#!bin/sh

echo "Migraciones"
python manage.py makemigrations inventario
python manage.py makemigrations usuarios
python manage.py makemigrations ventas
python manage.py migrate

python manage.py loaddata inventario_nova.json
python manage.py loaddata usuarios_nova.json
python manage.py loaddata ventas_nova.json

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '123')" | python manage.py shell

exec "$@"
