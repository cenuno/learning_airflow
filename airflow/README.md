# Airflow

## Run Airflow in a Python environment

After installing Airflow, start it by:

* initializing the metastore (a database in which all Airflow state is stored);
* creating a user;
* copying the rocket launch DAG into the DAGs directory;
    + NOTE: this is done by default for you already
* starting the scheduler and webserver
    + NOTE: both of these bash commands will be constantly running so, after executing each command, you should open up a new Terminal tab so you can continue

```bash
# initialize metastore
airflow db init

# create a user
airflow users create --username admin --password admin --firstname Anonymous --lastname Admin --role Admin --email admin@example.org

# start the webserver
# NOTE: this will be constantly running so be sure to open a new Terminal tab
airflow webserver

# start the scheduler
# NOTE: this will be constantly running so be sure to open a new Terminal tab
airflow scheduler
```