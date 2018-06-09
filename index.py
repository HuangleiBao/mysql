from model.admit import Admit

def main():
    use = input("username:")
    pwd = input("password:")
    admit=Admit()
    result = admit.Checkdata(use,pwd)
    if not result :
        print("登陆失败！")
    else:
        print("登陆成功！进入后台操作界面")
if __name__ == '__main__':
     main()