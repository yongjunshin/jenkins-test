#!/usr/bin/env python3

import ast
import re

def read_integration_result():
    with open('output/integrationResult.txt', 'r') as file:
        content = file.read()
    
    nodes_match = re.search(r'Integrated ROS nodes: (\[.*?\])', content)
    if nodes_match:
        nodes_list = ast.literal_eval(nodes_match.group(1))
        return nodes_list
    return []

def generate_launch_file(nodes):
    with open('JenkinsScripts/template/template_integration.launch.py', 'r') as template_file:
        template = template_file.read()
    
    node_entries = []
    for node in nodes:
        node_entries.append(f"""Node(
            package='integration',
            executable='{node}',
            name='{node}',
            parameters=[param_dir],
            output='screen')""")
    
    nodes_content = ',\n        '.join(node_entries)
    launch_content = template.format(nodes=nodes_content)
    
    with open('output/integration.launch.py', 'w') as file:
        file.write(launch_content)

def generate_setup_file(nodes):
    with open('JenkinsScripts/template/template_setup.py', 'r') as template_file:
        template = template_file.read()
    
    entry_points = [f"'{node} = integration.{node}:main'" for node in nodes]
    entry_points_content = ',\n            '.join(entry_points)
    
    setup_content = template.format(entry_points=entry_points_content)
    
    with open('output/setup.py', 'w') as file:
        file.write(setup_content)

def main():
    nodes = read_integration_result()
    generate_launch_file(nodes)
    generate_setup_file(nodes)
    print(f"Generated files: integration.launch.py and setup.py")

if __name__ == "__main__":
    main()