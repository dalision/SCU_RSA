#encoding:UTF-8
#输入十进制用十六进制保存，以及文件名字：
import argparse
def save(num,filename):
    num = str(hex(num)).upper()[2:]
    with open(filename,'w') as f:
        f.write(num)
#读取文件内容到加密函数中

def readfile():
    arg = []    
    parse = argparse.ArgumentParser()
    parse.add_argument("-p",type = str ,dest='p',help= "-p 指定明文文件的位置和名称",default="p1.txt",action='append')
    parse.add_argument("-n", type = str ,dest= 'n', help = "-n 指定存放整数 n 的文件的位置和名称", default="n1.txt",action='append')
    parse.add_argument("-e",type = str ,dest= 'e', help= "-e 在数据加密时，指定存放整数 e 的文件的位置和名称",default="e1.txt",action='append')
    parse.add_argument("-d", type = str , dest='d',help = "-d 在数字签名时，指定存放整数 d 的文件的位置和名称", default="d1.txt",action='append')
    parse.add_argument("-c", type = str , dest = 'c',help = "-c 指定密文文件的位置和名称", default="c1.txt",action='append')
    args = parse.parse_args()
    arg.append(rf(args.p))
    arg.append(rf(args.n))
    arg.append(rf(args.e))
    arg.append(rf(args.d))    
    return arg

def rf(path):
    with open(path) as f:
        return int(f.read(),16)





