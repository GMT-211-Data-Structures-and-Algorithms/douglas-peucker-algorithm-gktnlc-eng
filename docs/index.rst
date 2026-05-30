GMT211 Douglas-Peucker Algorithm
=================================

A Python implementation of the Douglas-Peucker line simplification algorithm.

Installation
------------

.. code-block:: bash

   pip install -i https://test.pypi.org/simple/ gmt211-2230674042

Usage
-----

.. code-block:: python

   from dp import *

   input_file = 'antalya.geojson'
   out_file = 'out.geojson'
   epsilon = 0.01

   execute_douglas_peucker(input_file, out_file, epsilon)