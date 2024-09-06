# RESILIENT: Decision under uncertainty using regret-matrix approach 

This repository contains the data sources and code for reproducing the workflow. The philosophy behind this repository is that no intermediary results are included, but all results are computed from raw data and code.


## Clone the repository

To start you need to clone the repository. Since the repository relies on git submodules ([pypsa-eur-resilient](https://github.com/resilient-project/pypsa-eur-resilient), you need to include the `--recurse-submodules` flag in your `git clone` command:

`git clone --recurse-submodules https://github.com/bobbyxng/resilient-regret-matrix.git`


## Initialisation

When running the workflow for the first time, please run in this order:

* `conda env create -f workflow/envs/environment.yaml` to create the environment and installing dependencies
* `conda activate resilient-regret-matrix` to activate the environment


## About RESILIENT

The energy transition faces many uncertainties, but planning tools are often deterministic. Our proposal will develop the first truly multi-vector energy infrastructure planning tool that represents this uncertain environment, both at a regional and national as well as the European level. We will build on the existing widely-used, open-source, sector-coupled energy planning tool for Europe, PyPSA-Eur, and add stochastic optimisation capabilities as well as a deeper representation of industry transformation, e-fuel conversion, biomass and carbon capture infrastructure. We will look at uncertainties that include the cost of fuels and technologies, hydrogen availability, network expansion delays for electricity, hydrogen and carbon dioxide, value chain restructuring in industry, imports of e-fuels and secondary materials, renewables build-out and social acceptance. We will examine novel computational techniques to address stochastic problems in a performant way. For this proposal, we have assembled a team of leading academic researchers and need-owners from industry who are at the cutting edge of energy system modelling. We will demonstrate the capabilities of our planning tool in several case studies for resilient infrastructure planning, together with our need-owners in France, Germany, Sweden and Finland. We plan several workshops and training events with a broader circle of need owners and stakeholders to ensure a wide uptake of our innovative project results.

[Project website](https://resilient-project.github.io)
