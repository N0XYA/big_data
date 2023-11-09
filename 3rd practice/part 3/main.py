import pandas as pd
import numpy as np
import scipy.stats as sts


def sample(df):
    south = []
    north = []
    for i in df.values:
        if i[1] == 'northwest':
            north.append(i[0])
        else:
            south.append(i[0])
    south = np.array(south)
    north = np.array(north)
    # t_criter_south = (np.mean(south) - np.mean(north))/np.sqrt((south.std()**2/len(south)) + (north.std()**2/len(north)))
    print("southwest ", sts.shapiro(south))
    print("northwest ", sts.shapiro(north))
    print("Критерий Бартлетта ", sts.bartlett(south, north))
    print("t-критерий Стьюдента = ", sts.ttest_ind(south, north))
    # print("t-критерий Стьюдента = ", t_criter_south)
    return


def cube():
    kybik = [97, 98, 109, 95, 97, 104]
    print(sts.chisquare(kybik))
    print("===============================")
    data = pd.DataFrame({'Женат': [89, 17, 11, 43, 22, 1],
                         'Гражданский брак': [80, 22, 20, 35, 6, 4],
                         'Не состоит в отношениях': [35, 44, 35, 6, 8, 22]})
    data.index = ['Полный рабочий день', 'Частичная занятость', 'Временно не работает',
                  'На домохозяйстве', 'На пенсии', 'Учёба']
    print(sts.chi2_contingency(data))
    return


def main():
    df = pd.read_csv("bmi.csv")
    # print(df.head())
    # sample(df)
    cube()
    return


if __name__ == "__main__":
    main()