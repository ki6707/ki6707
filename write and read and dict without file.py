import pickle
ab={"name":"ravi","age":34}
bc={"name":"kavi","age":34}
db={}
db[123]=ab
db[456]=bc
sk=pickle.dumps(db)
my=pickle.loads(sk)
print(my)