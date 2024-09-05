# SPDX-FileCopyrightText: 2024 https://github.com/bobbyxng
#
# SPDX-License-Identifier: MIT


##################
# Initialisation #
##################

import os

# Dictionary containing all needed symbolic link paths and target directories
symlinks = {
    "data": "submodules/pypsa-eur-resilient/data",
    # Add more symlinks as needed
}
# Define a function to create symlinks if they do not exist
def create_symlinks():
    for link_name, target_dir in symlinks.items():
        if not os.path.exists(link_name):
            os.symlink(target_dir, link_name)
            print(f"Created symlink: {link_name} -> {target_dir}")


# Initialisation that creates needed symlinks to submodules
rule init:
    output:
        directory("data")
    run:
        create_symlinks()


####################
# Submodule import #
####################

# Define the configuration file
configfile: "submodules/pypsa-eur-resilient/config/config.default.yaml"

# Include the Snakemake workflow from the submodule
module resilient:
    snakefile:
        "submodules/pypsa-eur-resilient/Snakefile"
    config:
        config

# Use all rules from the resilient module
use rule * from resilient


####################
# Additional rules #
####################


