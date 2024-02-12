## Table of contents

- [Ignite Carbon Accounting Methodology](#ignite-carbon-accounting-methodology)
  - [Spend-based estimates](#spend-based-estimates)
  - [Improving estimates over time](#improving-estimates-over-time)
  - [Reviewing estimates](#reviewing-estimates)

## Ignite carbon accounting methodology

Ignite's carbon accounting methodology is heavily inspired by what the GHG Protocol calls 'Using a combination of calculation methods' (scope 3 calculation guide, Introduction, page 13):

> For example, within each scope 3 category, a company may use more specific methods for the activities that contribute most to emissions and less specific methods for the activities that contribute least to emissions.

In Ignite it is possible to add different sources related to emissions, where spend is typically the main one and the starting point. For all scopes and underlying categories, it is also possible to add emissions-related activities, that are mapped to emission factors using standard databases. To date (January 2024), the following data bases have been built in:

- [BEIS/DEFRA](https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2023): Emission factors created by the UK government for calculating and reporting emissions
- The International Panel for Climate Change ([IPCC](https://www.notion.so/Carbon-Accounting-Wiki-8d77e991b0e04d9cb80c7e6e3ab8fb12?pvs=21)): Emission factors for other greenhouse gases than CO₂ into CO₂-equivalents
- Association of Issuing Bodies ([AIB](https://www.aib-net.org/facts/european-residual-mix/2022)): The organisation that handles guarantees of origin across the European electricity market. Provides location- and market-based emission factors for electricity consumption
- [Hotelfootprints](https://www.hotelfootprints.org/): The source BEIS/DEFRA uses for emissions from hotel nights. We use this source directly to cover more countries.

For each added activity, relevant information is added to Ignite using a set of forms that vary depending on the scope and category. Certain forms have specific functionality, such as handling guarantees of origin and renewable energy certificates for electricity consumption. In addition to the emission categories selected when filling in the forms, connecting with specific emission factors, some additional information is used when selecting the best-fitting emission factor:

- A time range, that is used to describe when the activity took place. Typically a whole year, but with the possibility of more granular breakdowns. This information is used both for selecting which year the activity should be reported within, as well as for selecting the best fitting emission factor with regards to time. If we don’t have any emission factor for the selected year, we will choose the closest one in time.
- A country, which is used to select the best fitting regional emission factors if available. For many activities we only have one value, for instance for most categories from BEIS/DEFRA, but for electricity consumption, regional differences can be significant and we have factors for all the 34 countries in the AIB data set.

For all of the forms, it is possible to add already calculated emissions in kg or tonnes of CO₂e, with the relevant documentation as files, as well as comments to that activity. It is also possible to improve any spend-based estimates with relevant activities, which is covered more in detail below. To review any activity, all the relevant information, including who added it and when, is easily available in Ignite for internal reviews and external audits.

In certain cases with custom setups, other kinds of emission factor databases or activities uploaded to Ignite by bulk can also be used for the company’s carbon accounting. In these cases complete transparency on the raw data and how it is mapped to emission factors is available.

As spend-based estimates are highly uncertain, it is important to improve the relevant scope 3 estimates over time by switching the calculation methodology to the average data, hybrid, or supplier-specific methods for more and more spend over time. To do this, Ignite follows a 3-step approach to upstream scope 3 carbon accounting:

1. **Initial Coverage and Estimation**: Ignite's system begins with a broad coverage of emissions categories, creating initial estimates using procurement data. This includes matching spend with appropriate spend-based Exiobase emission factor, considering the year, region, and product category. This is done using either aggregated values per supplier and year, or detailed procurement data, typically on an invoice level. These differences are described to more detail below.
2. **Drill-Down into Specific Activities**: After establishing a baseline, the focus shifts to increasing the accuracy of emissions data in selected categories. This is achieved by transitioning from spend-based to activity-based calculations in key areas. Common categories for enhanced accuracy include business travel, raw materials, logistics, and waste management, but depends on the specifics of each company.
3. **Engagement with Suppliers for Specific Data**: The third step involves direct engagement with key suppliers to obtain more accurate, supplier-specific emission data. This is highly relevant for strategic categories or those that significantly contribute to an organisation's emissions. Supplier-specific data allow for more accurate tracking of emission reductions over time and can highlight the effectiveness of choosing lower-emission options.

This is a continuous process where companies using Ignite are able to over time improve their estimates. This is done both by switching out larger parts of their spend with more specific data for each year, and to use more and more supplier-specific data for their carbon accounting as more data is available from their suppliers.

### Spend-based estimates

Ignite provides out-of-the-box initial spend-based estimates by matching spend with emission factors from the Exiobase 3.8.2 database. There are three things that will have to be mapped as those are the three dimensions to the Exiobase database; year, region and product category:

- For mapping a purchase by its year, this is usually pretty straight forward. The most challenging decision is what date information to chose if more than one is available. If the reporting company has reporting years defined in their data, that information is used to match up the calculations with their financial reporting.
- Matching with an Exiobase region is usually also relatively simple, as most companies have supplier country as a field in their procurement data, where we have standard rulesets going from the different spellings of countries, as well as Alpha-2 codes, into the 49 Exiobase regions. In some cases, parts of the spend is also matched to regions using payment currencies where no supplier country is available.
- The third part of matching with an emission factor is the most challenging one; mapping to an Exiobase product category for goods and services. The first iteration of this process utilises supplier industry information from 3rd-party databases like [Enin](https://www.enin.ai/) and [Infobel](https://www.infobel.com/), where all NACE industry codes on the lowest level have been matched to Exiobase as a standard ruleset. Everything that is not categorised by this method at this stage will be put into the regional average bucket (weighted by industry size in each region), where only the supplier region and purchase year will decide the emission factor.

**The two different setups in Ignite and how it affects estimates**

- Supplier table
  - A setup in Ignite where the spend-based estimates are based on the supplier table, which means the total aggregated spend with each supplier, with values for each relevant year. The values are without VAT, and all in one currency. With this setup, users of Ignite can add NACE industry information or country in the cases where this was unavailable in the initial setup. It is also possible to adjust the information to better represent the actual goods or services procured from each supplier. The main limitation with this setup is that it is not possible to break down the spend-based estimate into more than one category per supplier, which reduces complexity, but also granularity and in some cases accuracy.
- Spend table
  - With this setup, the spend information in Ignite is on a much more granular level, typically on an invoice basis, but sometimes with PO data, or down to invoice line level. The next iteration of matching with Exiobase emission factors involves creating rules from more accurate information like GL account, product description or spend categorization, depending on what is available. In some cases it will be possible to map all spend by a high-accuracy dimension such as by a product master. If this is the case, then this should be strived for. However, note that it is the most important categories (when accounting for spend size, emissions size and how vital the category is for the company) that should be prioritised in this iterative work towards more accurate calculations. For this, the Ignite Classification module is used, where rulesets are built on each of the different dimensions used, with specific precedence of each ruleset.

### Improving estimates over time

In Ignite, it is easily possible to improve spend-based estimates by adding activities related to certain parts of a company’s spend. This works a bit differently for the two kinds of setups, but the principle is the same. When adding an activity, using the average data-, hybrid-, or supplier-specific methods, which translates to adding an activity that Ignite has a standard emission factors for, or an already calculated emission, that activity can be connected to spend.

- Supplier table
  - With this setup, it is possible to connect one or more activities to a supplier, where the spend-based estimate for the selected year will be disregarded as a result. If not all the spend with a supplier within a specific year can be covered by one activity, more will have to be added to make sure nothing is left out. The sum of all the added activities for a combination of supplier and year will replace the spend-based estimates for that same combination.
- Spend table
  - When emissions are estimated from the full spend table, it is possible to improve emissions with more granularity when going from spend to more specific estimates. The typical examples are still connected to spend with a certain supplier, but it can be defined to only cover transactions within a limited time period (not limited to full years), and with more specific clarifications such as only spend within a certain spend category or account.

### Reviewing estimates

An important part of reporting corporate GHG inventories is to align with the GHG Protocol principle of transparency. To do this in Ignite, all added activities have full transparency on who added it, when it was added and a change log of edits to each activity. Is is also possible to look into which emission factors has been used, with the potential to add descriptions and documentation for each activity. If an activity has been mapped to spend, i.e. improving the specificity of that estimate, this information is also easily available for each activity.
