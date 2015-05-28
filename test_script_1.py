from database_call_v0 import lgdb_tools

a = lgdb_tools()

variable_name = 'MWPC.ZT8.135:PROFILE_H'
t1 = '2015-05-01 12:00:00'
t2 = '2015-05-01 14:00:00'
filename = 'file1'

test = a.get_data(variable_name, t1, t2, filename)

for line in test:
    print line
