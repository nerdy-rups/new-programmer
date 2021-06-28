import logging

def test_logging(): # as with any pytest testcase, the whole thing needs to be put inside a function
    myLogger = logging.getLogger(__name__) # magic method inside getLogger class

    RGFileHandler = logging.FileHandler("logfile.log") # filehandler type object created which defines what is the name and extension of the file to be generated
    RGFileFormatter = logging.Formatter("%(levelname)s : %(asctime)s : %(name)s : %(message)s")
    """Above: another object that defines in what format the logs will be printed. The values in parentheses are keywords and % sign is used to 
     denote that they will be evaluated at runtime. "s" denotes that each value should be converted to string format."""

    RGFileHandler.setFormatter(RGFileFormatter) # Binding the file formatter object to the filehandler, which in turn contains what is the file to be created

    myLogger.addHandler(RGFileHandler) # Finally, logger object knows what file to generate and how to put the data into it

    myLogger.setLevel(logging.WARNING) # Optional. Can be defined to say, what is the minimum level of log type need to be printed. Values always in Caps.

    myLogger.debug("This is debug level log 1")
    myLogger.info("This is information level log 1")
    myLogger.warning("This is warning level log 1")
    myLogger.error("This is error level log 1")
    myLogger.debug("This is debug level log 2")
    myLogger.info("This is information level log 2")
    myLogger.critical("This is critical level log 1")
    myLogger.debug("This is debug level log 3")
    myLogger.info("This is information level log 3")
    myLogger.debug("This is debug level log 4")
    myLogger.info("This is information level log 4")


    # Default logging level heirarchy: debug<info<warning<error<critical
    # The generated log file gets updated with new rows with each run of the testcase.
