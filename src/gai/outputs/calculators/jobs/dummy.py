# Dummy calculator job entrypoint for testing branch protection

def run_dummy_calculator():
    """
    Simulates a high-risk calculator job. 
    Changes to this file should require strict CODEOWNER review.
    """
    print("Running dummy calculator job...")
    return True

if __name__ == "__main__":
    run_dummy_calculator()