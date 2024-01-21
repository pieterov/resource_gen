# Import module.
import re

from .f_is_numerical import f_is_numerical

# Define function.
def f_clean_up_header_names(l_input):

    """
    Clean up header names of data frame: (1) set names to lower case, and (2) replace spaces by '_'.

    Parameters
    ----------
    l_input : list
        Column names.


    Returns
    -------
    list
        Cleaned up column names.
    """
    

    return [
        # Put in lower case:
        x3.lower() for x3 in [

        # Replace space by '_':
        x2 if f_is_numerical(x2) else re.sub(" |\.", "_", x2) for x2 in [

        str(x1) for x1 in l_input        
    ]]]
