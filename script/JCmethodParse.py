# 此脚本用于将接口文档转化为传输的JSON命令发送至客户端

def ReadJava(filePath):
    f = open(filePath)

    line = f.readline()
    while line:
        if line:
            line = line.strip()
            line = line.strip('\n')
            if line.startswith('public abstract') and line.endswith(';'):
                line = line.strip(');')
                data = line.split(' ')
                parmas = filter(filterblack, data)
                # 获取返回值
                returnlist = list(parmas)
                # 获取方法名
                methodList = returnlist[1].split('(')
                # 获取参数列表
                paramlist = returnlist.copy()
                paramlist.pop(0)

                if "(" in paramlist[0]:
                    pars = paramlist[0].split('(')
                    paramlist[0] = pars[1]

                finallist = list()
                finallist.append("command")
                finallist.append("mediaChannel")
                finallist.append(methodList[0])
                paramlist = filter(filterparms, paramlist)

                paramlistkey = list(paramlist).copy()

                key = [paramlistkey[i] for i in range(len(paramlistkey)) if i % 2 == 0]
                value = [paramlistkey[i] for i in range(len(paramlistkey)) if i % 2 == 1]
                dictionary = dict(zip(key, value))
                if dictionary:
                    finallist.append([dictionary])
                else:
                    finallist.append([])
                finallist.append(returnlist[0])
                print(finallist)
        line = f.readline()
    f.close()


def filterblack(args):
    if args is not '' and args != 'public' and args != 'abstract':
        return args


def filterparms(args):
    if args == '':
        return []
    elif "@" not in args:
        return args


ReadJava("JcCall.java")
