import os
from datetime import datetime

def integration_function(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            # Simple sentence splitting, assumes sentences end with '.', '!', or '?'
            sentences = content.split('.')
            first_sentence = sentences[0].strip()
            return first_sentence + '.' if sentences else "No content found."
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"Error reading file: {str(e)}"

def check_mobility_req():
    if os.path.exists("mobilityReq.txt"):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("mobilityReq.txt found. Generating integrationResult.txt...")
        
        integration_results = integration_function("mobilityReq.txt")
        
        with open("integrationResult.txt", "w") as f:
            f.write(f"{integration_results}\n")
            f.write(f"Integration completed successfully at {current_time}.\n")
        print("PROCEED")
    else:
        print("mobilityReq.txt not found. Terminating pipeline.")
        print("TERMINATE")

if __name__ == "__main__":
    check_mobility_req()