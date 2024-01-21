# Import module.

# Define function.
def f_is_numerical(value):

    """
    Test whether number is number.

    Parameters
    ----------
    <name> : <type>
        <short description>.
    <name> : <type>
        <short description>.

    Returns
    -------
    <type>
        <short description>.

    Testing
    -------

    """

    try:
        float(value)
        return True
    
    except ValueError:
        return False
     