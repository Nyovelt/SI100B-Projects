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
            self.__first_list = [str(i.strip()) for i in self.__first_list]
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
        self.__first_list = sorted(self.__first_list)
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
        for i in self.table: # i: Rows
            flag = 1
            for j in self.where:
                # if j[0] not in self.select:
                #     raise KeyError
                if flag:
                    if eval('i[ j[0] ]' + j[2] + 'j[1]'):
                        flag = 1
                    else:
                        flag = 0 #丢掉不符合的
            if flag:
                self.list.append(i)

        tmp_row = list()
        for i in self.list:
            tmp_row.append(
                Row(self.select, [i[key] for key in self.select], self.table.get_primary_key()))

        result = Table(self._from, tmp_row, self.select,
                       self.table.get_primary_key())
        return result


class JoinQuery(Query):

    def __init__(self, query):
        self.select = query['select']
        self._from = query['from']
        self.where = query['where']

        # 分别建立两个新的table
        table0 = Table(filename=self._from[0])
        table1 = Table(filename=self._from[1])

        self.list = list()

        #设置两个primary key
        pk = list()
        pk.append(table0.get_primary_key())
        pk.append(table1.get_primary_key())

        head = [i.replace('.csv', '.') for i in self._from]

        #决定最终的primary_key
        flag = 1
        for i in range(2):
            if head[i] + pk[i] in self.select and flag:
                primary_key = head[i] + pk[i]
                flag = 0
        if flag:
            primary_key = head[0] + pk[0]
            self.select.append(primary_key)



        #确定key list
        key_list = list()
        for i in table0.keys():
            key_list.append(head[0] + i)
        for i in table1.keys():
            key_list.append(head[1] + i)
        

        row_list = list()
        for i in table0:
            tmp = list()
            flag = 1
            for j in table1:
                if flag and i[pk[0]] == j[pk[1]]: #如果两个主键对应的值相同
                    for m in i.keys():
                        tmp.append(i[m])
                    for m in j.keys():
                        tmp.append(j[m])
                    row_list.append(Row(key_list, tmp, primary_key))  #建立新的row
                    flag = 0

        self.table = Table('join.csv', row_list,
                           key_list, primary_key)
        self.table.export('aa')
        self._from = 'join.csv'


class AggQuery(Query):
    """
    The `AggQuery` class
    """

    def __init__(self, query):

        self.select = query['select']
        self._from = query['from']
        group_by = query['group_by']
        self.where = query['where']

        if group_by not in self.select:
            self.select.append(group_by)

        q = {
            'select': Table(query['from']).keys(),
            'from': query['from'],
            'where': query['where']
        }

        table = Query(q)
        table = table.as_table()
        # table.export('aaa')

        group_set = list()
        for i in table:
            if i[group_by] not in group_set:
                group_set.append(i[group_by])
        # print(group_set)
        grouped_tables = dict()

        for i in group_set:
            tmp = []
            for j in table:
                if j[group_by] == i:
                    tmp.append(j)
            if tmp:
                grouped_tables[i] = Table(i, tmp, tmp[0].keys(), table.get_primary_key())

        new_row_list = list()
        # print(self.select)
        # print(group_by)

        for i in group_set:
            tmp = []
            for j in self.select:
                group = grouped_tables[i]
                # print(group)
                if j == group_by:
                    tmp.append(i)
                else:
                    op = j[:3]
                    key = j[4:-1]
                    if op == 'MAX':
                        max = -999999999999
                        for k in group:
                            if k[key] > max:
                                max = k[key]
                        tmp.append(max)
                    if op == 'MIN':
                        min = 999999999999
                        for k in group:
                            if k[key] < min:
                                min = k[key]
                        tmp.append(min)
                    if op == 'SUM':
                        _sum = 0
                        for k in group:
                            _sum += k[key]
                        tmp.append(_sum)
                    if op == 'AVG':
                        _sum = 0
                        for k in group:
                            _sum += k[key]
                        _sum = _sum / len(group)
                        # print(group)
                        # print(len(group))
                        tmp.append(_sum)
            new_row_list.append(Row(self.select, tmp, group_by))
        self.table  = Table(self._from, new_row_list, self.select, group_by)
        self.list = []
 