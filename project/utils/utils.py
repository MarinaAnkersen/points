def result_as_dict_matches(query_result):
    """Function transforming tuple result of the query into the list of
    dictionaries(JSON).

    :param query_result: result of the query as a tuple with the same amount of
    values as keys in the function
    """
    matches_keys = ['match_id', 'match_date', 'round_name', 'first_squad_name',
                    'first_squad_score', 'first_squad_points',
                    'second_squad_name', 'second_squad_score',
                    'second_squad_points']
    list_of_dict = []
    for i in range(len(query_result)):
        dictionary = dict(zip(matches_keys, query_result[i]))
        list_of_dict.append(dictionary)
        i += 1
    return list_of_dict
