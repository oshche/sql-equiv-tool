from sql_query import SqlQuery


def check_equiv(query1: str, query2: str) -> (bool, str):
    _query1 = SqlQuery(query1)
    _query2 = SqlQuery(query2)

    if _query1.SELECT != _query2.SELECT:
        return (False, 'mismatch in SELECT')
    if _query1.FROM != _query2.FROM:
        return (False, 'mismatch in FROM')
    if _query1.DISTINCT != _query2.DISTINCT:
        return (False, 'mismatch in DISTINCT')

    # TODO

    return (True, '')
