**Following simplifications made for sake of assignment:**

- For purposes of this demo, app can be built via docker-compose test env `docker-compose up --build app` to simulate deployed docker container
- Postgres database is initialized via docker-compose to simulate a separately initiated container
- For simplicity, tests will be conducted using this same docker-compose database (in reality production db would always be up in a separate container)

-------------------
To do:
- Find service that can supply a simple GUI to better view requests?


-------------------

Wishlist:

- Better error handling that covers more cases
- More user-friendly, more detailed error messages