import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,_exc_tb=error_detail.exc_info # retrives information about current exception ,this returns a tuple containing exception type,exception object and the traceback object.
    file_name=_exc_tb.tb_frame.f_code.co_filename # extracts the filename where the exception occured from the traceback object.
    error_message="error occured in python script name [{0}] line number [{1}], error message [{2}]]".format() # extract filename,line number,error message
    file_name,_exc_tb.tb_lineno,str(error)
    
    return error_message
    

class customException(Exception):
    def __init__(self,error_message,error_detail:sys): # super() is a special function in python that refers to the parent class of the current class.
        super().__init__(error_message) # calls the constructor of the parent Exception class,passing the error_message as an argument # by calling super().__init__ ,you ensure that the parent class constructor is executed correctly before any additional initialization code in child class constructor
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message

#if __name__=="__main__":
    #try:
        #a=1/0
    #except Exception as e:
        #logging.info("divide by 0")
        #raise customexception(e,sys)
        