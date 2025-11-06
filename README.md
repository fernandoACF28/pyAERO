# pyAERO

pyAERO are useful package for download aeronet datas.

Some vars from AERONET stations?

| Data Types  | Explanation |
| --- | --- |
| AOD10  | Aerosol Optical Depth Level 1.0 |
| AOD15  | Aerosol Optical Depth Level 1.5 |
| AOD20  | Aerosol Optical Depth Level 2.0 |
| SDA10  | SDA Retrieval Level 1.0 |
| SDA15  | SDA Retrieval Level 1.5 |
| SDA20  | SDA Retrieval Level 2.0 |
| TOT10  | Total Optical Depth based on AOD Level 1.0 (all points only) |
| TOT15  | Total Optical Depth based on AOD Level 1.5 (all points only) |
| TOT20  | Total Optical Depth based on AOD Level 2.0 (all points only) |
| LWN10  | Normalized Water Leaving Radiances Level 1.0 |
| LWN15  | Normalized Water Leaving Radiances Level 1.5 |
| LWN20 (not yet available)  | Normalized Water Leaving Radiances Level 2.0 |
| ZEN00  | Raw Zenith Sky Scan Radiance |
| ALM00  | Raw Almucantar Sky Scan Radiance |
| HYB00  | Raw Hybrid Sky Scan Radiance |
| PPL00  | Raw Principal Plane Sky Scan Radiance |
| PPP00  | Raw Polarized Principal Plane Sky Scan Radiance and Degree of Polarization |
| ALP00  | Raw Polarized Almucantar Sky Scan Radiance and Degree of Polarization |
| HYP00  | Raw Polarized Hybrid Sky Scan Radiance and Degree of Polarization |

Here are some vars like asymetry factor radiative forcing and others.

Inversion types:

| [inv_type] Values | Explanation |
| --- | --- |
| ALM15  | Level 1.5 Almucantar Retrievals |
| ALM20  | Level 2.0 Almucantar Retrievals |
| HYB15  | Level 1.5 Hybrid Retrievals |
| HYB20  | Level 2.0 Hybrid Retrievals |

Here are explanation of vars, its necessary use the ***inversion type*** for choise any var bellow:

| Data Types | Explanation |
| --- | --- |
| SIZ  | Size distribution |
| RIN  | Refractive indicies (real and imaginary) |
| CAD  | Coincident AOT data with almucantar retrieval |
| VOL  | Volume concentration, volume mean radius, effective radius and standard deviation |
| TAB  | AOT absorption |
| AOD  | AOT extinction |
| SSA  | Single scattering albedo |
| ASY  | Asymmetry factor |
| FRC  | Radiative Forcing |
| LID  | Lidar and Depolarization Ratios |
| FLX  | Spectral flux |
| ALL  | All of the above retrievals (SIZ to FLUX) in one file |
| PFN  | Phase function (available for only all points data format: AVG=10) |
| U27  | Estimation of Sensitivity to 27 Input Uncertainty Variations (available for only all points data format: AVG=10 and ALM20 and HYB20) |
