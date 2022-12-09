# Ignite Procurement: Carbon Accounting 
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

A public github repository describing the carbon accounting methodology of Ignite Procurement, as well as our version of the spend-based emission factors available in the Exiobase database. As we want our greenhouse gas estimates to be both as transparent and accurate as possible, any and all feedback is very welcome, either in the [Discussions](https://github.com/ignite-analytics/carbon-accounting/discussions) tab on this repository or by email to [mathias.backsaether@ignite.no](mathias.backsaether@ignite.no). Note that this is a work in progress, and that changes will occur over time.

## Table of contents
* [License](#license)
* [Introduction to Ignite Procurement](#introduction-to-ignite-procurement)
* [Carbon accounting basics](#carbon-accounting-basics)
 * [Some general challenges with emission factors](#some-general-challenges-with-emission-factors)
* [About Exiobase](#about-exiobase)
* [Ignite version of Exiobase](#ignite-version-of-exiobase)
  * [Motivation for altering the database](#motivation-for-altering-the-database)
  * [Changes](#changes)
   * [Outlier adjustment](#outlier-adjustment)
   * [Regional averages](#regional-averages)
  * [Column description](#column-description)
* [Ignite carbon accounting methodology](#ignite-carbon-accounting-methodology)
  * [Step 1: Create heatmap](#step-create-heatmap)
  * [Step 2: Select activities](#step-select-activities)
  * [Step 3: Supplier specifics](#step-supplier-specifics)

## License

As the [Exiobase 3 database](https://zenodo.org/record/5589597#.Ymfh8NNBweZ) is [licensed](https://www.exiobase.eu/index.php/terms-of-use) with a [Creative Commons Attribution-ShareAlike 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/), and we in Ignite Procurement have made changes to the original data to adjust outliers and add regional (weighted) averages, this work is shared with the same [license](LICENCE.md):

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

## Introduction to Ignite Procurement
Ignite Procurement (or simply Ignite) is a Norwegian SaaS-company with more than 50 employees located across two offices, one in Oslo, Norway and the other in Warsaw, Poland. Ignite provides a web-based application for consolidation and analysis of data, applied for work with strategic procurement. The last couple of years, Ignite has expanded its functionality to include contract management and an assessment module that can be used internally and externally towards your suppliers. As we aim to *empower companies around the world to make smarter and more **responsible** procurement decisions*, Ignite see the potential to contribute with carbon accounting based on procurement data as a small step in the direction of the 1.5 degree target as defined at COP21 in Paris, 2015. 

More information can be found on our website: [igniteprocurement.com](https://www.igniteprocurement.com/)

## Carbon accounting basics

To be able to measure reductions in emissions, and even set reduction targets for that matter, you need to calculate the emissions you are responsible for, either as a person, coorporation or nation. In this setting, it is the calculation of emissions that coorporations are responsible for that is in focus, and the gold standard for this is the Greenhouse Gas Protocol (GHGP) [Corporate Standard](https://ghgprotocol.org/corporate-standard). It was expanded in 2011 with the [Corporate Value Chain (Scope 3) Standard](https://ghgprotocol.org/standards/scope-3-standard), which includes detailed descriptions and examples for calculations in all the categories of indirect emissions not directly controlled by a coorporation. Emissions are by the GHGP defined as three scopes: 1, 2 and 3. Scope 1 includes the direct emissions from a company's own direct emissions of greenhouse gases to the air. Scope 2 is defined as the indirect emissions from a company's use of electricity, heating and cooling. All other emissions that a company is indirectly responsible for are placed within the 15 different categories of scope 3, as seen by the image below[^ghgp-scopes]. 

![image](https://user-images.githubusercontent.com/88656160/204288151-31f47d11-5b0c-47ce-8bdb-4761215f99ee.png)

> Note that there are other frameworks defining carbon accounting practices for coorporations such as [ISO-14064-1](https://www.iso.org/standard/66453.html), [GRI 305](https://www.globalreporting.org/standards/media/1012/gri-305-emissions-2016.pdf), [CDP](https://www.cdp.net/en), and [PCAF](https://carbonaccountingfinancials.com/standard#the-global-ghg-accounting-and-reporting-standard-for-the-financial-industry). However, all of them are based on the GHGP, often with specified clarifications or additions for certain categories of the GHGP standard.

Common for allmost all greenhouse gas emission calculations is that
* You should include all 7 greenhouse gases as defined by the (updated) Kyoto protocol, usually presented as carbon dioxide equivalents (CO<sub>2</sub>e)
  * Standard conversion rates between the different gases are included in the IPCC reports (AR6 being the latest). The latest available should be selected, using the global warming potential of 100 years (GWP100)
* The calculation it self usually encapsulate some amount of something (e.g. the emissions from burning 100L of diesel) times the best fitting emission factor that is available (e.g. 2.70 kg CO<sub>2</sub>e per L diesel)
  * The selected emission factor should be as specific as possible, optimally including matching the spatial (e.g. country), temporal (e.g. year), and technological (e.g. specific process) dimentions.
  
Emission factors are oftentimes diveded into two categories, spend-based (where the amount is a monetary one, e.g. 1.2 kg CO<sub>2</sub>e/€) and activity-based (where the amount is anything else, for instance kg, L, km, person-night etc.)

[^ghgp-scopes]: [Greenhouse Gas Protocol: Corporate Value Chain (Scope 3) Accounting and Reporting Standard, Introduction chapter, Figure 1.1](https://ghgprotocol.org/sites/default/files/standards/Corporate-Value-Chain-Accounting-Reporing-Standard-EReader_041613_0.pdf)

### Some general challenges with emission factors
`Note that this section was provided by the OpenAI chat GPT language model and fact checked by Ignite`

Some of the challenges with using emission factors include:

* Ensuring the quality and relevance of the emission factors: Emission factors can vary depending on the source, location, and activity, so it is important to use the most appropriate and up-to-date factors for your specific situation.

* Accounting for variability and uncertainty: Emission factors are typically based on averages or estimations, and there can be significant variability and uncertainty in the emissions from different activities. This can make it difficult to accurately estimate emissions, especially for complex or unique situations.

* Handling temporal and spatial variations: Emissions can vary over time and space, depending on factors such as weather, technology, and market conditions. This can make it challenging to apply emission factors consistently and accurately across different time periods and locations.

* Dealing with missing or incomplete data: In many cases, there may be gaps in the data or information needed to estimate emissions using emission factors. This can make it difficult to account for all relevant emissions and can introduce errors or uncertainty into the estimates.

* Incorporating emissions from indirect or downstream activities: Many emissions, especially in the scope 3 category, are indirect or occur downstream from the activity being considered. These emissions can be difficult to quantify and account for using emission factors.

* Addressing changes in activity levels or emissions intensity: Over time, the emissions intensity (emissions per unit of activity) of different activities can change due to factors such as technological improvements, policy changes, and market conditions. This can make it challenging to apply emission factors consistently and accurately over the long term.

* Considering emissions from multiple gases: Emissions from different activities can involve multiple greenhouse gases, each with its own unique characteristics and impacts. This can make it difficult to compare and combine emissions from different sources and activities using a single emission factor.

These are some of the challenges that can arise when using emission factors to estimate greenhouse gas emissions. It is important to carefully consider these challenges and address them in an appropriate and transparent manner when using emission factors in GHG accounting and reporting.

## About Exiobase
There are different sources of emission factors, usually from statistical bureaus, scientific studies or industry clusters. The UK Department for Business, Energy & Industrial Strategy (DEFRA) releases yearly [emission factors](https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2022) that are widely used, especially for activity-based calculations. Additionally, the German climate-API company Climatiq has a [data explorer](https://www.climatiq.io/explorer) where a large portion of open source emission factors are collected in one place. 

What we assume based on our experience is the most used database for spend-based emission factors, however, is Exiobase 3, where emission factors is one of several different dimensions of available data. On their [website](https://www.exiobase.eu/index.php/about-exiobase), they describe Exiobase as follows:

> EXIOBASE is a global, detailed Multi-Regional Environmentally Extended Supply-Use  Table (MR-SUT) and Input-Output Table (MR-IOT). It was developed by harmonizing and detailing supply-use tables for a large number of countries, estimating emissions and resource extractions by industry. Subsequently the country supply-use tables were linked via trade  creating an MR-SUT and producing a MR-IOTs from this. The MR-IOT that can be used for the analysis of the environmental impacts associated with the final consumption of product groups.
>
> EXIOBASE was developed by a consortium of several research institutes in projects financed by the European research framework programs. Three version of EXIOBASE are available.


There are two versions of Exiobase, an industry- and a product-version. Both covers 44 countries and 5 rest of the world regions (more or less overlapping with continents). While the industry version covers 163 industries, the product version is expanded to 200 categories of products and services. Data is available for the years 1995-2022, and the full raw dataset of the newest version of Exiobase (3.8.2) is available [online](https://zenodo.org/record/5589597#.Ymfh8NNBweZ).

## Ignite version of Exiobase
Some reformatting of the data is necessary to use Exiobase as there are no plain files with the spend-based emission factors readily available. The most important part is this is to extract and format the emission factors that are stored in the M.txt files for each of the industry/product versions and each year. 

In Exiobase, emission factors using GWP100 numbers from both AR4 and AR5 are available, and the current Ignite version of Exiobase as found in the [EUR_Exiobase3_8_2 Ignite v1_1](EUR_Exiobase3_8_2-Ignite1_1-Products_2010-2022.xlsx) excel file, use the AR5 values. In a future version, GWP100 values for AR6 will be used instead, but that requires much more reformatting of the database.

Ignite uses the product version of exiobase (the pxp folders), for the years 2010-2022. The columns used from the M.txt files are the following:
* `GHG emissions AR5 (GWP100) | GWP100 (IPCC, 2010)`
* `Water Consumption Blue - Total`
* `Land use Crop, Forest, Pasture`

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
* `EF Category L1` An added layer of categorization to distinguish products from regional averages and spend that should be exempt
* `EF Category L2` The 200 products and services as defined by Exiobase
* `EF Region` The 49 regions as defined by Exiobase 
* `EF Year` The year as defined by Exiobase 
* `EF Currency` The currency (EUR here, but we have versions for USD and NOK as well)
* `EF Source` The Exiobase version (and Ignite update as described in this repository)
* `EF Unique String` A text field combining the L1 and L2 of the Exiobase category, the Exiobase region, and the year
* `Adjusted by Ignite` A boolean field showing whether the emission factor has been adjusted/added or not when compared with the original Exiobase values
* `EF IPCC AR5 [kg CO2e/€]` Corresponding to the original Exiobase values (except for the regional averages)
* `Water Consumption [m3/€]` Corresponding to the original Exiobase values (except for the regional averages)
* `Land Use [m2/€]` Corresponding to the original Exiobase values (except for the regional averages)
* `Emission Factor [kg CO2e/€]` The emission factor values used in Ignite to calculate emissions from spend

## Ignite carbon accounting methodology
Ignite follows a 3-step approach to scope 3 carbon accounting:
1. Start by covering as many categories (both scope 3 categories and spend categories when based on procurement data) to create initial estimates that enables insights into where to focus further efforts.
2. Drill down into the categories of interest where more effort should be used to increase the accuracy, for instance by switching from a spend-based to an activity-based calculation.
3. Contact the most essential suppliers within targeted categories to approach supplier specific calculation. This is necessary to be able to directly compare two different suppliers within the same industry or products within the same product/service category.

![image](https://user-images.githubusercontent.com/88656160/204540717-3844d08e-604b-449a-9af9-49bc5b2e939c.png)

### Step 1: Create heatmap

What Ignite provides out of the box and which can be set up within a day of having access to a company's procurement data is the initial match of every single purchase with a spend-based Exiobase emission factor. For mapping a purchase by its year, this is usually pretty straight forward, the most challenging decission is what date to chose if more are avilable. We try to use the year from the transaction date where possible, but invoice date can also be used, and if the company has fiscal years defined in their data, that information is used to match up the calculations with their financial reporting. Matching with an Exiobase region is usually also relatively simple, as most companies have supplier country as a field in their procurement data, where we have standard rulesets going from the different spellings of countries, as well as Alpha-2 codes, into the 49 Exiobase regions. The third part of matching with an emission factor, matching each transaction with an Exiobase product/service category is the most challenging one, and is usually done in multiple iteration with increasing accuracies. The first iteration of this process utilize supplier industry information from 3rd-party databases like Enin and Infobel, where all NACE and SIC industry codes on the lowest level have been matched to Exiobase as standard rulesets. Everything that is not categorized by this method at this stage will be put into the regional average bucket, where only the supplier region and purchase year will decide the emission factor. The next iteration involves creating rules from more accuract information like GL account, product description or spend categorization, depending on what is available. In some cases it will be possible to map all spend by a high-accuracy dimention such as by a product master. If this is the case, then this should be strived for. However, note that it is the most important categories (when accounting for spend size, emissions size and how vital the category is for the company) that should be prioritized in this iterative work towards more accurate calculations. 

![image](https://user-images.githubusercontent.com/88656160/204540792-8ecec762-a6d2-4c98-98ff-736653e1bd63.png)

### Step 2: Select activities

![image](https://user-images.githubusercontent.com/88656160/204543215-604eec5c-6444-402c-b2c4-ab0f6879c023.png)


### Step 3: Supplier specifics

![image](https://user-images.githubusercontent.com/88656160/204543274-40515d15-3727-40b0-9e5d-9d34d225aae4.png)



