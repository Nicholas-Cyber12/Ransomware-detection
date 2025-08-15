import os

def get_files_snapshot(folder):
    """Return a list of filenames in folder"""
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
