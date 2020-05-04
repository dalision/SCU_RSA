import generator
import IO
import tools
def encode(e,p,n):
    c = tools.exp_mode(e,p,n)
    return str(hex(c))[2:]
if __name__ == "__main__":
    p,n,e,d = IO.readfile()
    c1 = encode(p,e,n).upper()
    c2 = encode(p,d,n).upper()
    f =  open('c1.txt','a')
    print(c1,file=f)
    print(c2,file=f)
    f.close()
    