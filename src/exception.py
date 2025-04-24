import sys 

def error_message_detail(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    error_message = ("The error happends on python script ({0}) at line ({1}) and the detail is ({2})".format(
        exc_tb.tb_frame.f_code.co_filename, exc_tb.tb_lineno, str(error)
    ))

    return error_message

class CustomException(Exception):
    def __init__(self, error, error_message, error_details:sys):
        super.__init__(error_message)
        self.error_message = error_message_detail(error=error, error_details=error_details)

    def __str__(self):
        return self.error_message