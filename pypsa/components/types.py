from pathlib import Path

import numpy as np
import pandas as pd

from pypsa.definitions.components import ComponentType

# TODO better path handeling, integrate custom components
_components_path = Path(__file__).parent.parent / "components.csv"
_attrs_path = Path(__file__).parent.parent / "component_attrs"

component_types_df = pd.read_csv(_components_path, index_col=0)


def load_component_types(
    component_df: pd.DataFrame, attrs_path: Path
) -> dict[str, ComponentType]:
    """
    #TODO Update docstring
    Get the default components and default component attributes.

    Either returns the passed arguments or if missing reads the default
    components and default component attributes from the PyPSA package data.

    Parameters
    ----------
    default_components : pandas.DataFrame
        Pass if they should be overridden and not be read from the package data.

    default_component_attrs : pypsa.descriptors.Dict
        Pass if they should be overridden and not be read from the package data.

    Returns
    -------
    tuple : pandas.DataFrame, pypsa.descriptors.Dict
        Default components and default component attributes.

    """

    component_dict = {}
    for c_name, row in component_df.iterrows():
        # Read in attributes
        attrs_file_path = attrs_path / f"{row.list_name}.csv"
        if not attrs_file_path.exists():
            msg = (
                f"Could not find {attrs_path}. For each component, there must be a "
                "corresponding file for its attributes."
            )
            raise FileNotFoundError(msg)
        attrs = pd.read_csv(attrs_file_path, index_col=0, na_values="n/a")

        # Format attributes
        attrs["default"] = attrs.default.astype(object)
        attrs["static"] = attrs["type"] != "series"
        attrs["varying"] = attrs["type"].isin({"series", "static or series"})
        attrs["typ"] = (
            attrs["type"]
            .map({"boolean": bool, "int": int, "string": str, "geometry": "geometry"})
            .fillna(float)
        )
        attrs["dtype"] = (
            attrs["type"]
            .map(
                {
                    "boolean": np.dtype(bool),
                    "int": np.dtype(int),
                    "string": np.dtype("O"),
                }
            )
            .fillna(np.dtype(float))
        )

        bool_b = attrs.type == "boolean"
        if bool_b.any():
            attrs.loc[bool_b, "default"] = attrs.loc[bool_b, "default"].isin(
                {True, "True"}
            )

        # exclude Network because it's not in a DF and has non-typical attributes
        if c_name != "Network":
            str_b = attrs.typ.apply(lambda x: x is str)
            attrs.loc[str_b, "default"] = attrs.loc[str_b, "default"].fillna("")
            for typ in (str, float, int):
                typ_b = attrs.typ == typ
                attrs.loc[typ_b, "default"] = attrs.loc[typ_b, "default"].astype(typ)

        # Initialize Component
        component_dict[c_name] = ComponentType(
            name=c_name,
            list_name=row.list_name,
            description=row.description,
            category=row.category,
            defaults=attrs,  # TODO: rename all
        )
    return component_dict


_all_types = load_component_types(
    component_df=component_types_df, attrs_path=_attrs_path
)


def get_component_type(name: str) -> ComponentType:
    return _all_types[name]


# Add generated objects to the module globals
globals().update(_all_types)

__all__ = list(_all_types.keys())
