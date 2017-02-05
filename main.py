import pandas as pd
import survival
import family

# reads file from csv and converts it to DataFrame
data_set = pd.read_csv('./titanicData.csv')

# extract LastName for family use.
data_set['LastName'] = data_set['Name'].apply(lambda name: name.split(',')[0])
data_set = data_set.sort(['LastName'])

# Class probabilities
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


# Sex probabilities
sex_survival = survival.get_sex_survival_dict(data_set)
print("""Probabilities of Survival:
Female: {female}
Male: {male}
The {survivors} gender had the highest survival chance.
""".format(female=sex_survival['female'],
           male=sex_survival['male'],
           survivors=survival.get_survivors(sex_survival)))


sample_family = family.print_clusters(data_set)

print("""One of the families that traveled in the Titanic were the {last_name}:
{names}
""".format(last_name=list(sample_family['LastName'])[0], names=family.get_names(sample_family)))
