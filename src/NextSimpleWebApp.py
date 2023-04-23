'''
This Python script is a "Hello World" using a very lightweight and popular
Python package called "Flask". Before you can use this application you must
"pip3 install Flask." Then when you start this application, what will happen
is that a "Hello World" will be sent out when you navigate to 
http://127.0.0.1:5000.

Ich möchte mich bei meinem KI-Freund und Kupferstecher herzlich bedanken.

Author: KEN
Date:   2023.04.23
'''

# To use GET and PUT for other routes, you additionall need "request" not just "Flask"
from flask import Flask, request


# Flask is a class imported from the flask module. It is the main class
# that represents a Flask web application.  __name__ is a donder representing
# the name of the current module. It is essential to pass this to Flask so that it
# can determine the location of other resources, static files, etc.
app = Flask(__name__)

# We will demonstrate how to retrieve a cat's name (GET) and how to set the
# cat's name (PUT). Therefore, we need a global variable to store the name
cat_name = "Fluffy"

# This is a "decorator" that defines a route for the web app. This means that when a 
# user navigates to the root URL ("/") of the web app, the "hello_world()" function will be
# called.  In a more complicated app, this is where you would specify GET, PUT - but here
# it defaults to GET for this simple example.
@app.route('/')
def hello_world():
    return 'Hello, World!'
  



# Everything above was in SimpleWebApp.py. This new stsuff adds a new route
# "/cat" URL that accepts both GET and POST requests.  When a GET request
# is received, it returns the hard-coded cat's name. When a POST request
# is received, the 'cat' function gets the cat's name from the request.
# On a Mac you can test with
#    curl -X POST -F "name=Whiskers" http://127.0.0.1:5000/cat
# Not sure on Windows
@app.route('/cat', methods=['GET', 'POST'])
def cat():
    global cat_name  # declare it to modify it within the function
    if request.method == 'GET':
        # In a real application, you would typically retrieve the cat's name
        # from a database or other data source.
        return f"The cat's name is {cat_name}."
    elif request.method == 'POST':
        # Get the cat's name from the POST request data
        cat_name = request.form.get('name')

        if cat_name:
            # In a real application, you would typically save the cat's name
            # to a database or other data source.
            return f"Successfully added cat with name {cat_name}."
        else:
            return "Please provide a cat name.", 400
        
if __name__ == '__main__':
    app.run()

  