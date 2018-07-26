Status
=======

[![Build Status](https://travis-ci.org/hschovanec-usgs/finite-fault-product.svg?branch=master)](https://travis-ci.org/hschovanec-usgs/finite-fault-product)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/81d612b63c864f3fb894f4e5bec90b49)](https://www.codacy.com/app/hschovanec-usgs/finite-fault-product?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=hschovanec-usgs/finite-fault-product&amp;utm_campaign=Badge_Grade)

[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/81d612b63c864f3fb894f4e5bec90b49)](https://www.codacy.com/app/hschovanec-usgs/finite-fault-product?utm_source=github.com&utm_medium=referral&utm_content=hschovanec-usgs/finite-fault-product&utm_campaign=Badge_Coverage)

[![Waffle.io - Columns and their card count](https://badge.waffle.io/hschovanec-usgs/finite-fault-product.svg?columns=all)](https://waffle.io/hschovanec-usgs/finite-fault-product)


# finite-fault-product

Load finite fault data and create products.

## fault
Designed to analyze finite fault models and time series.
* `fault.py` Class to analyze fault models.

### fault.io
fault.io is designed to read finite fault data from fsp, dat, and syn files.

 * `fsp.py` Load rupture model.
 * `timeseries.py` Load data and synthetic seismograms.

## product
product is designed to create eventpages and ShakeMap products.
* `web_product.py` Create web product from time series and fault data. (Under construction)
* `pdl.py` Contains methods for sending products to pdl.
* `shakemap_product.py` Create shakemap product from time series and fault data. (Unavailable)

## sendproduct
Includes functionality to send a finite fault product.

usage: sendproduct [-h] [-ffm2 FFM2] [-v COMMENT] [-r] net eventid ffm1

Send a finite fault product for event pages.

<table>
  <tr>
    <th colspan="2">Positional arguments</th>
  </tr>
  <tr>
    <td>net</td>
    <td>Network code (example: us)</td>
  </tr>
  <tr>
    <td>eventid</td>
    <td>Event identification code</td>
  </tr>
  <tr>
    <td>ffm1</td>
    <td>Directory where all files are contained for the finite fault model</td>
  </tr>
</table>

<table>
  <tr>
    <th colspan="2">Optional arguments</th>
  </tr>
  <tr>
    <td>-h, --help</td>
    <td>Show the help message and exit</td>
  </tr>
  <tr>
    <td>-ffm2 FFM2</td>
    <td>Directory where all files are contained for the second finite fault model</td>
  </tr>
  <tr>
    <td>-v COMMENT, --version COMMENT</td>
    <td>Add a version number to the finite fault output</td>
  </tr>
  <tr>
    <td>-r, --review</td>
    <td>Create product, but do not send to PDL</td>
  </tr>
</table>

See [docs](https://github.com/hschovanec-usgs/finite-fault-product/tree/master/docs) for more detailed explanations.
