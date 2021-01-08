import pickle
a = [1,2,3]
f = open('hi.pkl', 'ab')
pickle.dump(a, f)
f.close()
