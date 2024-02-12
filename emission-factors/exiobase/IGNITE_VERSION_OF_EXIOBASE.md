## Table of contents

- [About Exiobase](#about-exiobase)
- [Ignite version of Exiobase](#ignite-version-of-exiobase)
  - [Motivation for updating the database](#motivation-for-updating-the-database)
  - [Outlier adjustment](#outlier-adjustment)
  - [Regional averages](#regional-averages)
  - [Yearly values](#yearly-values)
  - [Column description](#column-description)

## About Exiobase

The most commonly used databases for spend-based emission factors according to the PCAF Financed Emissions standard are [Exiobase](https://www.exiobase.eu/), the Global Trade Analysis Project ([GTAP](https://www.gtap.agecon.purdue.edu)), and the World Input-Output Database ([WIOD](http://www.wiod.org)). Because of its extended coverage in both emission categories, regions and years, we have decided to use Exiobase 3.8.2. This is also the database most other carbon accounting software providers use, which is good for comparability. On their [website](https://www.exiobase.eu/index.php/about-exiobase), they describe Exiobase as follows:

> EXIOBASE is a global, detailed Multi-Regional Environmentally Extended Supply-Use Table (MR-SUT) and Input-Output Table (MR-IOT). It was developed by harmonizing and detailing supply-use tables for a large number of countries, estimating emissions and resource extractions by industry. Subsequently the country supply-use tables were linked via trade creating an MR-SUT and producing a MR-IOTs from this. The MR-IOT that can be used for the analysis of the environmental impacts associated with the final consumption of product groups.
>
> EXIOBASE was developed by a consortium of several research institutes in projects financed by the European research framework programs. Three version of EXIOBASE are available.

There are two versions of Exiobase, an industry- and a product-version. Both covers 44 countries and 5 rest of the world regions (more or less overlapping with continents). While the industry version covers 163 industries, the product version is expanded to 200 categories of products and services. Data is available for the years 1995-2022, and the full raw dataset of the newest version of Exiobase (3.8.2) is available [online](https://zenodo.org/record/5589597#.Ymfh8NNBweZ).

## Ignite version of Exiobase

Some reformatting of the data is necessary to use Exiobase as there are no plain files with the spend-based emission factors readily available. The most important part is this is to extract and format the emission factors that are stored in the M.txt files for each of the industry/product versions and each year.

In Exiobase, emission factors using GWP100 numbers from both AR4 and AR5 are available, and the current Ignite version of Exiobase as found in the [EUR_Exiobase3_8_2 Ignite v1_1](https://github.com/ignite-analytics/carbon-accounting/blob/main/emission-factors/exiobase/EUR_Exiobase3_8_2-Ignite1_1-Products_2010-2022.xlsx) excel file, use the AR5 values. In a future version, GWP100 values for AR6 will be used instead, but that requires much more reformatting of the database.

Ignite uses the product version of exiobase (the pxp folders), for the years 2010-2022. The columns used from the M.txt files are the following:

- `GHG emissions AR5 (GWP100) | GWP100 (IPCC, 2010)`
- `Water Consumption Blue - Total`
- `Land use Crop, Forest, Pasture`

And all can be found in the emission factor file in this repository. As no new version of Exiobase has been released that includes values for 2023, we use the 2022 values also for 2023 estimates.

### Motivation for updating the database

Unfortunately, there are several outliers in the dataset as a result of sparse statistical data in certain combinations of regions and categories. These combinations of a region and category will rarely be used, but can still have a huge impact on the final result. Therefore, Ignite has created its own version of Exiobase where outliers are adjusted and blank values filled with estimates based on the other available data. Also, it is practical to have a category to put the tail-spend into that cannot easily be classified anywhere else, that still represents the average emission from a specific region and year. This is the reason why regional (weighted) averages have been added to the Ignite version.

### Outlier adjustment

The most important outliers to adjust are the extremely large numbers, in some cases 6-8 orders of magnitude above the average emission factors. However, we also want to adjust the outliers that are too small and too large, without being extreme. Also, we want to add values to the combinations of product/service and region that originally in Exiobase is set to 0.

This is all solved by using two sets of limits. One global set of upper and lower limit for all emission factors within a specified year, using the 3- and 97-percentiles (without considering the 0-values). A local set of limits are also found for each emission factor category within that year, using 5- and 95-percentiles. Then a set of conditions are checked to adjust values within the local and global limits. If a value is more extreme than the global limits, it is adjusted to the corresponding limit. The same for the local limits, if they are within the global ones. Here, there's also a check for negative values as there are around 10 of them for the whole database. 0-values are also adjusted in this step to the lower limit (global if the local is lower than the global). In the next iteration of the Ignite version of Exiobase, the 0-values will most likely be set to a weighted average within that category, instead of using the lower limit for 0-values to give a better representation of that category.

### Regional averages

It is important to be able to estimate also the tail-spend that might not be possible to classify anywhere else without an effort much higher than the potential gain for that effort. It would be possible to just create an average of all the emission factors, either divided by year, region, or both. However, this would potentially give too much weight to high emission factors from smaller categories by size. Therefore, a weighted average has been applied to each region per year, weighted by the relative sizes of each industry in that region for that year as defined by the x.txt files. In a future version, the use-tables will likely be used instead of the x.txt files for an increased accuracy on the weighted sizes of each product and service category.

### Yearly values

There are different ways of solving how to calculate emissions over time. One of the data quality indicators defined by the GHG Protocol is _temporal representativeness,_ defined as “The degree to which the data set reflects the actual time (e.g. year) or age of the activity”. This indicator is also very relevant for the selection of emission factors, as changes happens from year to year, that have an impact on both direct and indirect emissions.

In some categories, it makes sense to use the most up-to-date emission factors for all calculations in that category, and potentially re-calculate activities back in time to provide a good comparison over time. These categories are especially linked to scientific progress on the effects of different greenhouse gases, for instance the Global Warming Potential (GWP) defined by the International Panel for Climate Change (IPCC). When the GWP values are updated as a result of new and improved scientific insights, then the newest values should be used.

However, in most cases, there are good arguments for selecting yearly emission factors that represent the actual emissions for certain activities to the highest accuracy possible for each year. A good example is electricity consumption, where the indirect emissions for 1 kWh within the same grid can change form year to year based on the composition of electricity production in that grid. Other cases include the indirect effect of purchased goods and services, transportation and most other scope 3 categories, as changes to emission intensities in production and transportation have an effect on the average emissions for those kinds of products or services. When getting to the most specific estimates for emissions on a product-level for a specific supplier (e.g. EPDs or other Life Cycle Analysis information), then it is also very relevant to have as good temporary representativeness as possible (i.e. as close to the actual emissions for that specific product in that specific time period).

For emission factors from BEIS/DEFRA (a set of emission factors for estimating UK corporate emissions) and AIB (electricity consumption emission factors for Europe), we use yearly emission factors and select the closest year possible if no values for the specified year is available. For Exiobase, we have also decided to use yearly emission factors. This is mainly driven by the fact that this, at least to some degree, represent changes in macro-economic systems and improvements to average industry emissions for different goods and services over time. Because the Exiobase 3.8.2 database has values from 1995 to 2022, we have used those values. However, the uncertainty in changes from year to year is high, and much of the data is now-casted where statistical data is not available for the most recent years (the most recent CO2-values are for instance from 2019). An alternative approach would be to only use the emission factors from 2019 and then handle estimation of inflation, currency, and potentially industry changes ourselves, but that would in our eyes reduce comparability with other users of the Exiobase database. Because most companies are now (as of Q1 2024) working with their 2023 GHG emission inventories, we have used the 2022 Exiobase emission factors also for 2023. To use the closest emission factor in time when there are none available for the year in question is a typical practice, which we also use for other categories. However, as the Exiobase database presents its values in Euros, and many of our customers have data in other currencies such as GBP, USD, NOK and SEK, we do a yearly currency conversion on when using the Exiobase emission factors. Both of these things combined, using the 2022 values for 2023, and handling currency exchange with yearly averages, results in all 2023 values becoming shifted either up or down with the same percentage as compared with 2022, when using a currency other than Euro. This does to some degree make sense as spending the same amount on the same goods or service from year to year results in different amounts of that goods or service as a result of changing prices, and thus also changed emissions. However, it also introduces a general change in estimates that is important to take into account when looking at year-over-year changes from 2022 to 2023, as some of that change will then purely be based on currency conversion, and might be misleading. The conclusion is that it is important to be aware of this effect, and that it should be an important reminder that spend-based estimates are inherently limited when it comes to accuracy, and especially when it comes to looking at comparativeness of changes to emissions over time. Surely a motivational factor for changing out spend-based estimates with average data, the hybrid method, or supplier-specific calculations over time.

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
