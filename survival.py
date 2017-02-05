

def get_subset_survival_probability(sub_set):
	"""
	Gets the survival probability after a first filter has been applied to data
	:param sub_set: data set after filter (eg class or sex)
	:return: probability, value between 0 and 1.
	"""
	survivors = sub_set[sub_set.Survived == 1]  # filter by survivors
	return float(len(survivors)) / float(len(sub_set))  # get quotient between survivors and population of sub_set.


def get_sex_survival_probability(data_set, sex):
	"""
	Given DataFrame and the_class gets the chance of surviving
	:param data_set: data set
	:param sex: 'male' or 'female'
	:return: probability, value between 0 and 1.
	"""
	sub_set = data_set[data_set.Sex == sex]  # filter by sex.
	return get_subset_survival_probability(sub_set)


def get_class_survival_probability(data_set, the_class):
	"""
	Given DataFrame and the_class gets the chance of surviving
	:param data_set: data set
	:param the_class: 1, 2 or 3
	:return: probability, value between 0 and 1.
	"""
	sub_set = data_set[data_set.Pclass == the_class]  # filter by class.
	return get_subset_survival_probability(sub_set)


def get_class_survival_dict(data_set):
	"""
	Gets dict containing class (1,2,3) as key and survival probability as value.
	:param data_set: DataFrame
	:return: dict
	"""
	return {'first': get_class_survival_probability(data_set, 1),
			'second': get_class_survival_probability(data_set, 2),
			'third': get_class_survival_probability(data_set, 3)}


def get_sex_survival_dict(data_set):
	"""
	Gets dict containing class (1,2,3) as key and survival probability as value.
	:param data_set: DataFrame
	:return: dict
	"""
	return {'female': get_sex_survival_probability(data_set, 'female'),
			'male': get_sex_survival_probability(data_set, 'male')}


def get_survivors(survivor_data):
	"""
	Gets the class with highest survival probability
	:param survivor_data: dict.
	:return: for class: 1, 2, 3. For sex 'female' or 'male'
	"""
	max_prob = -1
	max_property = None
	for k, v in survivor_data.items():
		if v > max_prob:
			max_property = k
			max_prob = v

	return max_property
