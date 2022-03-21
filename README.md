# Data Pipelines with Apache Airflow

Using ["Data Pipelines with Apache Airflow" book](https://www.manning.com/books/data-pipelines-with-apache-airflow), written by Bas Harenslak and Julian de Ruiter, this repo tracks my journey to getting familiar with this technology. Most code comes from the authors so please buy their book for more context!

## Setup Instructions and Requirements

### Mac OS requirement

This repo assumes you're running a Mac OS.

### `zsh` requirement

This repo assumes you're using `zsh` as the default shell. [Read more here](https://www.theverge.com/2019/6/4/18651872/apple-macos-catalina-zsh-bash-shell-replacement-features).

To ensure you're setup correctly, please run the following command within the Terminal after cloning the repository:

```bash
# setup your airflow home & virtual environment
sh setup.sh
```

### Change `AIRFLOW_HOME` to point to this project directory

`AIRFLOW_HOME` is the environment variable that points to the folder where your airflow pipelines live. By default, it's located at `~/airflow/` but we are changing it to point to `~/Documents/learning_airflow/airflow/`.

#### Warning

You may have `learning_airflow/` located elsewhere. Be sure to change the `AIRFLOW_HOME_CMD` variable in `setup.sh` to point to where it lives on your machine.

For my machine, that's the Documents folder under the root directory.

### Use `venv` to recreate the virtual environment

To recreate the same virtual environment as me, please run the following commands:

* open the terminal;
* navigate to the root of this project folder (you know you're the right place if the last folder you see after running `pwd` results in a file path that ends with `learning_airflow/`); and
* run `sh setup.sh` to execute a series of commands that create a new virtual environment for you named `venv` that ensures your environment looks the same as mine.
