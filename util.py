import math


def get_subset_survival_probability(sub_set):
	"""
	Gets the survival probability after a first filter has been applied to data
	:param sub_set: data set after filter (eg class or sex)
	:return: probability, value between 0 and 1.
	"""
	survivors = sub_set[sub_set.Survived == 1]  # filter by survivors
	return float(len(survivors)) / float(len(sub_set))  # get quotient between survivors and population of sub_set.


def fill_in_missing_cabin_data(data_set):
	"""
	Most Cabin data is missing therefore it is substituded for consecutive integers. As there are so many rooms
	it is assumed that each passenger is in a different cabin rather than having a single value.
	:param data_set: DataFrame with all fields.
	:return: DataFrame that replaces nan for different numbers.
	"""
	idx = 0
	new_cabins = []
	cabins = list(data_set['Cabin'])
	for e in cabins:
		if not isinstance(e, str) and math.isnan(e):
			e = str(idx)
			idx += 1
		new_cabins.append(e)
	return new_cabins


def fill_in_missing_embarked_data(data_set):
	"""
	Some Embark data is missing therefore a unknown value is added.
	:param data_set: DataFrame with all fields.
	:return: DataFrame that replaces nan for different numbers.
	"""

	new_embark = []
	cabins = list(data_set['Embarked'])
	for e in cabins:
		if not isinstance(e, str) and math.isnan(e):
			e = 'Unknown'
		new_embark.append(e)
	return new_embark


def unique_value_in_series(series):
	"""
	Is the last name unique?
	:param series: DataSeries or column of DataFrame
	:return: Boolean indicating uniqueness
	"""
	return len(set(series)) == 1
