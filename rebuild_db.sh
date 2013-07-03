dropdb -U scripts_db scripts_db_dev 
createdb scripts_db_dev -U scripts_db -E utf8
python manage.py syncdb --noinput
