#=============================================================================#
#                            Homework 4: yourSQL                              #
#         SI 100B: Introduction to Information Science and Technology         #
#                     Spring 2020, ShanghaiTech University                    #
#                     Author: Diao Zihao <hi@ericdiao.com>                    #
#                         Last motified: 02/18/2020                           #
#=============================================================================#
# Implement your database here.


class Row():
    """
    The `Row` class.

    You are building the row class here.
    """

    def __init__(self, keys, data, primary_key=None):
        '''
            The arguments are of illegal types (raise TypeError);
            The keys and the data are of different length (raise keyError);
            The keys or the data  contains no element (raise ValueError).
        '''
        if type(keys) != list or type(data) != list:
            raise TypeError
        if len(keys) != len(data):
            raise KeyError
        if (not keys) or (not data):
            raise ValueError

        self.__keys = keys
        self.__dict = dict()
        length = len(keys)
        for i in range(length):
            self.__dict[keys[i]] = data[i]

        '''
        If it is set to None, use the first field in keys as the primary key.
        Otherwise, use the given string value as the primary key.
        Raise KeyError if the primary_key is not in the row.
        '''
        if not primary_key in keys and primary_key != None:
            raise KeyError
        elif primary_key != None:
            self.__primary_key = primary_key
        else:
            self.__primary_key = keys[0]

    def __getitem__(self, key):
        '''
            Row[key] = item
        '''
        if key not in self.__dict:
            raise KeyError
        try:
            return self.__dict[key]
        except:
            raise KeyError

    def __setitem__(self, key, value):
        if key not in self.__dict:
            raise KeyError
        try:
            self.__dict[key] = value
        except:
            raise KeyError

    def __iter__(self):
        self.__a = sorted(self.__dict.keys())
        # print('self.a', self.a)
        self.__b = 0
        return self

    def __next__(self):
        if self.__b < self.__len__():
            x = self.__b
            self.__b += 1
            # print(self.b, self.a[x][0])
            return (self.__a[x][0])
        else:
            self.__b = 0
            raise StopIteration

    def __len__(self):
        return len(self.__dict)

    def __lt__(self, other):
        if type(other) is not Row or self.get_primary_key() != other.get_primary_key() or self.keys() != other.keys():
            raise TypeError

        try:
            if self[self.get_primary_key()] < other[other.get_primary_key()]:
                return True
        except:
            raise TypeError

    def keys(self):
        return sorted(self.__dict.keys())

    def get_primary_key(self):
        return self.__primary_key


class Table():
    """
    The `Table` class.

    This class represents a table in your database. The table consists
    of one or more lines of rows. Your job is to read the content of the table
    from a CSV file and add the support of iterator to the table. See the
    specification in README.md for detailed information.
    """

    def __init__(self, filename, rows=None, keys=None, primary_key=None):
        self.__filename = filename
        self.__list = list()
        self.__first_list = list()

        '''
            Case 1: rows=None, keys=None
        '''
        if rows == None and keys == None:

            # Read Files
            f = open(filename, mode='r')
            str_list = list()
            for i in f.readlines():
                str_list.append(i.strip())

            # Establish key list
            self.__first_list = str_list[0].split(',')
            self.__first_list = [i.strip() for i in self.__first_list]
            # print(self.__first_list)
            # Set primary key
            if not primary_key in self.__first_list and primary_key != None:
                raise KeyError
            if primary_key != None:
                self.__primary_key = primary_key
            else:
                self.__primary_key = self.__first_list[0]

            # Establish Rows
            str_list.pop(0)
            # print(self.first_list)
            # print(self.__primary_key)
            # print(str_list)
            for i in str_list:
                tmp = i.split(',')
                tmp = [i.strip() for i in tmp]
                tmp_list = list()
                for j in tmp:
                    try:
                        if '.' in j:
                            tmp_list.append(float(j))
                        else:
                            tmp_list.append(int(j))
                    except:
                        tmp_list.append(j)
                # print(tmp_list)
                self.__list.append(
                    Row(self.__first_list, tmp_list, self.__primary_key))
            # print(self.first_list)
            # print(self.list)
            f.close()
        '''
            Case 2: rows != None and keys != None
        '''
        if rows != None and keys != None:
            self.__first_list = keys

            if primary_key != None and not primary_key in keys:
                raise KeyError
            if primary_key == None:
                self.__primary_key = keys[0]
            else:
                self.__primary_key = primary_key

            for i in rows:
                self.__list.append(i)

    def __iter__(self):
        self.__a = sorted(self.__list)
        # print('self.__a', self.__a)
        self.__b = 0
        return self

    def __next__(self):
        if self.__b < self.__len__():
            x = self.__b
            self.__b += 1
            return (self.__a[x])
        else:
            self._b = 0
            raise StopIteration()

    def __getitem__(self, key):
        for i in self.__list:
            if i[self.__primary_key] == key:
                return i
        raise ValueError

    def __len__(self):
        return len(self.__list)

    def get_table_name(self):
        return self.__filename

    def keys(self):
        return sorted(self.__first_list)

    def get_primary_key(self):
        return self.__primary_key

    def export(self, filename=None):
        if not filename:
            filename = self.get_table_name()
        f = open(filename, 'w')
        for i in self.__first_list:
            f.write(i)
            if i == self.__first_list[-1]:
                f.write('\n')
            else:
                f.write(',')
        for i in self.__list:
            k = len(self.__first_list)
            for j in self.__first_list:
                f.write(str(i[j]))
                if k == 1:
                    f.write('\n')
                else:
                    f.write(',')
                    k -= 1
        f.close()


class Query():
    """
    The `Query` class.
    """

    def __init__(self, query):
        self.select = query['select']
        self._from = query['from']
        self.where = query['where']
        self.table = Table(filename=self._from)
        self.list  = list()
        if self.table.get_primary_key() not in self.select:
            self.select.append(self.table.get_primary_key())
        for i in self.select:
            if i not in self.table.keys():
                raise KeyError

    def as_table(self):
        self.list = list()
        for i in self.table:
            flag = 1
            for j in self.where:
                # if j[0] not in self.select:
                #     raise KeyError
                if flag:
                    if eval('i[ j[0] ]' + j[2] + 'j[1]'):
                        flag = 1
                    else:
                        flag = 0
            if flag:
                self.list.append(i)

        tmp_row = list()
        for i in self.list:
            tmp_row.append(
                Row(self.select, [i[key] for key in self.select], self.table.get_primary_key()))
        # print(self._from)
        # print(self.table.get_primary_key())
        # print('00000000000000000')
        result = Table(self._from, tmp_row, self.select,
                       self.table.get_primary_key())
        # result.export('output')
        return result


class JoinQuery(Query):

    def __init__(self, query):
        if type(query['from']) is not list:
            super().__init__(query)
            return

        self.select = query['select']
        self._from = query['from']
        self.where = query['where']
        self.table0 = Table(filename=self._from[0])
        self.table1 = Table(filename=self._from[1])

        self.list = list()

        pk = list()
        pk.append(self.table0.get_primary_key())
        pk.append(self.table1.get_primary_key())

        self.__head = [i.replace('.csv', '.') for i in self._from]

        flag = 1
        for i in range(2):
            if self.__head[i] + pk[i] in self.select:
                self.__primary_key = self.__head[i] + pk[i]
                flag = 0
        if flag:
            self.__primary_key = self.__head[0] + pk[0]
            self.select.append(self.__primary_key)

        # print(self.__primary_key)
        self.__key_list = list()
        for i in self.table0.keys():
            self.__key_list.append(self.__head[0] + i)
        for i in self.table1.keys():
            self.__key_list.append(self.__head[1] + i)
        # print(self.__key_list)
        # print('00000000000000000000')
        row_list = list()
        for i in self.table0:
            tmp = list()
            for j in self.table1:
                if i[pk[0]] == j[pk[1]]:
                    for m in i.keys():
                        tmp.append(i[m])
                    for m in j.keys():
                        tmp.append(j[m])
            # print(self.__key_list)
            # print(tmp)
            # print(self.__primary_key)
            row_list.append(Row(self.__key_list, tmp, self.__primary_key))
        # Table('join.csv', row_list, self.__key_list, self.__primary_key)
        self._from = 'join.csv'
        self.table = Table('join.csv', row_list,
                           self.__key_list, self.__primary_key)
        # print(self.__key_list)
        # print(self.where)
        # print(self.select)


class AggQuery(Query):
    """
    The `AggQuery` class
    """

    def __init__(self, query):

        self.select = query['select']
        self._from = query['from']
        self.group_by = query['group_by']
        self.where = query['where']

        if self.group_by not in self.select:
            self.select.append(self.group_by)

        q = {
            'select': Table(query['from']).keys(),
            'from': query['from'],
            'where': query['where']
        }

        table = Query(q).as_table()
        table.export('aaa')

        group_set = set()
        for i in table:
            group_set.add(i[self.group_by])
        print(group_set)
        grouped_tables = {}

        for i in group_set:
            tmp = []
            for j in table:
                if j[self.group_by] == i:
                    tmp.append(j)
            grouped_tables[i] = Table(i, tmp, tmp[0].keys(), table.get_primary_key())

        new_row_list = []
        print(self.select)
        print(self.group_by)

        for i in group_set:
            tmp = []
            for j in self.select:
                group = grouped_tables[i]
                print(group)
                if j == self.group_by:
                    tmp.append(i)
                else:
                    op = j[:3]
                    key = j[4:-1]
                    if op == 'MAX':
                        tmp.append(max([k[key] for k in group ]))
                    if op == 'MIN':
                        tmp.append(min([k[key] for k in group ]))
                    if op == 'SUM':
                        tmp.append(sum([k[key] for k in group]))
                    if op == 'AVG':
                        tmp.append(sum([k[key] for k in group]) / len(group))
            new_row_list.append(Row(self.select, tmp, self.group_by))
        self.table  = Table(self._from, new_row_list, self.select, self.group_by)
        self.list = []
 