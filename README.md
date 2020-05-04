# （1） 要求实现 RSA 的密钥生成

> a. 随机选择两个不相等的质数p和q
>
> b. 计算p和q的乘积n
>
> c. 计算n的欧拉函数φ(n)
>
> d. 随机选择一个整数e，条件是1< e < φ(n)，且e与φ(n) 互质,实现过程默认选择65537
>
> e.用拓展欧几里得算法计算e对于φ(n)的模反元素d



# （2） 数据加密、数字签名

> a. 加密要用公钥 (n,e)
>
> M**e≡c(modn)
>
> b.    签名用私钥 (n,e)
>
> C**d≡m(modn)

