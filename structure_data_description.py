def statistics_description(df):
    print("for which columns statistics?")
    print(list(df.columns))

    cols = input().split(' ')
    cols = list(map(int, cols))
    print(cols)
    pom = df.iloc[:, cols]

    print(pom.describe())
