# web scraping project with python , django and beautifulsoup

# steps to run this project

1- download code of this project

2- create a virtual env by this command. "virtualenv myenv" -> for linux users

3- activate the virtual environment "source myenv/bin/activate" -> for linux users

4- change directory to the project folder 

5- run the following commands

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver


#How The App Works!
The use of this app pretty much easy. Just You need to create your account by clicking the register tab and provide essential information. Then Login to your account with login page by entering valid username and password. if username and password were correct you will be navigate to the dashboard.

#How To Add Item for tracking
It is very easy to add item to the tracking list. Go to the Flipkart website, search your favourite item and copy the url from browser url box. click on "add new item" button, a pop up model will be appear past the url in the input box and click on save button, if the url is valid then item will be added to the track items list. Note!.. some urls are not working on this app.

#How to update the tracked items
Updating the list is very easy, just click on the update button and all items will be updated.
