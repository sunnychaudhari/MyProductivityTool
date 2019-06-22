# MyProductivityTool
-------------------------------
1. Create virtual environment and activate it for your project
   virtualenv prdtools
   cd prdtools
   source bin/ activate

2. Clone project
    git clone https://github.com/<your github username>/MyProductivityTool.git

3. Install required packages
    cd MyProductivityTools
    pip install -r requirements.txt

4. Makemigrations and migrate into default database sqlite
    cd myproductivitytools
    python manage.py makemigrations
    python manage.py migrate

5. Run your django project
    python manage.py runserver
