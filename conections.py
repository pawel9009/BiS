import db_info
import get_data
from pathlib import Path
from db_info import *
from sqlalchemy import create_engine
from validation import validate_data


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        conn = db_config

        df = get_data.scrap_data()
        df.to_csv(Path('files/data.csv'), index=False)
        testowa = df.head(5)

        # testowa.Zamkniecie.iloc[1] = 'asdsd'
        # testowa.Otwarcie.iloc[3] = 'asdsd'
        # testowa.Data.iloc[3] = 'asdsd'

        df = validate_data(testowa)

        engine = create_engine(f"postgresql://{db_info.user}:{db_info.password}@localhost/{db_info.database}")

        df.to_sql(
            "gold_pl",
            engine,
            if_exists='replace',
            index=True,
        )


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


connect()
