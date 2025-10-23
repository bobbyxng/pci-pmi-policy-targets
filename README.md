# PCI PMI policy targets

This repository contains the data sources and code for reproducing the workflow of the preprint "The role of Projects of Common Interest in reaching Europe's energy policy targets" (https://doi.org/10.48550/arXiv.2507.01860). The philosophy behind this repository is that no intermediary results are included, but all results are computed from raw data and code. A dataset of all results is provided on Zenodo (https://doi.org/10.5281/zenodo.15790592)

## Clone the repository

To start you need to clone the repository. Since the repository relies on git submodules ([pypsa-eur-resilient](https://github.com/resilient-project/pypsa-eur-resilient), you need to include the `--recurse-submodules` flag in your `git clone` command:

`git clone --recurse-submodules https://github.com/bobbyxng/pci-pmi-policy-targets.git`


## Initialisation

Before running the workflow for the first time, please run in this order:

* `conda env create -f workflow/pypsa-eur-resilient/envs/environment.yaml` to create the environment and installing dependencies
* `conda activate pypsa-eur` to activate the environment

## Run the workflow

To reproduce the workflow of the study, please run in the CI:
* `cd workflow/pypsa-eur-resilient`
* `snakemake solve_sector_networks --configfile config/pcipmi.config.yaml` (add `-n` for dry-run)

To recreate the figures of the study, please run:
* `snakemake create_paper_plots --configfile config/pcipmi.config.yaml`


## Abstract

The European Union aims to achieve climate-neutrality by 2050, with interim 2030 targets including 55% greenhouse gas emissions reduction compared to 1990 levels, 10 Mt p.a. of a domestic green H2 production, and 50 Mt p.a. of domestic CO2 injection capacity. To support these targets, Projects of Common and Mutual Interest (PCI-PMI) --- large infrastructure projects for electricity, hydrogen and CO2 transport, and storage --- have been identified by the European Commission. This study focuses on PCI-PMI projects related to hydrogen and carbon value chains, assessing their long-term system value and the impact of pipeline delays and shifting policy targets using the sector-coupled energy system model PyPSA-Eur. Our study shows that PCI-PMI projects enable a more cost-effective transition to a net-zero energy system compared to scenarios without any pipeline expansion. Hydrogen pipelines help distribute affordable green hydrogen from renewable-rich regions in the north and southwest to high-demand areas in central Europe, while CO2 pipelines link major industrial emitters with offshore storage sites. Although these projects are not essential in 2030, they begin to significantly reduce annual system costs --- by more than €26 billion --- from 2040 onward. Delaying implementation beyond 2040 could increase system costs by up to €24.2 billion per year, depending on the extent of additional infrastructure development. Moreover, our results show that PCI-PMI projects reduce the need for excess wind and solar capacity and lower reliance on individual CO2 removal technologies, such as Direct Air Capture, by 13 to 136 Mt annually, depending on the build-out scenario.

## About RESILIENT

The energy transition faces many uncertainties, but planning tools are often deterministic. Our proposal will develop the first truly multi-vector energy infrastructure planning tool that represents this uncertain environment, both at a regional and national as well as the European level. We will build on the existing widely-used, open-source, sector-coupled energy planning tool for Europe, PyPSA-Eur, and add stochastic optimisation capabilities as well as a deeper representation of industry transformation, e-fuel conversion, biomass and carbon capture infrastructure. We will look at uncertainties that include the cost of fuels and technologies, hydrogen availability, network expansion delays for electricity, hydrogen and carbon dioxide, value chain restructuring in industry, imports of e-fuels and secondary materials, renewables build-out and social acceptance. We will examine novel computational techniques to address stochastic problems in a performant way. For this proposal, we have assembled a team of leading academic researchers and need-owners from industry who are at the cutting edge of energy system modelling. We will demonstrate the capabilities of our planning tool in several case studies for resilient infrastructure planning, together with our need-owners in France, Germany, Sweden and Finland. We plan several workshops and training events with a broader circle of need owners and stakeholders to ensure a wide uptake of our innovative project results.

[Project website](https://resilient-project.github.io)


## License

There are different open licenses for different types of files in the repository. See [specifications here](.reuse/dep5).
