"""
Purpose:    DAG for downloading and processing rocket launch data
Date:       March 20, 2022
Author:     Cristian Nuno
"""

# load necessary packages
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import (
    datetime,
)
import json
import os
import pathlib
import requests
import requests.exceptions as requests_exceptions

# parse the API response and download all rocket pictures
def _get_pictures():
    """Parse the space devs API response and download all rocket pictures
    
    All images will be placed into a temporary images/ dir

    Args:
        None

    Returns:
        None
    """
    # store target directory
    TARGET_DIR = os.path.join("tmp", "images")

    # ensure directory exists
    pathlib.Path(TARGET_DIR).mkdir(parents=True, exist_ok=True)

    # download all pictures in launches.json
    with open("/tmp/launches.json") as f:
        # cast json into dictionary
        launches = json.load(f)

        # parse the rocket image URLs
        image_urls = [launch["image"] for launch in launches["results"]]

        # for each image URL
        for image_url in image_urls:
            try:
                response = requests.get(image_url)
                image_filename = image_url.split("/")[-1]
                target_file = os.path.join(TARGET_DIR, image_filename)
                with open(target_file, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {image_url} to {target_file}")
            except requests_exceptions.MissingSchema:
                print(f"{image_url} appears to be an invalid URL.")
            except requests_exceptions.ConnectionError:
                print(f"Could not connect to {image_url}.")


# instantiate a DAG object
download_rocket_launches = DAG(
    dag_id="download_rocket_launches",
    # NOTE: modify this to your preference
    start_date=datetime(2022, 3, 20),
    schedule_interval=None,
)

# apply bash command to download the URL response with curl
download_launches = BashOperator(
    task_id="download_launches",
    bash_command="curl -o ~/Documents/learning_airflow/tmp/launches.json -L 'https://ll.thespacedevs.com/2.0.0/launch/upcoming'",
    dag=download_rocket_launches,
)

# apply python function to store rocket images
get_pictures = PythonOperator(
    task_id="get_pictures",
    python_callable=_get_pictures,
    dag=download_rocket_launches,
)

# notify user about how many rocket images there now are for viewing
notify = BashOperator(
    task_id="notify",
    bash_command='echo {{ macros.ds_add(ds, -3) }}',
    #bash_command='echo "There are now $(ls ~/Documents/learning_airflow/tmp/images/ | wc -l) images."',
    dag=download_rocket_launches,
)

# set the order of execution tasks
download_launches >> get_pictures >> notify
