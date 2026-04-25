import sys
from networksecurity.logging.logger import logger

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details):
        self.error_message=error_message

        _,_, exc_tb=error_details.exc_info()

        self.file_name=exc_tb.tb_frame.f_code.co_filename
        # self.lineno=exc_tb.tb_frame.f_code.co_filename
        self.lineno=exc_tb.tb_lineno

    def __str__(self):
        return "Error occured in python script name [{}] line number [{}] error message [{}]".format(
            self.file_name, 
            self.lineno, 
            self.error_message
            )

if __name__=="__main__":
    try:
        logger.info("Enter the try block")
        a=1/0
        print("this will not be printed ",a)

    except Exception as e:
        logger.error("Exception occured")
        raise NetworkSecurityException(e,sys)