#encoding:UTF-8
import tools as t
from pyunit_prime import get_large_prime_length,get_large_prime_bit_size
from IO import save
def key_gen(n):
    #生成大素数
    for _ in range(4):
        p = get_large_prime_length(n)
        q = get_large_prime_length(n)
        while(p==q):
            q = get_large_prime_length(n)
    print(p)
    print(q)
    n =  p*q
    n1 = (p-1)*(q-1)
    #默认为65537
    e = 65537
    r,d,l = t.ext_gcd(e, n1)
    if d<0:
        d = d+n1
    
    return p,q,n,e,d


if __name__ == "__main__":
    p,q,n,e,d = key_gen(20)
    save(p,"p.txt")
    save(q,"q.txt")
    save(n,"n.txt")
    save(e,"e.txt")
    save(d,"d.txt")

