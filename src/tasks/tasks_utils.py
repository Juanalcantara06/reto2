from prefect import task
from config import config
from mysql import connector

@task(name="1. Inicializar la tabla de ruc")
def task_init_table():
  try: 
    with connector.connect(**config.MYSQL_CONFIG) as db:
      with db.cursor() as cursor:
          query_drop_table = "drop table if exists ruc"

          cursor.execute(query_drop_table)
          db.commit()

          query_create_table = """
          create table if not exists ruc(
            id int auto_increment primary key,
            ruc varchar(20),
            nombre_o_razon_social varchar(255),
            estado varchar(255),
            condicion varchar(255)
          )
          """
          cursor.execute(query_create_table)
          db.commit()
  except Exception as error:
     print("error: ", error)


@task(name="3. Consultar la existencia de un ruc en la db")
def task_get_user_from_db(ruc):
   with connector.connect(**config.MYSQL_CONFIG) as db:
      with db.cursor() as cursor:
         query_select_one = "select * from ruc where ruc = %s"
         cursor.execute(query_select_one, (ruc,))
         user = cursor.fetchone()
         return user