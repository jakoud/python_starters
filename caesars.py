import pandas as pd
import matplotlib.pyplot as plt


def caesars_1():
    data = pd.read_csv("rome.csv")
    df_top = data.sort_values(by='Length_of_Reign', ascending=False).head(10)
    df_top.plot.barh(y='Length_of_Reign', x='Emperor', legend=None)
    plt.ylabel('Emperor')
    plt.xlabel('Length of Reign')
    plt.show()


caesars_1()


def caesars_2():
    data = pd.read_csv("rome.csv")
    df = pd.DataFrame(data)
    frequencies = df['Cause_of_Death'].value_counts()
    condition = frequencies < 5
    mask_obs = frequencies[condition].index
    mask_dict = dict.fromkeys(mask_obs, 'Other')
    df2 = df['Cause_of_Death'].replace(mask_dict).value_counts()

    plt.figure(1)
    frequencies.plot.pie(title='Causes of Death')
    plt.ylabel('')

    plt.figure(2)
    df2.plot.pie(title='Causes of Death with threshold')
    plt.ylabel('')
    plt.show()


caesars_2()
