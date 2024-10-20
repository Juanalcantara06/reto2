from config import config
from mysql import connector
from prefect import task

@task(name="5. Carga de data en bd")
def task_load_user(user_data):
  with connector.connect(**config.MYSQL_CONFIG) as db:
    with db.cursor() as cursor:
      query_insert = """
        insert into ruc(ruc, nombre_o_razon_social, estado, condicion)
        values(%s, %s, %s, %s)
      """
      cursor.execute(query_insert, user_data)
      db.commit()