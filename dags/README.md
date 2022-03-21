# DAGs

This is where all DAGs will live.

## First Dag

After installing Airflow, start it by:

* initializing the metastore (a database in which all AIrflow state is stored);
* creating a user; 
* copying the rocket launch DAG into the DAGs directory; and
* starting the scheduler and webserver

## Setup Instructions and Requirements

This repo assumes you're running a Mac OS.

To recreate the same virtual environment as me, please run the following commands:

* open the terminal;
* navigate to the root of this project folder (you know you're the right place if the last folder you see after running `pwd` results in a file path that ends with `learning_airflow/`); and
* run `sh setup.sh` to execute a series of commands that create a new virtual environment for you named `venv` that ensures your environment looks the same as mine.
