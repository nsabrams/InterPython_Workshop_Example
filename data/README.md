# Data Readme

The 'data' directory contains two files:
- `kepler_RRLyr.csv`. This catalog contains 93487 Kepler observations of a single RR Lyrae variable star in a single band. The catalogue
  includes 'time', 'flux' and 'flux_err' columns for visualizing the light curve, and a number of other columns, which full description
  can be found at https://exoplanetarchive.ipac.caltech.edu/docs/KeplerMission.html
- `lsst_RRLyr.pkl`. This catalogue contains 11177 LSST Data Preview 0 records of various variable star candidates. The records are in
  the six `ugrizy` bands. The columns of this catalogue are:
    - 'band':         str, contains information of the band of the observation
    - 'ccdVisitId':   int64, id of the visit
    - 'coord_ra':     float, ra
    - 'coord_dec':    float, dec
    - 'objectId':     int64, object id
    - 'psfFlux':      float, flux
    - 'psfFluxErr':   float, flux error
    - 'psfMag':       float, magnitude
    - 'ccdVisitId2'   int62, id of the second visit in the pair
    - 'band2'         str, band of the second visit in the pair
    - 'expMidptMJD':  float, mjd observation timestamp in days
    - 'zeroPoint':    float, zero point

  The purpose of these two datasets is to serve as model catalogues for the development and testing the lcanalyzer functionality.
