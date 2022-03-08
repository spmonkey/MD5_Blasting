import threading
from hashlib import md5
from itertools import permutations
from string import ascii_letters, digits, ascii_lowercase, ascii_uppercase
from time import time

all_letters = ascii_lowercase + '.,;@' + digits
class MDfive:
    def __init__(self):
        self.__mdfive = 0

    def md5_poj(self, md5_value, k):
        if len(md5_value) != 32:
            print("error")
            return
        md5_value = md5_value.lower()
        # permutations() 全排列
        for item in permutations(all_letters, k):
            item = "".join(item)
            if md5(item.encode()).hexdigest() == md5_value:
                print('\n success: ' + md5_value + ' ==> ' + item)
                self.__mdfive = 1

    def main(self):
        # NT_md5 = 'e00cf25ad42683b3df678c61f42c6bda'
        NT_md5 = input("请填写MD5：")
        start_time = time()
        t_list = []
        print("正在查询...")
        # 添加线程
        for k in range(5, 18):
            t = threading.Thread(target=self.md5_poj, args=(NT_md5, k))
            t.daemon = 1    # 守护程序
            t_list.append(t)
        # 启动所有线程
        for i in t_list:
            i.start()
        # 当 __mdfive == 1 时结束所有线程
        while 1:
            if self.__mdfive:
                break
        print("\n查询结束!")
        print('time used: {0}'.format(time() - start_time))

if __name__ == '__main__':
    MDfive().main()






