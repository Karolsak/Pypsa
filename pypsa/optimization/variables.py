#!/usr/bin/env python3
"""
Define optimisation variables from PyPSA networks with Linopy.
"""

from __future__ import annotations

import logging
from collections.abc import Sequence
from typing import TYPE_CHECKING

from pypsa.descriptors import get_activity_mask
from pypsa.descriptors import get_switchable_as_dense as get_as_dense

if TYPE_CHECKING:
    from pypsa import Network

logger = logging.getLogger(__name__)


def define_operational_variables(n: Network, sns: Sequence, c: str, attr: str) -> None:
    """
    Initializes variables for power dispatch for a given component and a given
    attribute.

    Parameters
    ----------
    n : pypsa.Network
    c : str
        name of the network component
    attr : str
        name of the attribute, e.g. 'p'
    """
    if n.df(c).empty:
        return

    active = get_activity_mask(n, c, sns) if n._multi_invest else None
    coords = [sns, n.df(c).index.rename(c)]
    n.model.add_variables(coords=coords, name=f"{c}-{attr}", mask=active)


def define_committability_variables(n: Network, sns: Sequence, c: str) -> None:
    """
    Initializes integer variables  related to committability for all committable components. Initialized variables are:
    - status
    - start-up
    - shut down

    Parameters
    ----------
    n : pypsa.Network
    sns : pd.Index
        Snapshots of the constraint.
    c : str
        network component of which the committability variables should be defined
    """
    com_i = n.get_committable_i(c)

    if com_i.empty:
        return

    active = get_activity_mask(n, c, sns, com_i) if n._multi_invest else None
    coords = (sns, com_i)
    is_integer = not n._linearized_uc

    n.model.add_variables(
        lower=0, coords=coords, name=f"{c}-status", mask=active, integer=is_integer
    )

    n.model.add_variables(
        lower=0, coords=coords, name=f"{c}-start_up", mask=active, integer=is_integer
    )

    n.model.add_variables(
        lower=0, coords=coords, name=f"{c}-shut_down", mask=active, integer=is_integer
    )


def define_nominal_variables(n: Network, c: str, attr: str) -> None:
    """
    Initializes variables for nominal capacities for a given component and a
    given attribute.

    Parameters
    ----------
    n : pypsa.Network
    c : str
        network component of which the nominal capacity should be defined
    attr : str
        name of the variable, e.g. 'p_nom'
    """
    ext_i = n.get_extendable_i(c)
    if ext_i.empty:
        return

    n.model.add_variables(coords=[ext_i], name=f"{c}-{attr}")


def define_modular_variables(n: Network, c: str, attr: str) -> None:
    """
    Initializes variables 'attr' for a given component c to allow a modular
    expansion of the attribute 'attr_nom' It allows to define 'n_opt', the
    optimal number of installed modules.

    Parameters
    ----------
    n : pypsa.Network
    c : str
        network component of which the nominal capacity should be defined
    attr : str
        name of the variable to be handled attached to modular constraints, e.g. 'p_nom'
    """
    mod_i = n.df(c).query(f"{attr}_extendable and ({attr}_mod>0)").index
    mod_i = mod_i.rename(f"{c}-ext")

    if (mod_i).empty:
        return

    n.model.add_variables(lower=0, coords=[mod_i], name=f"{c}-n_mod", integer=True)


def define_spillage_variables(n: Network, sns: Sequence) -> None:
    """
    Defines the spillage variables for storage units.
    """
    c = "StorageUnit"
    if n.df(c).empty:
        return

    upper = get_as_dense(n, c, "inflow", sns)
    if (upper.max() <= 0).all():
        return

    active = get_activity_mask(n, c, sns).where(upper > 0, False)
    n.model.add_variables(0, upper, name="StorageUnit-spill", mask=active)


def define_loss_variables(n: Network, sns: Sequence, c: str) -> None:
    """
    Initializes variables for transmission losses.
    """
    if n.df(c).empty or c not in n.passive_branch_components:
        return

    active = get_activity_mask(n, c, sns) if n._multi_invest else None
    coords = [sns, n.df(c).index.rename(c)]
    n.model.add_variables(0, coords=coords, name=f"{c}-loss", mask=active)
