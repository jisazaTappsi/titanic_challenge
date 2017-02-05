from kmodes import kmodes
import pandas as pd
import util


def get_names(family):
	"""
	Gets the names of the members
	:param family: DataFrame with members
	:return: string with names
	"""
	return '\n'.join(list(family['Name']))


def is_family(family):
	"""
	Strict filter for a family:
	1. has more than 1 member
	2. has common last name.
	3. Cabin/s is/are known and is/are the same.
	:param family: DataFrame with family members.
	:return: boolean
	"""
	cabin = list(family['Cabin'])[0]
	return len(family) > 1\
		and util.unique_value_in_series(family['LastName'])\
		and util.unique_value_in_series(family['Cabin'])\
		and isinstance(cabin, str)


def get_family_set(data_set):
	"""
	Will filter the original data set and do some changes to fit the data into a categorial k-modes
	clustering algorithm.
	:param data_set: DataFrame
	:return: filtered and transformed data_set (aka family_set)
	"""
	# filter for traits that families have in common.
	family_set = pd.DataFrame()
	family_set['LastName'] = data_set['LastName']

	# Tickets are numbers, but they should be categorical.
	family_set['Ticket'] = data_set['Ticket'].apply(lambda t: str(t))

	# Cabins cannot have nan, will assume every nan Cabin is different, becuase of low collisions.
	family_set['Cabin'] = util.fill_in_missing_cabin_data(data_set)

	# the class is categorical.
	family_set['Pclass'] = data_set['Pclass'].apply(lambda c: str(c))

	# nan are removed and replaced by s single value as collisions are likely.
	family_set['Embarked'] = util.fill_in_missing_embarked_data(data_set)

	return family_set


def get_best_family(data_set, num_clusters):
	"""
	The biggest family found with the highest chance of being a family.
	:param data_set: normal DataFrame plus column with clusters (aka families).
	:param num_clusters: number of clusters.
	:return: one family as DataFrame
	"""
	best_family = None
	max_family_size = 0
	num_families_found = 0
	for i in range(num_clusters):
		possible_family = data_set[data_set.cluster == i]
		if is_family(possible_family):
			num_families_found += 1

			if max_family_size < len(possible_family):
				max_family_size = len(possible_family)
				best_family = possible_family

	return best_family


def print_clusters(data_set):
	"""
	Should cluster members of the same family,
	and return the best family (Biggest with highest chance of being family)
	:param data_set: DataFrame
	:return: prints the clusters
	"""
	family_array = get_family_set(data_set).as_matrix()

	num_clusters = 230
	model = kmodes.KModes(n_clusters=num_clusters, init='Huang', n_init=5, verbose=0)
	data_set['cluster'] = model.fit_predict(family_array)

	return get_best_family(data_set, num_clusters)
