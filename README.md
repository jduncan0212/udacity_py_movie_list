# udacity_py_movie_list: from Udacity's "Fresh Tomatoes" Webpage Prompt
A simple python project that generates a Bootstrap Style static html page with a list of predefined movies and their trailers on https://www.youtube.com 

To use: clone and directly access the html page at: fresh_tomatoes.html

Or, to generate a new/different fresh_tomatoes.html; after cloning, just change the movies listed in media_presenter.py and run it.

#Addition to vanilla project:

"Well basically, I just copied the plant we have now. Then, I added some fins to lower wind resistance. And this racing stripe here I feel is pretty sharp. "
--Homer Simpson

I added a mouseout feature to show the one-line movie summaries ... The way I implemented it is to generate script dynamically based on the movies added in the media_presenter.py file. The advantage is this functionality can be used with different lists of movies simply by adding/removing movies changing media_presenter.py ( without touching fresh_tomatoes.py ) ...

...However, I'm sure there is a (much) simpler and less error prone way to achieve the same effect, if you are reading this maybe you can add one?
