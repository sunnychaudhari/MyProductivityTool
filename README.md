# URL Shortner and MyProductivityTool project

    This is web application for url shortner and myproductivitytool project, based on django-1.11 with python-2.7
    Used ajax to update the data on the pages to display the results without reloading the page.
    * Technologies used : HTML, CSS, Javascript, Jquery, python, django

    * Follow the bellow installation steps and notes for this web application to run in your local machine


INSTALLATION :

1. Create virtual environment and activate it for your project

    --> virtualenv prdtools

    --> cd prdtools

    --> source bin/ activate

2. Clone project

    --> git clone https://github.com/<<your github username>>/MyProductivityTool.git

3. Install required packages

    --> cd MyProductivityTools

    --> pip install -r requirements.txt

4. Makemigrations and migrate into default database sqlite

    --> cd myproductivitytools

    --> python manage.py makemigrations

    --> python manage.py migrate

5. Run your django project

    --> python manage.py runserver

# Notes For URL Shortner:

    http://localhost:8000/dashboard/

    Enter the url in the input box and hit the "Shorten url" button
    You will see the shortend url below, check hitting that shorten url into browser it will redirect to the original url

    * you can see all the relevant code under shortner app in django project. urls, models and business logic.
    * Used ajax calls to execute the api calls, you will see the results without reloading the page.

# Notes For MyProductivityTool project

    http://localhost:8000/login   -->(login page for project)
    * Signup first for the project by click on signup link on login page, once signed up successfully it will redirect to login page.
    * Once you loggedin you will redirect to "project page", where you can create new project, add ,update and delete projects
    * You can create a task under that project, click on project name you will be redirected to the task page
    * You can create new task here or edit the existing tasks or delete
    * To enter the task details, click on task name and you will see popup modal with task assigned_to, due date and task description details, You can add or update the task details from that form or you can delete the task
    * The user should only have access to his/her own projects and tasks.

    * You can see all the relevant code under tasks app in django project.
    All urls(login,logout,signup,project,tasks), views, models under tasks app for this project