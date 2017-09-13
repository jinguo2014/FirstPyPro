s="ilovepython"
str1=s[1:5]
print(s)
print(str1)
print(s*2)
print("祝各位身体健康", end=' ')
print("！")

list=["runoob",875,2.22,"john",70.2]
tinylist=[123,"hehe"]

print(list[1:3])
print(tinylist*2)
print(list+tinylist)

tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print(tuple)
print(tuple+tinytuple)

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print (dict['one']     )     # 输出键为'one' 的值
print (dict[2])              # 输出键为 2 的值
print (tinydict['code'] )            # 输出完整的字典
print (tinydict.keys() )     # 输出所有键
print (tinydict.values())    # 输出所有值

if(not False):
    print("ssss")

flag=False
name="sss"
if name=="python":
    flag=True
    print("welcome boss")
else:
    print(name)



