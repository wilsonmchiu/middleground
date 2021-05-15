# CSE 115a - Middle Ground

TO RUN: fire up the server and client. Open up a new terminal, go back to the same location (open up venv in middleground/src/server/mgflask)

Run `python3` and `from mgflask import test_news`

Insert articles into db: `test_news.test_retrieval()`

Test endpoints: `test_news.test_endpoint()`

The client fetches articles from the current day.

Running `test_news.test_retrieval()` only ensures that the database has the up-to-date articles for one day. If the client fails to display any article, try running `test_news.test_retrieval()` again to update the database.

-------

We are currently using JIRA for our scrum board. If you are the TA/tutor, please email wmchiu@ucsc.edu for access.
