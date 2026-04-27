import os

def generate_code(plan, project_name):
    os.makedirs(project_name, exist_ok=True)

    # Example file (you will later replace this with AI-generated files)
    with open(f"{project_name}/main.py", "w") as f:
        f.write("# Generated code\nprint('Hello from AI agent')")
