.. _badge_twitter:

=============================================
Twitter Search Client
=============================================

This tutorial will cover using the ``urllib`` module with HTTP APIs (Twitter, in this case), using the ``json`` module to parse JSON API responses, and how to make your life easier by using wrapper libraries.


What's an API?
================================================

Many websites offer what is called an API ("Application Programming Interface") which lets developers like you integrate with their site and build applications on top of their functionality or data. Often, an API gives you ways to authenticate on behalf of a user so that you can perform actions on their data.

Twitter offers an API for both un-authenticated actions, like searching public tweets, and for authenticated actions, like posting and replying. There are hundreds (or thousands) of Twitter clients built by non-Twitter developers that use the API, and these clients often feature a different interface or specialized set of functionality than what Twitter.com offers. In this tutorial, we will use the Twitter API methods that don't require authentication, for simplicity's sake.

Developers interact with an API by using HTTP. It varies depending on the particular API, but basically, you make an HTTP request (usually GET or POST) to a specified URL, optionally attaching some data, and you parse the response.

For example, if you want to find the recent tweets for 'pystar' using the Twitter API, you can put this URL in your browser:

http://search.twitter.com/search.json?q=pystar

You should see the JSON response (don't worry if it looks crazy, we'll explain it soon).

If you wanted to instead find recent tweets for 'python', you could change the value of the 'q' parameter at the end of the URL:
http://search.twitter.com/search.json?q=python

The Twitter search API is an example of an "RPC" API. "RPC" stands for "Remote Procedure Call" and conceptually means that we're calling a method on another server and passing in arguments. In this case, we're calling the 'search' method on the Twitter server and our argument is the 'q' parameter.

How do we use APIs in Python?
================================================

Now, let's try to get the same results that we got in the browser using Python.

Start a new python file ``twitter_search.py`` and copy this code:

.. code-block:: python

  import urllib

  url = 'http://search.twitter.com/search.json?q=python'
  print urllib.urlopen(url).read()

The ``urllib`` module gives us functionality to make HTTP requests, so we import it at the top. Then we store the URL in a variable, we use the ``urlopen`` method to hit up the URL and the ``read()`` method to read the response.
For now, we'll simply print it out to the screen to see if it worked.

Try it out by just running the script from the command line:

.. code-block:: bash

  python twitter_search.py


If it worked, you should see the same thing you saw in the browser.

You can also try changing the search URL to see the results change.

Now, let's talk about that crazy looking response...

What's JSON?
================================================

As you've seen, the request to an HTTP API is often just the URL with some query parameters. The response from an API is data and that data can come in various formats, with the most popular being XML and JSON. Many HTTP APIs support multiple response formats, so that developers can choose the one they're more comfortable parsing.

For example, the Twitter API lets you request "atom" format, which is XML:
http://search.twitter.com/search.atom?q=pystar

Their default response is JSON, which is increasingly popular amongst developers, and is easier to parse in Python than XML. JSON stands for "JavaScript Object Notation" and is the native way of representing objects in JavaScript - so it will look familiar to those of you who know JS. Even if you don't, however, JSON is a fairly intuitive format to understand. JSON is a hierarchy of key/value pairs, where each key is a string and each value is a string, number, boolean, or array.

Here's a JSON describing a person's information:

.. code-block:: javascript

 {"firstName": "John",
  "lastName": "Smith",
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": 10021
   },
   "phoneNumbers": [
    "212 732-1234",
    "646 123-4567" ]
  }

The names are string values, the address is another object with string values,
and the phone numbers is an array of string values.

When we looked at the Twitter API response in the last section, the response was JSON (just a whole lot more of it). Some browsers don't "pretty format" JSON, so it can be hard to look at in the browser when you're a mere human. If you're in Chrome, download the JSONView Chrome extension for pretty formatting:
https://chrome.google.com/webstore/detail/chklaanhfefbnpoihckbnefhakgolnmc

Now, take another look at the search API response in the browser:
http://search.twitter.com/search.json?q=python

You should see something like this:

.. code-block:: javascript

 {
  completed_in: 0.099
  max_id: 111626724697063420
  max_id_str: "111626724697063424"
  next_page: "?page=2&max_id=111626724697063424&q=python"
  page: 1
  query: "python"
  refresh_url: "?since_id=111626724697063424&q=python"
  results: [
   {
   created_at: "Thu, 08 Sep 2011 02:27:39 +0000"
   from_user: "akamrsjojo"
   from_user_id: 32455649
   geo: null
   id: 111626724697063420
   iso_language_code: "en"
   profile_image_url: "http://a0.twimg.com/profile_images/1520692851/akamrsjojo_normal.jpg"
   text: "#Win Christian Louboutin Sueded Python Pump http://t.co/vr5C6St via @AddThis"
   }, ...
  ]
 }

How do we parse JSON in Python?
================================================

Now let's parse some data from that response using Python.

In your Python file, add this to the top:

.. code-block:: python

  import json

The ``json`` module gives us functionality for parsing JSON into Python data structures.

Instead of printing what is read from the url, we'll store it in response:

.. code-block:: python

  url = 'http://search.twitter.com/search.json?q=python'
  response = urllib.urlopen(url).read()

Then add these lines to the bottom:

.. code-block:: python

  data = json.loads(response)
  results = data['results']
  print results[0]['text']

Here, we're telling the json module to convert the string response, then we're storing the results array and printing the text of the first result tweet.

Run the code - you should see the full results and the tweet at the bottom. If you want, remove the first print statement so you just see the tweet.

Now, let's show all the tweets (and the usernames) using a for loop to iterate through the results array. Add these lines:

.. code-block:: python

  for result in results:
    print result['from_user'] + ': ' + result['text'] + '\n'

Run the code, and you should see a bunch of mildly entertaining tweets. Try adding the timestamp to the tweets to see if you understand the JSON response.

Let's make the client!
================================================

Now that we are successfully showing Twitter API search results, let's turn our script into a proper command-line client, so that you can search Twitter from your Terminal all day long!

First, let's structure the code into functions to be a bit cleaner.
Replace your code with this:

.. code-block:: python

  def search_twitter(query='python'):
    url = 'http://search.twitter.com/search.json?q=' + query
    response = urllib.urlopen(url).read()
    data = json.loads(response)
    return data['results']

  def print_tweets(tweets):
    for tweet in tweets:
      print tweet['from_user'] + ': ' + tweet['text'] + '\n'

  results = search_twitter()
  print_tweets(results)

We've made two functions - ``search_twitter`` takes one argument
(falling back to 'python' if none is specified) and returns the array
of results from Twitter, and ``print_tweets`` prints results to the screen,
We could do this as one function, but it's nice to separate
functionality from presentation.

At the end, we just call these functions, passing the results from the first
function as the argument to the second.

Try that out and make sure it works. Try sending in a different argument
to the ``search_twitter`` function and see that it works.

Now, let's make it so we can send in the query argument from the command line.

Add this import to the top:

.. code-block:: python

  import sys

The ``sys`` module gives us access to the passed in arguments.

Now replace the last two lines with this code:

.. code-block:: python

  if __name__ == "__main__":
    query = sys.argv[1]
    results = search_twitter(query)
    print_tweets(results)

That code passes in the first argument to the ``search_twitter`` function and prints the results.

Try running your script, but specifying different queries, like so:

.. code-block:: bash

  python twitter_search.py love
  python twitter_search.py snakes

You may soon lose faith in the intelligence of humanity, but atleast you should now feel good about your own intelligence. :)

Using a wrapper library
================================================

You're not the first developer to use the Twitter search API from Python -
and it's a bit silly for every developer to write their own functions for
interacting with the API. Most developers use "wrapper libraries"
or "client libraries" for interacting with HTTP APIs in their favorite language,
and those libraries are either provided by the API provider themselves or
by other developers. By using a wrapper library, you can focus on writing the unique
part of your app and not fuss over the subtleties of an API.

Twitter maintains a list of developer-created libraries here - with 5 listed for Python alone:
https:/dev.twitter.com/docs/twitter-libraries#python

Let's try using the 'Twython' library, since that has a clever name:
https://github.com/ryanmcgrath/twython

The easiest way to install the library is using pip:

.. code-block:: bash

  pip install python

To use the library, first import the module at the top of your script:

.. code-block:: python

  import twython

You can remove the import statements for ``urllib`` and ``json``,
since the Twython library will take care of the URL opening
and JSON conversion for us.

Next, remove the ``search_twitter`` function and replace the
main functionality with code that calls the search function
from the Twython library instead:

.. code-block:: python

    query = sys.argv[1]
    results = twython.Twitter().searchTwitter(q=query)
    print_tweets(results['results'])


What now?
================================================

Great work! You now have a command line Twitter search client.
Here are some ideas for ways you can extend this code to do more:

Add support for more search options:
-------------------------------------------

So far, we've only been passing in one parameter to the Twitter search API,
the ``q`` argument. As is common with HTTP APIs, the API lets you specify
multiple parameters, and it documents them in their API reference:
https://dev.twitter.com/docs/api/1/get/search

For example, you can specify the ``lang`` argument to get tweets in a particular language, like "lang=es" for Spanish tweets:
http://search.twitter.com/search.json?q=python&lang=es

Modify your client so you can specify options like this:

.. code-block:: bash

  python search_twitter.py python --lang=es

You can use the `argparse`_ module if you're using Python 2.7 or the `argparse_` module if you're using Python 2.6.

Add support for more Twitter API methods:
-------------------------------------------

The Twitter API offers several other methods that can be accessed without user authentication,
like getting all the tweets for a particular user and listing current trends.
Their API reference here lists all the method:
https://dev.twitter.com/docs/api

Modify your client so you can call other methods, maybe like this:

.. code-block:: bash

  python search_twitter.py --username=pamelafox
  python search_twitter.py --search=python

You can use the `argparse`_ module if you're using Python 2.7 or the `argparse_` module if you're using Python 2.6.


.. _argparse: http://docs.python.org/library/argparse.html
.. _optparse: http://docs.python.org/library/optparse.html


