**Following simplifications made for sake of assignment:**

Initialization:
- For purposes of this demo, app can be built via docker-compose test env `docker-compose up --build app` to simulate deployed docker container
- Postgres dependency can be built using `docker-compose up --build postgres`
- Postgres database is initialized via docker-compose to simulate a separately initiated container
- Config is set up to take variables from separate env files, but for this demo all variables are set up as defaults

Tests:
- For simplicity, tests will be conducted using the same docker-compose postgres database (in reality production db would always be up in a separate container, while test db would always be re-initiated upon running tests)
- No current handling of other db values that may update upon calling certain functions
- Due to above, if postgres container is not reset (e.g. `docker-compose down; docker-compose up...`), tests may fail
- For simplicity and considering time, automated tests would cover only fundamental functionality of each endpoint (so far)

DB:
- For simplicity, prices are stored as `integers`, not accounting for decimals in the db to avoid complications with decimal conversion
- ^ Converted prices in returned products, however, are displayed up to two decimal places (cents)

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
- More user-friendly, more specific, detailed error messages