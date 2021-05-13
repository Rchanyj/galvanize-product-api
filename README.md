**Following simplifications made for sake of assignment:**

- For purposes of this demo, app can be built via docker-compose test env `docker-compose up --build app` to simulate deployed docker container
- Postgres dependency can be built using `docker-compose up --build postgres`
- Postgres database is initialized via docker-compose to simulate a separately initiated container
- For simplicity, tests will be conducted using this same docker-compose database (in reality production db would always be up in a separate container, while test db would always be re-initiated upon running tests)
- Due to above, if postgres container is not reset (e.g. `docker-compose down; docker-compose up...`), tests may fail
- For simplicity and considering time, not all functionalities in this demo may have specific tests

-------------------
Assumptions and explanations:

- Currently incrementing views after select query successfully completes to prevent failed requests from incrementing views
- Assumes that task does not ask for returned product views to account for "current" view (will return view_count up until that request)

-------------------
To do:
- Find service that can supply a simple GUI to better view requests?
- Make GitHub repo public so commit history is accessible

-------------------

Wishlist:

- Better error handling that covers more cases
- More user-friendly, more detailed error messages