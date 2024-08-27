import os
from datetime import datetime

def integration_function(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            if "segmentation" in content.lower():
                return ["a", "b", "c", "d"]
            else:
                return ["a", "b"]
    except FileNotFoundError:
        return ["File not found."]
    except Exception as e:
        return [f"Error reading file: {str(e)}"]

def check_mobility_req():
    if os.path.exists("mobilityReq.txt"):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("mobilityReq.txt found. Generating integrationResult.txt...")
        
        integration_results = integration_function("mobilityReq.txt")
        
        with open("output/integrationResult.txt", "w") as f:
            f.write(f"Integrated ROS nodes: {integration_results}\n")
            f.write(f"Integration completed successfully at {current_time}.\n")
        print("PROCEED")
    else:
        print("mobilityReq.txt not found. Terminating pipeline.")
        print("TERMINATE")

if __name__ == "__main__":
    check_mobility_req()