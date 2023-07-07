import pickle

my_dict = {'neut': 1, 'geo':22, 'neo': 100}

#terate over the dict
for key,value in my_dict.items():
    print(key, value)

#serialize in a file
with open('my_dict.pickle', 'wb') as handle:
    pickle.dump(my_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print("*"*50)


#serialize
serialised = pickle.dumps(my_dict)
print(serialised)

#deserialize
deserialised = pickle.loads(serialised)
print(deserialised)

#iterate over the dict
for key,value in deserialised.items():
    print(key, value)

#open pickle file
with open('my_dict.pickle', 'rb') as handle:
    deserialised = pickle.load(handle)
    print(deserialised)