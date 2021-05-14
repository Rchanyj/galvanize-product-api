**Quick start**:

- App can be accessed by first running `docker-compose up --build postgres` and then `docker-compose up --build app`
- Tests can be run by first running postgres container as described above and then running `docker-compose up --build test`
- Endpoints and request specs can be viewed at http://localhost:8080/swagger.
- For easier viewing, the swagger can also be copied to https://editor.swagger.io/
   - **Note: I attempted to use swagger UI's Petstore demo for easy testing of API endpoints, but it had problems loading any HTTP schemes
- This repo can also (for the time being) be viewed at https://github.com/Rchanyj/galvanize-product-api for more details regarding commits, etc.

**Following simplifications made for sake of assignment:**

Initialization:
- For purposes of this demo, app is run in docker-compose to simulate a deployed docker container
- Postgres database is initialized via docker-compose to simulate a separately initiated container
- Config is set up to take variables from separate env files, but for this demo all variables are set up as defaults
- Please initialize postgres db container first: `docker-compose up --build postgres`
- App can be built via `docker-compose up --build app`
- ^ These are done separately to make sure postgres has time to fully build (for simplicity, waiting logic for this was not implemented in the code)

Infrastructure and functionality:
- Due to minimal traffic and simplicity of this demo API, there are currently no async implementations
- A simple in-memory cache is implemented for results from external currency API to simulate caching for potential bottleneck

Tests:
- For simplicity, tests will be conducted using the same docker-compose postgres database (in reality production db would always be up in a separate container, while test db would always be re-initiated upon running tests)
- To ensure a clean test run, please initialize postgres container to ensure a test db reset before running e.g. `docker-compose up --build test`
- No current handling of other db values that may update upon calling certain functions
- Due to above, if postgres container is not reset (e.g. `docker-compose down; docker-compose up...`), tests may fail if run repeatedly
- For simplicity and considering time, automated tests would cover only fundamental functionality of each endpoint (so far)

DB:
- For simplicity, prices are stored as `integers`, not accounting for decimals in the db to avoid complications with decimal conversion
- ^ Converted prices in returned products, however, are displayed up to two decimal places (cents)
- Currently no built in manual or automatic commits for persistence; DB will reset once app and/or postgres containers are closed

-------------------
Assumptions and explanations:

- Currently incrementing views after select query successfully completes to prevent failed requests from incrementing views
- Assumes that task does not ask for returned product views to account for "current" view (will return view_count up until that request)
- Assumes that requesting for a list of most-viewed products does NOT contribute to the view count for each individual product
- ^ Assumes that 'view event' for products only occurs if user specifically looks for a particular product

-------------------

Wishlist:

- Better error handling that covers more cases and is more graceful
- More user-friendly, more specific, detailed error messages
- Monitoring and metrics (e.g. request durations, errors)
- Auth and security features