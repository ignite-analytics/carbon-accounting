## Table of contents

- [About Exiobase](#about-exiobase)
- [Ignite version of Exiobase](#ignite-version-of-exiobase)
  - [Motivation for altering the database](#motivation-for-altering-the-database)
  - [Changes](#changes)
  - [Outlier adjustment](#outlier-adjustment)
  - [Regional averages](#regional-averages)
  - [Column description](#column-description)

## About Exiobase

There are different sources of emission factors, usually from statistical bureaus, scientific studies or industry clusters. The UK Department for Business, Energy & Industrial Strategy (DEFRA) releases yearly [emission factors](https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2022) that are widely used, especially for activity-based calculations. Additionally, the German climate-API company Climatiq has a [data explorer](https://www.climatiq.io/explorer) where a large portion of open source emission factors are collected in one place.

What we assume based on our experience is the most used database for spend-based emission factors, however, is Exiobase 3, where emission factors is one of several different dimensions of available data. On their [website](https://www.exiobase.eu/index.php/about-exiobase), they describe Exiobase as follows:

> EXIOBASE is a global, detailed Multi-Regional Environmentally Extended Supply-Use Table (MR-SUT) and Input-Output Table (MR-IOT). It was developed by harmonizing and detailing supply-use tables for a large number of countries, estimating emissions and resource extractions by industry. Subsequently the country supply-use tables were linked via trade creating an MR-SUT and producing a MR-IOTs from this. The MR-IOT that can be used for the analysis of the environmental impacts associated with the final consumption of product groups.
>
> EXIOBASE was developed by a consortium of several research institutes in projects financed by the European research framework programs. Three version of EXIOBASE are available.

There are two versions of Exiobase, an industry- and a product-version. Both covers 44 countries and 5 rest of the world regions (more or less overlapping with continents). While the industry version covers 163 industries, the product version is expanded to 200 categories of products and services. Data is available for the years 1995-2022, and the full raw dataset of the newest version of Exiobase (3.8.2) is available [online](https://zenodo.org/record/5589597#.Ymfh8NNBweZ).

## Ignite version of Exiobase

Some reformatting of the data is necessary to use Exiobase as there are no plain files with the spend-based emission factors readily available. The most important part is this is to extract and format the emission factors that are stored in the M.txt files for each of the industry/product versions and each year.

In Exiobase, emission factors using GWP100 numbers from both AR4 and AR5 are available, and the current Ignite version of Exiobase as found in the [EUR_Exiobase3_8_2 Ignite v1_1](EUR_Exiobase3_8_2-Ignite1_1-Products_2010-2022.xlsx) excel file, use the AR5 values. In a future version, GWP100 values for AR6 will be used instead, but that requires much more reformatting of the database.

Ignite uses the product version of exiobase (the pxp folders), for the years 2010-2022. The columns used from the M.txt files are the following:

- `GHG emissions AR5 (GWP100) | GWP100 (IPCC, 2010)`
- `Water Consumption Blue - Total`
- `Land use Crop, Forest, Pasture`

And all can be found in the emission factor file in this repository.

### Motivation for altering the database

Unfortunately, there are several outliers in the dataset as a result of sparse statistical data in certain combinations of regions and categories. These combinations of a region and category will rarely be used, but can still have a huge impact on the final result. Therefore, Ignite has created its own version of Exiobase where outliers are adjusted and blank values filled with estimates based on the other available data. Also, it is practical to have a category to put the tail-spend into that cannot easily be classified anywhere else, that still represents the average emission from a specific region and year. This is the reason why regional (weighted) averages have been added to the Ignite version.

### Changes

As mentioned in the paragraph above, the current two changes to the Exiobase database are the adjustments of outliers and additions of regional averages. Both of these are described in more detail below.

#### Outlier adjustment

The most important outliers to adjust are the extremely large numbers, in some cases 6-8 orders of magnitude above the average emission factors. However, we also want to adjust the outliers that are too small and too large, without being extreme. Also, we want to add values to the combinations of product/service and region that originally in Exiobase is set to 0.

This is all solved by using two sets of limits. One global set of upper and lower limit for all emission factors within a specified year, using the 3- and 97-percentiles (without considering the 0-values). A local set of limits are also found for each emission factor category within that year, using 5- and 95-percentiles. Then a set of conditions are checked to adjust values within the local and global limits. If a value is more extreme than the global limits, it is adjusted to the corresponding limit. The same for the local limits, if they are within the global ones. Here, there's also a check for negative values as there are around 10 of them for the whole database. 0-values are also adjusted in this step to the lower limit (global if the local is lower than the global). In the next iteration of the Ignite version of Exiobase, the 0-values will most likely be set to a weighted average within that category, instead of using the lower limit for 0-values to give a better represenation of that category.

#### Regional averages

It is important to be able to estimate also the tail-spend that might not be possible to classify anywhere else without an effort much higher than the potential gain for that effort. It would be possible to just create an average of all the emission factors, either divided by year, region, or both. However, this would potentially give too much weight to high emission factors from smaller categories by size. Therefore, a weighted average has been applied to each region per year, weighted by the relative sizes of each industry in that region for that year as defined by the x.txt files. In a future version, the use-tables will likely be used instead of the x.txt files for an increased accuracy on the weighted sizes of each product and service category.

### Column description

Here follows a description of the columns in the Ignite version of Exiobase as seen in the [EUR_Exiobase3_8_2 Ignite v1_1](EUR_Exiobase3_8_2-Ignite1_1-Products_2010-2022.xlsx) excel file:

- `EF Category L1` An added layer of categorization to distinguish products from regional averages and spend that should be exempt
- `EF Category L2` The 200 products and services as defined by Exiobase
- `EF Region` The 49 regions as defined by Exiobase
- `EF Year` The year as defined by Exiobase
- `EF Currency` The currency (EUR here, but we have versions for USD and NOK as well)
- `EF Source` The Exiobase version (and Ignite update as described in this repository)
- `EF Unique String` A text field combining the L1 and L2 of the Exiobase category, the Exiobase region, and the year
- `Adjusted by Ignite` A boolean field showing whether the emission factor has been adjusted/added or not when compared with the original Exiobase values
- `EF IPCC AR5 [kg CO2e/€]` Corresponding to the original Exiobase values (except for the regional averages)
- `Water Consumption [m3/€]` Corresponding to the original Exiobase values (except for the regional averages)
- `Land Use [m2/€]` Corresponding to the original Exiobase values (except for the regional averages)
- `Emission Factor [kg CO2e/€]` The emission factor values used in Ignite to calculate emissions from spend
