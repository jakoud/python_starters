import pandas as pd


def by_price(lower_bound, upper_bound):
    data = pd.read_csv("cars.csv")
    print(data.query("price > {value}".format(value=lower_bound)).query("price < {value}".format(value=upper_bound))
          .sort_values(by=['price']).to_string())


def max_prices_cars(dataframe):
    makes = set(dataframe['company'])
    indexes = []
    for element in makes:
        data = dataframe.query("company == '{company}'".format(company=element))
        index = data['price'].idxmax()
        indexes.append(data.loc[index, 'index'])
    return dataframe.query("index in {list}".format(list=indexes)).to_string()


def main():
    data = pd.read_csv("cars.csv")
    print(data.groupby('company').size())
    print(data.query("company == 'jaguar'").to_string())
    print(data.groupby('company').mean().sort_values(by=['price'], ascending=False).head(1)['price'])
    print(max_prices_cars(data))
    by_price(10000, 30000)


main()
