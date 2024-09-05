# Function that creates symlinks if they don't exist
def create_symlinks(link_name, target_dir):
    import os
    if not os.path.exists(link_name):
        os.symlink(target_dir, link_name)
        print(f"Created symlink: {link_name} -> {target_dir}")
