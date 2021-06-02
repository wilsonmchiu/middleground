# CSE 115a - Middle Ground

TO RUN: fire up the server and client. Open up a new terminal, go back to the same location (open up venv in middleground/src/server/mgflask)

Run `python3` 

1) import new_retrieval into python REPL
`from mgflask import news_retrieval`

2) Insert articles into db: 
`news_retrieval.populate_db()`

The client fetches articles from the current day.

Running `news_retrieval.populate_db()`only ensures that the database has the up-to-date articles for one day. If the client fails to display any article, try running `news_retrieval.populate_db()` again to update the database.

-------

We are currently using JIRA for our scrum board. If you are the TA/tutor, please email wmchiu@ucsc.edu for access.
