import logging

def get_logger(name="default_logger", log_level=logging.INFO):
    """
    Creates and configures a logger that can be used as a substitute for the print function.

    Parameters:
    - name (str): The name of the logger (default is 'default_logger').
    - log_level (int): The logging level (default is logging.INFO).

    Returns:
    - logger (logging.Logger): Configured logger instance.
    """
    # Create a logger with the specified name
    logger = logging.getLogger(name)
    
    # Set the logging level
    logger.setLevel(log_level)
    
    # Create a stream handler (outputs to console)
    handler = logging.StreamHandler()
    
    # Define the format for log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Attach the formatter to the handler
    handler.setFormatter(formatter)
    
    # Ensure the logger does not add duplicate handlers
    if not logger.handlers:
        logger.addHandler(handler)
    
    return logger
