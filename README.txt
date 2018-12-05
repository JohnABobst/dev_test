To run this program you need to install the following python packages using pip.

pip install django
pip install django-cors-headers
pip install django-filter 
pip install djangorestframework
pip install psycopg2

I wrote the program with postgres, but I commented out that database and used the default sqlite3
database since it doesn't need any further configuration.  If you'd like to run the program with 
a postgres database you can set one up with the follow credentials, or adjust the settings file 
to your servers specifications and run these commands from the project root folder after you've deleted
the current migrations files.  
python manage.py makemigrations
python manage.py migrate
from the project root folder

**Credentials**
name: DeveloperTest
user: dev_test_admin
password: dev_test_admin

python manage.py runserver from django root folder to start the backend
yarn start from the vue root folder to install the dependencies and start the server for the vue front end


Part 1:

1. I chose to search for the songs by artist first.  I made artist a foreign key to recording in the database, 
that way so that the initial search query could be cut down.  I used Django's built in query object for the searches.  

2 &3. I think my method of using artist to cut down the initial query would be helpful in a larger database, 
but I definitely think it could be improved upon.  Perhaps setting up more relationships with data points 
that are reliable indicators of a match to further shorten initial querysizes.


Part 2:

1. I chose this layout because with a bigger database the data could become difficult to look at.  
So I chose simple cards to display the data in a uniform manner to make larger amounts of data easier to take in.  
I left out labels for the values to further simplify things.  My thinking was that anyone visiting the site will be familar with it's purpose
so if the meta data values aren't ambigious they can be excluded without losing clarity.  

2.  I would improve the UI by fine tuning the break points, to make sure that the website looks good on any sized display.
I would also add a login screen that redirects to a component that displayed past reports sorted by the current user,
and had an option to upload another csv file.  A descriptor field for reports would also be nice.  Right now I just have 
them displayed using their ID and I don't like the way it looks.  Something like "Foo Bar Music Festival 2019" Would be a much 
better way to display the report links.  

