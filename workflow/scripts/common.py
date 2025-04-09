import pandas as pd
import pypsa
import warnings


def sanitize_locations(n):
    if "EU" not in n.buses.index:
        n.add("Bus", "EU", x=-5.5, y=46)
        n.buses.loc["EU", "location"] = "EU"
        n.buses.loc["co2 atmosphere", "location"] = "EU"
    n.buses["x"] = n.buses.location.map(n.buses.x)
    n.buses["y"] = n.buses.location.map(n.buses.y)


def fill_missing_carriers(n):
    for c in n.iterate_components(n.one_port_components | n.branch_components):
        new_carriers = set(c.df.carrier.unique()) - set(n.carriers.index)
        if new_carriers:
            n.add("Carrier", list(new_carriers), nice_name=list(new_carriers))


def add_carrier_groups(n, config):

    groups = pd.Series(config["grouping"])
    colors = pd.Series(config["group_colors"])
    n.carriers["group"] = groups.reindex(n.carriers.index, fill_value="")
    n.carriers["group_color"] = n.carriers.group.map(colors).fillna("")

    n.carriers.drop("", inplace=True)
    # if (no_names := n.carriers.query("nice_name == ''").index).any():
    #     warnings.warn(f"Carriers {no_names} have no nice_name")
    # if (no_colors := n.carriers.query("color == ''").index).any():
    #     warnings.warn(f"Carriers {no_colors} have no color")
    if (no_groups := n.carriers.query("group == ''").index).any():
        warnings.warn(f"Carriers {no_groups} have no technology group")
    if (no_group_colors := n.carriers.query("group_color == ''").index).any():
        warnings.warn(f"Carriers {no_group_colors} have no technology group color")
    n.carriers = n.carriers.sort_values(["color"])


def import_network(path):

    n = pypsa.Network(path)
   
    sanitize_locations(n)
    add_carrier_groups(n, config)
    # fill_missing_carriers(n)


    return n

