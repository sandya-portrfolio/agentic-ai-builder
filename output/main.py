from agents.planner import plan_project
from agents.coder import generate_code
from agents.packager import zip_project
from agents.github_agent import push_to_github

PROJECT_NAME = "ai-devops-agent"

idea = "Build a FastAPI app that analyzes Terraform code"

plan = plan_project(idea)

generate_code(plan, PROJECT_NAME)

zip_path = zip_project(PROJECT_NAME)

push_to_github(PROJECT_NAME)

print(f"Project created and pushed: {PROJECT_NAME}")
