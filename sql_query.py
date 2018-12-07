
class SqlQuery:
    def __init__(self, query_str):
        self.SELECT = []
        self.FROM = ''
        self.WHERE = ''
        self.ORDER_BY = []
        self.DISTINCT = False

        self.__parse_query_str(query_str)

    def __parse_query_str(self, query_str):
        # TODO
        return 0
