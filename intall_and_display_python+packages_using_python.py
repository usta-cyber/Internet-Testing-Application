import subprocess

# List of packages to install
packages = ['numpy', 'pandas', 'matplotlib']

# Install each package using pip
for package in packages:
    subprocess.call(['pip', 'install', package])

import pkg_resources

# Get a list of installed packages
installed_packages = [d for d in pkg_resources.working_set]

print("Installed Packages:-")
i=1
# Display the list of installed packages
for package in installed_packages:
    print("\t",i," :- ",package.project_name)
    i=i+1
