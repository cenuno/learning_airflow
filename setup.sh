echo "Start customizing where Airflow Home is located at $(date)"

# customize where the DAGs in airflow should be sourced from
AIRFLOW_HOME_COMMENT="# Airflow needs a home. `~/airflow` is the default, but we will place it elsewhere."
# NOTE: change the value here if you need it to live elsewhere
AIRFLOW_HOME_CMD="export AIRFLOW_HOME=~/Documents/learning_airflow/airflow"
echo "${AIRFLOW_HOME_COMMENT}\n${AIRFLOW_HOME_CMD}\n" >> ~/.zshrc

# reload the environment variables from the z shell resource file
source ~/.zshrc

echo "Finish customizing where Airflow Home is located at $(date)"

echo "Start recreating virtual environment at $(date)"

# create new virtual environment named venv
python3 -m venv venv

# activate the virtual environment named venv
source "./venv/bin/activate"


# install the same exact packages that I used which are stored in a .txt file
pip3 install -r requirements.txt

echo "Finish recreating virtual environment at $(date)"
