import os
from datetime import datetime

def check_mobility_req():
    if os.path.exists("mobilityReq.txt"):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("mobilityReq.txt found. Generating integrationResult.txt...")
        with open("integrationResult.txt", "w") as f:
            f.write(f"Integration completed successfully at {current_time}.")
        print("PROCEED")
    else:
        print("mobilityReq.txt not found. Terminating pipeline.")
        print("TERMINATE")

if __name__ == "__main__":
    check_mobility_req()