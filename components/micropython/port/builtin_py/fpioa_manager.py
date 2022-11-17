from board import board_info
from Maix import FPIOA
class Fpioa_Manager:
    def __init__(self):
        self.board_dict={}
        self.fpioa_dict={}
        self.fpioa = FPIOA()
        self.board_info = board_info
    def register(self,pin = None,function = None, force = True):
        if pin is None or function is None:
            print("Please enter Pin and function")
            return -1
        find_pin,find_func = self.find_dict(pin,function)
        if (find_pin is not None or find_func is not None) and not force:
            return find_pin,find_func
        self.board_dict[pin] = function
        self.fpioa_dict[function] = pin
        self.fpioa.set_function(pin,function)
        return 1
    def unregister(self,pin = None,function = None):
        if pin is None and function is None:
            print("Please enter Pin and function")
            return -1
        find_pin,find_func = self.find_dict(pin,function)
        if find_pin != None or find_func != None:
            ret_func=self.board_dict.pop(find_pin)
            ret_pin=self.fpioa_dict.pop(find_func)
            return ret_pin,ret_func
        else:
            print("This function and pin have not been registered yet")
            return 0
    def find_dict(self,pin,function):
        bd_pin,bd_func = self.__find_board_dict(pin)
        fp_pin,fp_func = self.__find_fpioa_dict(function)
        if bd_pin != None or bd_func != None:
            return bd_pin,bd_func
        elif fp_pin != None or fp_func != None:
            return fp_pin,fp_func
        else:
            return None,None
    def __find_board_dict(self,pin):
        if pin is None:
            return None,None
        function = self.board_dict.get(pin)
        return (None, None) if function is None else (pin, self.board_dict[pin])
    def __find_fpioa_dict(self,function):
        if function is None:
            return None,None
        pin = self.fpioa_dict.get(function)
        return (None, None) if pin is None else (self.fpioa_dict[function], function)

global fm
fm=Fpioa_Manager()

