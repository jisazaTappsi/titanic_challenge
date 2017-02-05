import pandas as pd
import numpy as np
import survival

# reads file from csv and converts it to DataFrame
data_set = pd.read_csv('./titanicData.csv')


# see unique values and possible missing values of dataframe

fields = list(data_set.columns.values)
fields.remove('PassengerId')

for field in fields:

	print(data_set[field].value_counts())

	# count nan
	print('total count:' + str(len(data_set[field])))
	#print('total nan:' + str(sum([1 for x in list(df[field]) if x == np.nan])))


class_survival = survival.get_class_survival_dict(data_set)

print("""Probabilities of Survival:
First Class: {class1}
Second Class: {class2}
Third Class: {class3}
The {survivors} class had the highest survival chance.
""".format(class1=class_survival['first'],
           class2=class_survival['second'],
           class3=class_survival['third'],
           survivors=survival.get_survivors(class_survival)))


sex_survival = survival.get_sex_survival_dict(data_set)

print("""Probabilities of Survival:
Female: {female}
Male: {male}
The {survivors} gender had the highest survival chance.
""".format(female=sex_survival['female'],
           male=sex_survival['male'],
           survivors=survival.get_survivors(sex_survival)))
