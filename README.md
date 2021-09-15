installation steps 
git https://github.com/AmbroTall/fourthyearproject/new/master 
cd https://github.com/AmbroTall/fourthyearproject/new/master 
virtualenv -p python 3.9 ./Script/activate
pip install -r requirements.txt 
cd umoja 
python manage.py migrate
python manage.py runserver
