import pickle

listexample = ["ss","yy","ddd"]
filename = open("notebook.dat","wb")
pickle.dump(listexample, filename)
filename.close()
filename = open("notebook.dat","rb")
just_read = pickle.load(filename)
print("Following was just read: ",just_read)