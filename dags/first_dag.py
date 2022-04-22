try:
    from datetime import timedelta
    from airflow import DAG 
    from airflow.operators.python_operator import PythonOperator 
    from datetime import datetime
    import pandas as pd 

    print("All Dag modules are ok .......")
except Exception as e:
    print("Error {}".format(e))


def first_function_execute(**context):
    print("first_function_execute")
    context["ti"].xcom_push(key='mykey', value="first_function_execute says Hello")


def second_function_execute(**context):
    instance = context.get("ti").xcom_pull(key="mykey")
    data = [
        {
            "name": "Aravinda", 
            "title": "Full stack Software Engineer",
            "city": "Karnataka City",
        }
    ]

    df = pd.DataFrame(data=data)
    print("@"*66)
    print(df.head())
    print("@"* 66)

    print(
        "Iam in second_function_excute got value : {} from  function 1:".format(instance)
    )


with DAG(
    dag_id='first_dag',
    schedule_interval="@daily",
    default_args={
        "owner": "airflow",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
        "start_date": datetime(2021, 1, 1)
    },
    catchup=False
) as F:

    first_function_execute_op = PythonOperator(
        task_id="first_function_execute",
        python_callable=first_function_execute,
        provide_context=True,
        op_kwargs={"name": "Aravinda"}
    )

    second_function_execute_op = PythonOperator(
        task_id="second_function_execute",
        python_callable=second_function_execute,
        provide_context=True
    )

    first_function_execute_op >> second_function_execute_op