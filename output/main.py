from agents.planner import plan_project
from agents.coder import generate_code
from agents.packager import zip_project
from agents.github_agent import push_to_github
import os

PROJECT_NAME = "generated_project"

idea = "Build a FastAPI app that analyzes Terraform code"

# Step 1: Plan
plan = plan_project(idea)
print("PLAN:\n", plan)

# Step 2: Generate code
project_path = f"output/{PROJECT_NAME}"
generate_code(plan, project_path)

# Step 3: Zip
zip_path = zip_project(project_path)
print("ZIP created:", zip_path)

# Step 4: Push to GitHub
push_to_github(project_path)
