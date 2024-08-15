class phone:
    __is_5g_enable=True
    
    def __check_5g(self):
        if self.__is_5g_enable==True:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")
            
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")
        
Phone=phone()
Phone.call_by_5g()   