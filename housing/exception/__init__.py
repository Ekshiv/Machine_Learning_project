import os
import sys

class HousingException(Exception):
    
    #sys is used for the details of where at what file, at what line error occured in program
    #we are creating our custom error msg and sending it to Exception class
    
    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(error_message)
        self.error_message=HousingException.get_detailed_error_message(error_message=error_message, error_detail=error_detail )


    #static method is used so that we dont need any object to call this function
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)->str:
        
        """Error_msg: Exception object
        Error_detail: Object of sys module"""

        _,_ ,exec_tb = error_detail.exc_info()     #we are taking only 3rd value of exc_info(type, value, traceback)
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message =  f"Error Occured in script: [{file_name}] at line number: [{line_number}] error message: [{error_message}] "

        return error_message

    def __str__(self):
        return self.error_message
    
    def __repr__(self)-> str:
        return HousingException.__name__.str()