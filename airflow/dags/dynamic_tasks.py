"""
Purpose:    DAG for referencing context variables
Date:       April 9, 2022
Author:     Cristian Nuno
"""

# load necessary packages
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator
import csv
from datetime import datetime
import logging

logging.info("create custom python function")
def write_to_csv(templates_dict):
    """Write data to a csv file"""
    # provide feedback about what function is doing
    logger = logging.getLogger(__name__)

    logging.info("Extract the templated output path")
    filename = templates_dict["filename"]
    logging.info(f"The templatized filename is {filename}")

    logging.info("Open the filename")
    with open(filename, mode='w') as csv_file:
        logging.info("Create headers")
        fieldnames = ['emp_name', 'dept', 'birth_month']

        logging.info("Create csv writer object")
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        logging.info("Write the headers to the csv")
        writer.writeheader()
        
        logging.info("Write two rows of data to the csv")
        writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
        writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})


logging.info("instantiate a DAG object")
dynamic_tasks = DAG(
    dag_id="dynamic_tasks",
    # NOTE: modify this to your preference
    start_date=datetime(2022, 4, 8),
    schedule_interval=None,
)

logging.info("create start task")
start = DummyOperator(
    task_id="start", 
    dag=dynamic_tasks
)

logging.info("create report list")
report_dict = {
    "Text": "hello world",
    "Email": "goodbye moon",
}

logging.info("for each report ----")
for report_name, query in report_dict.items():
    logging.info("create write to csv task ds")
    report_csv = PythonOperator(
        task_id=f"{report_name}_write_to_csv",
        python_callable=write_to_csv,
        templates_dict={
            "filename": "{report_name}_data_{ds}".format(
                report_name=report_name,
                ds=r"{{ ds }}"#"{report_name}_data_{{ds}}.csv"
            )
        },
        dag=dynamic_tasks,
    )

    logging.info("set task order")
    start >> report_csv

logging.info("finish with all reports ----")
