# Ignite Procurement: Carbon Accounting

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

A public github repository describing the carbon accounting methodology of Ignite, as well as our version of the spend-based emission factors available in the Exiobase database. As we want our greenhouse gas estimates to be both as transparent and accurate as possible, any and all feedback is very welcome, either in the [Discussions](https://github.com/ignite-analytics/carbon-accounting/discussions) tab on this repository or by email to [mathias.backsaether@ignite.no](mathias.backsaether@ignite.no). Note that this is a work in progress, and that changes will occur over time, described in the [changelog](CHANGELOG.md) document.

## Table of contents

- [License](#license)
- [Introduction to Ignite Procurement](#introduction-to-ignite-procurement)
- [About the document](#about-the-document)
- [Carbon accounting basics](#carbon-accounting-basics)
  - [The use of spend to estimate emissions](#the-use-of-spend-to-calculate-emissions)
- [Other files](#other-files)

## License

As the [Exiobase 3 database](https://zenodo.org/record/5589597#.Ymfh8NNBweZ) is [licensed](https://www.exiobase.eu/index.php/terms-of-use) with a [Creative Commons Attribution-ShareAlike 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/), and we in Ignite Procurement have made changes to the original data to adjust outliers and add regional (weighted) averages, this work is shared with the same [license](LICENCE.md):

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

## Introduction to Ignite Procurement

Ignite is a Norwegian SaaS company with more than 50 employees. We provide a web-based application for the consolidation and analysis of data, applied for work with strategic procurement. Through the last couple of years, Ignite has expanded its functionality to now include procurement analytics, carbon accounting, contract management, and supplier risk management that can be used together or separately. As we aim to empower companies around the world to make smarter and more responsible procurement decisions, Ignite sees the potential to contribute with carbon accounting as a small step in the direction limiting emissions in line with the 1.5-degree target.

More information can be found on our website: [ignite.no](https://www.ignite.no/)

## About the document

This document aims to provide a thorough description of our carbon accounting methodology, which is used both for calculating our own emissions, as well as those of our customers. It can be shared with, and referred to by any auditors of companies using the Ignite software for their carbon accounting.

## Carbon accounting basics

To be able to measure reductions in emissions, and even set reduction targets for that matter, you need to calculate the emissions you are responsible for, either as a person, corporation or nation. In this setting, it is the calculation of emissions that corporations are responsible for that is in focus, and the gold standard for this is the Greenhouse Gas Protocol (GHGP) [Corporate Standard](https://ghgprotocol.org/corporate-standard). It was expanded in 2011 with the [Corporate Value Chain (Scope 3) Standard](https://ghgprotocol.org/standards/scope-3-standard), which includes detailed descriptions and examples for calculations in all the categories of indirect emissions not directly controlled by a corporation. Emissions are by the GHGP defined within three scopes: 1, 2 and 3. Scope 1 includes the direct emissions from a company's own operations, for instance company-owned internal combustion vehicles. Scope 2 is defined as the indirect emissions from a company's use of electricity, heating and cooling. All other emissions that a company is indirectly responsible for are placed within the 15 different categories of scope 3, as seen by the image below.

![image](https://user-images.githubusercontent.com/88656160/204288151-31f47d11-5b0c-47ce-8bdb-4761215f99ee.png)

> All images on this page is from the [Greenhouse Gas Protocol: Corporate Value Chain (Scope 3) Accounting and Reporting Standard](https://ghgprotocol.org/sites/default/files/standards/Corporate-Value-Chain-Accounting-Reporing-Standard-EReader_041613_0.pdf)

In carbon accounting, there are two quantification methods: direct measurements using physics or chemistry, and calculations. The first method is much more accurate, but also much more challenging to conduct. Especially for indirect emissions, calculations are used almost without exception. Common for almost all greenhouse gas emission calculations is that

- You should optimally include all 7 greenhouse gases as defined by the (updated) Kyoto protocol, usually presented as carbon dioxide equivalents (CO₂e)
  - Standard conversion rates between the different gases are included in the IPCC reports (AR6 being the latest). The latest available should be selected, using the global warming potential of 100 years (GWP100)
- The calculation itself usually encapsulate some amount of an activity (e.g. the emissions from burning 100 liters of diesel) times the best fitting emission factor that is available (e.g. 2.70 kg CO₂e per liter diesel)
  - The selected emission factor should be as specific as possible, optimally including matching the spatial (e.g. country/region), temporal (e.g. year), and technological (e.g. specific process) dimensions.

Emission factors are oftentimes divided into two categories, spend-based (where the amount is a monetary one, e.g. 1.2 kg CO₂e/€) and activity-based (where the amount is anything else, for instance kg, L, km, and hours).

As almost all carbon accounting is calculated, it is important to acknowledge some of the general challenges with these kinds of calculations. This list includes some of these to keep in mind:

- Ensuring the quality and relevance of the emission factors: Emission factors can vary depending on the source, location, and activity, so it is important to use the most appropriate and up-to-date factors for your specific situation.
- Accounting for variability and uncertainty: Emission factors are typically based on averages or estimations, and there can be significant variability and uncertainty in the emissions from different activities. This can make it difficult to accurately estimate emissions, especially for complex or unique situations.
- Handling temporal and spatial variations: Emissions can vary over time and space, depending on factors such as weather, technology, and market conditions. This can make it challenging to apply emission factors consistently and accurately across different time periods and locations.
- Dealing with missing or incomplete data: In many cases, there may be gaps in the data or information needed to estimate emissions using emission factors. This can make it difficult to account for all relevant emissions and can introduce errors or uncertainty into the estimates.
- Addressing changes in activity levels or emissions intensity: Over time, the emissions intensity (emissions per unit of activity) of different activities can change due to factors such as technological improvements, policy changes, and market conditions. This can make it challenging to apply emission factors consistently and accurately over the long term.
- Considering emissions from all the GHGs: Even though you should use emission factors that take into account all the 7 categories of greenhouse gases, very few emission factors currently available do so.

Where there might be ambiguities in calculation and reporting of corporate GHG emissions, the GHGP has defined five principles for implementation guidance:

- Relevance: Ensure the GHG inventory appropriately reflects the GHG emissions of the company and serves the decision-making needs of users – both internal and external to the company.
- Completeness: Account for and report on all GHG emission sources and activities within the inventory boundary. Disclose and justify any specific exclusions.
- Consistency: Use consistent methodologies to allow for meaningful performance tracking of emissions over time. Transparently document any changes to the data, inventory boundary, methods, or any other relevant factors in the time series.
- Transparency: Address all relevant issues in a factual and coherent manner, based on a clear audit trail. Disclose any relevant assumptions and make appropriate references to the accounting and calculation methodologies and data sources used.
- Accuracy: Ensure that the quantification of GHG emissions is systematically neither over nor under actual emissions, as far as can be judged, and that uncertainties are reduced as far as practicable. Achieve sufficient accuracy to enable users to make decisions with reasonable confidence as to the integrity of the reported information.

In practice, companies may encounter tradeoffs between principles when completing a scope 3 inventory. For example, a company may find that achieving the most complete scope 3 inventory requires using less accurate data, compromising overall accuracy. Conversely, achieving the most accurate scope 3 inventory may require excluding activities with low accuracy, compromising overall completeness.

### The use of spend to calculate emissions

Quite a lot of the indirect emissions covered by the upstream categories of scope 3 can usually be estimated using information on how much money has been spend on different kinds of goods or services. This is called a spend-based method by the GHG Protocol, described in the scope 3 calculation guidance from 2013. From the excerpt below, each of the calculation methods for scope 3 category 1: purchased goods and services, is described.

The GHG Protocol scope 3 calculation guidance also gives a visual explanation of each of the calculation methods and to what degree data for the supplier’s scope 1, 2 and 3 is specific to that supplier or based on average data.

Figure 1.2 from the calculation guidance as seen below provides a decision tree for which calculation method should be used for scope 3 category 1. There’s also an option to use what the GHG Protocol calls a combination of calculation methods, where parts of this category is calculated using one method, while other parts might use other methods, depending on data availability and prioritisation.

Other parts of the upstream scope 3 emissions can also be covered by spend data:

- Category 2: capital good
  - Calculated in the same way as category 1, just distinguished by what is considered capital goods in financial reporting.
- Category 3: fuel and energy-related activities
  - This category includes the cradle-to-gate emissions (often called well-to-tank for fuels) of purchased fuels and electricity, as well as the transportation and distribution losses of purchased electricity. The GHG Protocol scope 3 calculation guidance does not mention spend as a source for calculating this category, so using spend for this category is mainly relevant for screening purposes in the cases where activity data is not available. As Exiobase does include spend-based emission factors for cradle-to-gate emissions for a range of fuels, with regional distinguishment, this can be used with care.
- Category 4: transportation and distribution
  - In the cases where the organisation pays for this separately, transportation and distribution will definitively be covered by procurement data. If not fuel amount or distances are available, then a spend-based approach can be used. Note that this category covers both inbound and outbound logistics, as long as the reporting corporation pays for the service. Also note that this category includes the transportation and distribution between a company’s tier-1 suppliers and themselves, but not between their tier-1 and tier-n suppliers (earlier in the supply chain).
- Category 5: waste generated in operations
  - Waste is partly covered by spend-data as most organisations pay for this, but an activity-based method where the quantities and types of waste are combined with information about how the waste is handled, will give much more accurate results. Note that a spend-based approach is not listed in the GHGP scope 3 calculation guidance for category 5, so it should optimally only be used for screening purposes. However, a spend-based method was used in the now discontinued [GHGP/Quantis calculation tool](https://quantis-suite.com/Scope-3-Evaluator/), so it has some merit to it as long as care is taken with the resulting numbers as the uncertainty is high.
- Category 6: business travel
  - Business travel is certainly covered as this is something companies pay for, and it is specifically mentioned in the calculation guidance. However, travel expenses are oftentimes bulked into joint invoices from travel agencies where it is hard to say how much is used on what part of the travel. Below is the suggested decision tree from the GHG Protocol.

There are some solutions providers that also estimate scope 1 and 2 emissions from information on spending within categories such as fuel and energy. As this is not mentioned as a valid approach in the GHG Protocol, and there are large uncertainties connected with going from spend to activity amounts within these categories as prices have a tendency to fluctuate, we have decided to only accept activity amounts (liters, kWh, etc), not spend amounts, to estimate scope 1 and 2 emissions.

> Note that there are other frameworks defining carbon accounting practices for corporations such as [ISO-14064-1](https://www.iso.org/standard/66453.html), [ESRS](https://eur-lex.europa.eu/legal-content/en/TXT/?uri=CELEX:32023R2772), [GRI 305](https://www.globalreporting.org/standards/media/1012/gri-305-emissions-2016.pdf), [CDP](https://www.cdp.net/en), and [PCAF](https://carbonaccountingfinancials.com/standard#the-global-ghg-accounting-and-reporting-standard-for-the-financial-industry). However, all of them are either based on the GHG Protocol or interchangable, but sometimes with specified clarifications or additions for certain categories of emissions.

## Other Files

The Ignite carbon accounting methodology is described in [METHODOLOGY.md](methodology/METHODOLOGY.md). It is built on the [Greenhouse Gas Protocol](https://ghgprotocol.org/), and can be used for reporting frameworks such as [GRI](https://www.globalreporting.org/), [CDP](https://www.cdp.net/), and the reporting requirements for gross scope 1, 2, and 3 emissions from the [ESRS E1-6](https://eur-lex.europa.eu/legal-content/en/TXT/?uri=CELEX:32023R2772).

An explanation of the Exiobase database, as well as how Ignite has updated it to adjust outliers and blank values, can be found in [EXIOBASE.md](emission-factors/exiobase/IGNITE_VERSION_OF_EXIOBASE.md).
