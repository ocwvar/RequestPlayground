echo "[STEP 1] begin to migrate anything"
python3 ./manage.py makemigrations
python3 ./manage.py migrate

echo "[STEP 2] begin to run server, will listening at port:$DJANGO_PORT"
python3 ./manage.py runserver 0.0.0.0:$DJANGO_PORT