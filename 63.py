import pickle

# Pickling a python object
# cars = ['Rolls royce', 'BMW', 'Lamborghini', 'Mercedes Benz']
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))
