def write_data():
    import pickle
    f1=open('product.dat','wb')
    p=eval(input('enter id, name, cost'))
    pickle.dump(p, f1)
    f1.close()
def read_data():
    import pickle
    f2=open('product.dat','rb')
    try:
        while True:
            p1= pickle.load(f2)
            print(p1)
    except EOFError:
        pass
    f2.close()

#main
write_data()
read_data()