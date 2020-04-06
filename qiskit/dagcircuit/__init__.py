# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
=======================================
DAG Circuits (:mod:`qiskit.dagcircuit`)
=======================================

.. currentmodule:: qiskit.dagcircuit

DAG Circuits
============

.. autosummary::
   :toctree: ../stubs/

   DAGCircuit
   DAGNode

Exceptions
==========

.. autosummary::
   :toctree: ../stubs/

   DAGCircuitError
"""

import qiskitc
import sys
if hasattr(qiskitc, "__qiskitc__"):
    from qiskitc import DAGCircuit
else:
    from .dagcircuit import DAGCircuit

from .dagnode import DAGNode
from .exceptions import DAGCircuitError
