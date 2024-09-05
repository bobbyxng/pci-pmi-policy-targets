# SPDX-FileCopyrightText: 2024 https://github.com/bobbyxng
#
# SPDX-License-Identifier: MIT

##################
# Initialisation #
##################

import sys
sys.path.append("scripts")
from _tools import create_symlinks
create_symlinks("data", "submodules/pypsa-eur-resilient/data")


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


