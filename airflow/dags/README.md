# DAGs

This is where all DAGs will live, which are essentially Python scripts that describe the structure of the corresponding DAG.

## Testing

To test individual tasks within a particular DAG, you can use the command line command:

```bash
airflow tasks test <DAG ID> <Task ID> <YYYY-MM-DD>
```

For instance, to test the `notify` task within the `download_rocket_launches` DAG, I'd modify the command above like so:

```bash
airflow tasks test download_rocket_launches notify 2022-03-21
```