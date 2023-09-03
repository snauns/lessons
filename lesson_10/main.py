from dbcontenxt import DBContext
context = DBContext("students.sl3", 5.0)
#1 CREATE TABLE ... (definition_fields_with_types_constarints)
'''
context.Query("CREATE TABLE V2011(id INT PRIMARY KEY, name VARCHAR(20), age INT, avg_grade FLOAT)")
'''
#2 INSERT INTO ...(name_fields) VALUES()
'''
context.Query("INSERT INTO V2011(id, name, age, avg_grade) VALUES(1, 'Bormatov Ivan', 14, 12)")
context.Query("INSERT INTO V2011(id, name, age, avg_grade) VALUES(2, 'Garkusha Mychaylo', 13, 12)")
context.Query("INSERT INTO V2011(id, name, age, avg_grade) VALUES(3, 'Dedushkin Nikita', 12, 8.5)")
context.Query("INSERT INTO V2011(id, name, age, avg_grade) VALUES(4, 'Lazarchuk Mychaylo', 13, 11.5)")
'''
#3 UPDATE ... SET name_field = value WHERE name_field = value
'''
context.Query("UPDATE V2011 SET avg_grade=9.0 WHERE id=3")
'''
#4 DELETE FROM ... WHERE name_field = value
#4.1 CREATE test record
'''
context.Query("INSERT INTO V2011(id, name, age, avg_grade) VALUES(5, 'test', 0, 0)")
'''
#4.2 DELETE test record
'''
context.Query("DELETE FROM V2011 WHERE id=5")
'''
#5 SELECT ..... FROM ...
'''
res = context.Execute("SELECT id, name, age, avg_grade FROM V2011")#DEFAULT ORDER BY id ASC
res = context.Execute("SELECT id, name, age, avg_grade FROM V2011 ORDER BY id DESC")
res = context.Execute("SELECT avg_grade, name FROM V2011 ORDER BY avg_grade DESC")
print(res)
'''
#6 DROP TABLE
#context.Query("CREATE TABLE V2011TEST(id INT PRIMARY KEY, name VARCHAR(20), age INT, avg_grade FLOAT)")
#context.Query("DROP TABLE V2011TEST")