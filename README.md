# Ignite Procurement: Carbon Accounting

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

A public github repository describing the carbon accounting methodology of Ignite Procurement, as well as our version of the spend-based emission factors available in the Exiobase database. As we want our greenhouse gas estimates to be both as transparent and accurate as possible, any and all feedback is very welcome, either in the [Discussions](https://github.com/ignite-analytics/carbon-accounting/discussions) tab on this repository or by email to [mathias.backsaether@ignite.no](mathias.backsaether@ignite.no). Note that this is a work in progress, and that changes will occur over time, described in the [changelog](CHANGELOG.md) document.

## Table of contents

- [License](#license)
- [Introduction to Ignite Procurement](#introduction-to-ignite-procurement)
- [Carbon accounting basics](#carbon-accounting-basics)
  - [General challenges](#general-challenges)
- [Other files](#other-files)

## License

As the [Exiobase 3 database](https://zenodo.org/record/5589597#.Ymfh8NNBweZ) is [licensed](https://www.exiobase.eu/index.php/terms-of-use) with a [Creative Commons Attribution-ShareAlike 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/), and we in Ignite Procurement have made changes to the original data to adjust outliers and add regional (weighted) averages, this work is shared with the same [license](LICENCE.md):

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

## Introduction to Ignite Procurement

Ignite Procurement (or simply Ignite) is a Norwegian SaaS-company with more than 50 employees located across two offices, one in Oslo, Norway and the other in Warsaw, Poland. Ignite provides a web-based application for consolidation and analysis of data, applied for work with strategic procurement. The last couple of years, Ignite has expanded its functionality to include contract management and an assessment module that can be used internally and externally towards your suppliers. As we aim to _empower companies around the world to make smarter and more **responsible** procurement decisions_, Ignite see the potential to contribute with carbon accounting based on procurement data as a small step in the direction of the 1.5 degree target as defined at COP21 in Paris, 2015.

More information can be found on our website: [igniteprocurement.com](https://www.igniteprocurement.com/)

## Carbon accounting basics

To be able to measure reductions in emissions, and even set reduction targets for that matter, you need to calculate the emissions you are responsible for, either as a person, corporation or nation. In this setting, it is the calculation of emissions that corporations are responsible for that is in focus, and the gold standard for this is the Greenhouse Gas Protocol (GHGP) [Corporate Standard](https://ghgprotocol.org/corporate-standard). It was expanded in 2011 with the [Corporate Value Chain (Scope 3) Standard](https://ghgprotocol.org/standards/scope-3-standard), which includes detailed descriptions and examples for calculations in all the categories of indirect emissions not directly controlled by a corporation. Emissions are by the GHGP defined within three scopes: 1, 2 and 3. Scope 1 includes the direct emissions from a company's own operations, for instance company-owned internal combustion vehicles. Scope 2 is defined as the indirect emissions from a company's use of electricity, heating and cooling. All other emissions that a company is indirectly responsible for are placed within the 15 different categories of scope 3, as seen by the image below[^ghgp-scopes].

![image](https://user-images.githubusercontent.com/88656160/204288151-31f47d11-5b0c-47ce-8bdb-4761215f99ee.png)

> Note that there are other frameworks defining carbon accounting practices for corporations such as [ISO-14064-1](https://www.iso.org/standard/66453.html), [GRI 305](https://www.globalreporting.org/standards/media/1012/gri-305-emissions-2016.pdf), [CDP](https://www.cdp.net/en), and [PCAF](https://carbonaccountingfinancials.com/standard#the-global-ghg-accounting-and-reporting-standard-for-the-financial-industry). However, all of them are based on the GHGP, often with specified clarifications or additions for certain categories of the GHGP standard.

In carbon accounting, there are two quantification methods, direct measurements using physics and chemistry, and calculations. The first method is much more accurate, but also much more challenging in that physical measurements of the involved operations are needed. Especially for indirect emissions, calculations are used almost without exception. Common for almost all greenhouse gas emission calculations is that

- You should include all 7 greenhouse gases as defined by the (updated) Kyoto protocol, usually presented as carbon dioxide equivalents (CO<sub>2</sub>e)
  - Standard conversion rates between the different gases are included in the IPCC reports (AR6 being the latest). The latest available should be selected, using the global warming potential of 100 years (GWP100)
- The calculation itself usually encapsulate some amount of an activity (e.g. the emissions from burning 100L of diesel) times the best fitting emission factor that is available (e.g. 2.70 kg CO<sub>2</sub>e per L diesel)
  - The selected emission factor should be as specific as possible, optimally including matching the spatial (e.g. country/region), temporal (e.g. year), and technological (e.g. specific process) dimensions.

Emission factors are oftentimes divided into two categories, spend-based (where the amount is a monetary one, e.g. 1.2 kg CO<sub>2</sub>e/€) and activity-based (where the amount is anything else, for instance kg, L, km, and hours).

[^ghgp-scopes]: [Greenhouse Gas Protocol: Corporate Value Chain (Scope 3) Accounting and Reporting Standard, Introduction chapter, Figure 1.1](https://ghgprotocol.org/sites/default/files/standards/Corporate-Value-Chain-Accounting-Reporing-Standard-EReader_041613_0.pdf)

### General challenges

As almost all carbon accounting is calculated (as compared to direct measurements, especially for indirect emissions), it is important to acknowledge some of the general challenges with these kinds of calculations. This list includes some of the general challenges to keep in mind:

- Ensuring the quality and relevance of the emission factors: Emission factors can vary depending on the source, location, and activity, so it is important to use the most appropriate and up-to-date factors for your specific situation.

- Accounting for variability and uncertainty: Emission factors are typically based on averages or estimations, and there can be significant variability and uncertainty in the emissions from different activities. This can make it difficult to accurately estimate emissions, especially for complex or unique situations.

- Handling temporal and spatial variations: Emissions can vary over time and space, depending on factors such as weather, technology, and market conditions. This can make it challenging to apply emission factors consistently and accurately across different time periods and locations.

- Dealing with missing or incomplete data: In many cases, there may be gaps in the data or information needed to estimate emissions using emission factors. This can make it difficult to account for all relevant emissions and can introduce errors or uncertainty into the estimates.

- Incorporating emissions from indirect or downstream activities: Many emissions, especially in the scope 3 category, are indirect or occur downstream from the activity being considered. These emissions can be difficult to quantify and account for using emission factors.

- Addressing changes in activity levels or emissions intensity: Over time, the emissions intensity (emissions per unit of activity) of different activities can change due to factors such as technological improvements, policy changes, and market conditions. This can make it challenging to apply emission factors consistently and accurately over the long term.

- Considering emissions from multiple gases: Emissions from different activities can involve multiple greenhouse gases, each with its own unique characteristics and impacts. This can make it difficult to compare and combine emissions from different sources and activities using a single emission factor.

It is important to carefully consider these challenges and address them in an appropriate and transparent manner when using emission factors in GHG accounting and reporting.

## Other Files

An explanation of the Exiobase database, as well as how Ignite has updated it to adjust outliers and blank values, can be found in [exiobase-emission-factors/EXIOBASE.md](exiobase-emission-factors/EXIOBASE.md).

The Ignite carbon accounting methodology is described in [methodology/METHODOLOGY.md](methodology/METHODOLOGY.md). It is built on the [Greenhouse Gas Protocol](https://ghgprotocol.org/), and can be used for reporting according to [GRI](https://www.globalreporting.org/) and [CDP](https://www.cdp.net/) as well.
