# Import module.
import subprocess


# Define function.
def f_get_git_branch():

    """
    Get git branch name.

    Parameters
    ----------
    -

    Returns
    -------
    str
        Git branch name.

    Testing
    -------
    """ 

    try:

        # Run the "git rev-parse --abbrev-ref HEAD" command and capture its output
        branch_name = (            
            subprocess
            .check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
            .strip()
            .decode("utf-8")
        )

        return branch_name
    
    except subprocess.CalledProcessError as e:

        # Handle the case where the command fails (e.g., not in a Git repository)
        print("Error getting current Git branch:", e)

        return None


