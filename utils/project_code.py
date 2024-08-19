import os

# Specify the directory to start from and the output file
# Assuming you want to fetch code from the project root
start_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
output_file = os.path.join(start_dir, 'project_code.txt')

# File extensions to include as code
code_extensions = ['.py', '.html', '.css', '.js', '.txt']

def is_code_file(file_name):
    return any(file_name.endswith(ext) for ext in code_extensions)

def fetch_code_from_project(start_dir, output_file):
    with open(output_file, 'w') as outfile:
        for root, dirs, files in os.walk(start_dir):
            # Skip the __pycache__ directory
            if '__pycache__' in dirs:
                dirs.remove('__pycache__')
            for file in files:
                if is_code_file(file):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(f"\n\n# Contents of {file_path}\n")
                        outfile.write(infile.read())
                        outfile.write("\n" + "#" * 80 + "\n")

# Execute the function
fetch_code_from_project(start_dir, output_file)

print(f"All code has been written to {output_file}")