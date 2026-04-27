import shutil

def zip_project(project_name):
    zip_path = shutil.make_archive(project_name, 'zip', project_name)
    return zip_path
