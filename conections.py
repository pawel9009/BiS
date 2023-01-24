import db_info
import get_data
from pathlib import Path
from db_info import *
from sqlalchemy import create_engine
from validation import validate_data
from save_selected_date import save_date
from operations import operations_loop


def connect():
    conn = None
    try:
        conn = db_config
        df = get_data.scrap_data()
        df.to_csv(Path('files/data.csv'), index=False)
        testowa = df.head(5)
        # testowa.Zamkniecie.iloc[1] = 'asdsd'
        # testowa.Otwarcie.iloc[3] = 'asdsd'
        # testowa.Data.iloc[3] = 'asdsd'

        df = validate_data(df)
        # statystyka_odp = input('Display descriptive statistics y/n?')
        # if statystyka_odp == 'y':
        #     print(df.describe())

        engine = create_engine(f"postgresql://{db_info.user}:{db_info.password}@localhost/{db_info.database}")

        # operations_ansver = input('Operations? y/n?')
        # if operations_ansver == 'y':
        operations_loop(engine)

        # save_date_ans = input('Save data?')
        # if save_date_ans == 'y':
        # save_date(df, engine)

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
