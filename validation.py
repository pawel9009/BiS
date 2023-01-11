from dateutil.parser import parse
import warnings

warnings.filterwarnings('ignore')


def validate_data(data):
    dates = list(data.Data)

    for i, val in enumerate(dates):
        try:
            parse(val)
        except Exception as e:
            print(f'error in {i} row, unvalid value - {val}')
            data.drop(data.index[i], axis=0, inplace=True)
            print(e.args)

    otwarcie = list(data.Otwarcie)
    najwyzszy = list(data.Najwyzszy)
    najnizszy = list(data.Najnizszy)
    zamkniecie = list(data.Zamkniecie)

    numeric_values = [otwarcie, najnizszy, najwyzszy, zamkniecie]

    for index, n_value in enumerate(numeric_values):
        for i, val in enumerate(n_value):
            try:
                int(val) or float(val)
            except Exception as e:
                print(f'error in {i} row, unvalid value - {val}')
                data.drop(data.index[i], axis=0, inplace=True)
                print(e.args)

    return data
