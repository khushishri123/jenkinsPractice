# Here we will be creating a map.
data={1:'Khushi',2:'Stuti',3:'Deepak',4:'Preeti'}
print(data[1])
# or we can also write: map.get(1) but it is more efficient because if a particular key is not present than map[1] will give an
# exception while get method will return None.
print(data.get(5))
#Also if a key is not present and you want that get should return this particular value then you can write:
print(data.get(5,'William'))
#Now if I have two lists : keys and values and I want to create a dict where keys will be key and values will be value,then:
keys=['Khushi','Stuti','Siddhi']
values=['C','C++','Java']
data=dict(zip(keys,values))
print(data)
#We can also create a dict having value as a list or a dict itself:
data={'JS':'Atom','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print(data['Python'])
print(data['Python'][0])
print(data['Java']['JEE'])