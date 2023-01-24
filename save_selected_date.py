def save_date(df, engine):
    pom = None
    while True:
        ans = input("if you want save one day write in format YYYY-MM-DD if whole month YYYY-MM")
        if len(df[df['Data'] == ans]) == 1:
            pom = df[df['Data'] == ans]
            break
        elif len(df[df['Data'].str[:7] == ans]) > 1:
            pom = df[df['Data'].str[:7] == ans]
            break
        else:
            print('bledna data')
            again = input("again?")
            if again == 'y':
                continue
            elif again == 'n':
                break

    pom.to_sql(
        "archive",
        engine,
        if_exists='append',
        index=True,
    )
    print('Saved ...')
