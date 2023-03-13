## Table of contents

- [Introduction](#introduction)
- [Ignite Carbon Accounting Methodology](#ignite-carbon-accounting-methodology)
  - [Step 1: Create heatmap](#step-create-heatmap)
  - [Step 2: Select activities](#step-select-activities)
  - [Step 3: Supplier specifics](#step-supplier-specifics)
- [Results](#results)

## Introduction

Quite a lot of the indirect emissions covered by the 15 categories of scope 3 can usually be estimated using procurement data, especially when considering the typical sizes of the different categories. Scope 3 category 1: purchased goods and services, is usually the largest source of emissions for an organization, also when compared with scope 1 and 2. For Ignite, this one category covers around 62% of our total emissions. Naturally, this is a category where the most detailed information related to the emissions, i.e. what do you buy and from who do you buy it, is something procurement covers better than any other part of an organization. As Ignite Procurement in its core is a data- and analytics platform focusing on strategic procurement, building on top of that functionality to include calculations on indirect emissions was a natural step.

There are also other parts of an organizations scope 3 emissions where procurement data can be used as the basis for calculation. These are

- Category 2: capital good
  - Calculated in the same way as category 1, just distinguished by what is considered capital goods in financial reporting.
- Category 3: fuel and energy-related activities
  - This category includes the cradle-to-gate emissions of purchased fuels and electricity, as well as the transportation and distribution losses of purchased electricity. The GHGP scope 3 calculation guidance (scope 3 guide[^ghgp-scope3], Chapter 3) does not mention spend as a source for calculating this category, so this is mainly relevant where activity data is available either in the procurement data or separately. However, Exiobase does include spend-based emission factors for cradle-to-gate emissions for a range of fuels, with regional and temporal distinguishment that is lacking for some activity-based emission factors for the same products. A spend-based approach could therefore be used for screening purposes, even though care should be taken, and it should not be used in reporting to be in accordance with the GHGP.
- Category 4: transportation and distribution
  - In the cases where the organization pays for this separately, this can definitively be covered by procurement data. If not fuel amount or distances are available, then a spend-based approach can be used. Note that this category covers both inbound and outbound logistics, as long as the reporting corporation pays for the service.
- Category 5: waste generated in operations
  - This is partly covered as yes, most organizations pay for this, but then again an activity-based method where the quantities and types of waste are combined with information about how the waste is handled, will give much more accurate results. Note that a spend-based approach is not strictly speaking listed in the GHGP scope 3 calculation guidance for category 5 (scope 3 guide[^ghgp-scope3], Chapter 5), but still used for screening purposes in the [GHGP/Quantis calculation tool](https://quantis-suite.com/Scope-3-Evaluator/).
- Category 6: business travel
  - Indeed covered as this is something organizations pays for, but oftentimes bulked into joint invoices from travel agencies where it is hard to say how much is used on what part of the travel. This is a category where many companies today have calculated their emissions related to air travel, but typically not other parts of their business travel.

Note that in this setting, procurement data will mostly be used with a spend-based approach, but in some cases the data also include quantities or other activity-based information on a product level that can be used with activity-based or supplier-specific calculations.

## Ignite carbon accounting methodology

The Ignite Procurement methodology is heavily inspired by what the GHGP calls 'Using a combination of calculation methods' (scope 3 guide[^ghgp-scope3], Introduction, page 13):

> For example, within each scope 3 category, a
> company may use more specific methods for the activities that contribute most to emissions and less specific methods
> for the activities that contribute least to emissions.

To do this, Ignite follows a 3-step approach to upstream scope 3 carbon accounting:

1. Start by covering as many categories (both scope 3 categories and spend categories when based on procurement data) to create initial estimates that enables insights into where to focus further efforts.
2. Drill down into the categories of interest where more effort should be used to increase the accuracy, for instance by switching from a spend-based to an activity-based calculation.
3. Contact the most essential suppliers within targeted categories to approach supplier specific calculation. This is necessary to be able to directly compare two different suppliers within the same industry or products within the same product/service category.

![image](https://user-images.githubusercontent.com/88656160/204540717-3844d08e-604b-449a-9af9-49bc5b2e939c.png)

### Step 1: Create heatmap

What Ignite provides out of the box and which can be set up within a day of having access to a company's procurement data is the initial match of every single purchase with a spend-based Exiobase emission factor. There are three things that will have to be matched as those are the three dimensions to the Exiobase database: year, region and product category.

For mapping a purchase by its year, this is usually pretty straight forward. The most challenging decision is what date to chose if more are available. We try to use the year from the transaction date where possible, but invoice date can also be used, and if the company has fiscal years defined in their data, that information is used to match up the calculations with their financial reporting. Matching with an Exiobase region is usually also relatively simple, as most companies have supplier country as a field in their procurement data, where we have standard rulesets going from the different spellings of countries, as well as Alpha-2 codes, into the 49 Exiobase regions. In some cases, parts of the spend is also matched to regions using payment currencies where no supplier country was available.

The third part of matching with an emission factor, matching each transaction with an Exiobase product/service category is the most challenging one, and is usually done in multiple iteration with increasing accuracies. The first iteration of this process utilize supplier industry information from 3rd-party databases like [Enin](https://www.enin.ai/) and [Infobel](https://www.infobel.com/), where all NACE and SIC industry codes on the lowest level have been matched to Exiobase as standard rulesets. Everything that is not categorized by this method at this stage will be put into the regional average bucket (weighted by industry size in each region), where only the supplier region and purchase year will decide the emission factor. The next iteration involves creating rules from more accurate information like GL account, product description or spend categorization, depending on what is available. In some cases it will be possible to map all spend by a high-accuracy dimension such as by a product master. If this is the case, then this should be strived for. However, note that it is the most important categories (when accounting for spend size, emissions size and how vital the category is for the company) that should be prioritized in this iterative work towards more accurate calculations.

The flow of this process is described in the slide below.

![image](https://user-images.githubusercontent.com/88656160/204540792-8ecec762-a6d2-4c98-98ff-736653e1bd63.png)

For the other parts of scope 3 categories not related to procurement, other initial estimates should be conducted as a screening to add information on where further efforts should be focused. This is however not something that has been built into Ignite at this stage.

### Step 2: Select activities

All organizations should strive towards increasing the accuracy of their calculated emissions over time. However, the first step is to start somewhere, so this is mostly relevant after running the spend-based method and an initial screening. Based on those results and the specifics of your corporation/organization, it should be possible to select certain categories where it is necessary to increase the accuracy to be able to start more specific initiatives on emission reduction.

Some categories are more common for this exercise than others, both based on the availability of more specific emission data and what categories the accuracy increases the most when moving from spend-based to activity-based calculations. A typical example that many companies have already started with is the business travel category, specifically for air travel as this is something many travel agencies have numbers on already and it is a much talked about category. Calculations based on the number of passengers and the distance of a flight is much more accurate than only looking at the spend, as tickets to the same flight will vary hugely in price based on availability and other factors that doesn't necessarily increase the emissions correspondingly (for instance buying business vs economy). Other typical categories are as shown in the image below:

- Raw materials
  - The cradle-to-gate emissions for fuels (scope 3, category 3)
  - Packaging and building materials, where the prices often fluctuate quite a bit within a year (scope 3 category 1)
- Logistics
  - A category where activity data is often reasonably available and where the calculated results are more accurate than with a spend-based approach
- Waste
  - Scope 3 category 5 can be covered by a spend-based approach, but an activity-based calculation will be much more accurate as more information on the type of waste and what is being done with it can be included
- Business travel
  - Especially the flights can be covered well with activity-based calculations, but also to a larger degree other modes of transport and hotel stays as well. A possibility is to use numbers from your travel agency on flights, but the spend-based approach on the rest of this category.

![image](https://user-images.githubusercontent.com/88656160/204543215-604eec5c-6444-402c-b2c4-ab0f6879c023.png)

### Step 3: Supplier specifics

For the products that are of strategic importance and that by initial screening seems to represent a relatively large portion of your emissions, you should strive towards getting supplier specific emission estimates. This is both as a step to increase the accuracy, but also of importance when measuring reductions over time as neither spend- nor activity-based calculations typically shows anything other than a general decrease in spend or activity amount, or a general trend within the industry.

Another important consideration is the fact that organizations sometimes chose to pay more for a goods or service that has less emissions, which would in a spend-based calculation increase the estimate, while it should be lowered. The main solution to this is to move to supplier specific calculations for these cases.

![image](https://user-images.githubusercontent.com/88656160/204543274-40515d15-3727-40b0-9e5d-9d34d225aae4.png)

As shown in the image above, it is important to take into account the methodology, completeness and assumptions related to the supplier specific numbers. Today there are still many different ways of calculating emissions, and few companies have calculated their total scope 3, so when comparing numbers from different suppliers, make sure to do the comparison on similar grounds.

## Results

Using this methodology, it is possible to get corporation-level results of emissions within different parts of scope 3 that can be used for reporting. Additionally, the results will give insights into where the estimated emission hot-spots are and where to focus efforts related to increasing accuracy and reducing emissions. It is also essential to move to supplier-specific calculations (in some cases activity-based ones can also be enough) to be able to actually measure the effect of reduction initiatives.

For Ignite's own emissions, this method, with the addition of some activity-based calculations on scope 2 and other parts of scope 3, resulted in the following emissions.

When combined with company metrics such as number of employees and sales revenue, it becomes possible to showcase the emission intensities over time, relevant for target-setting and comparison with other similar companies. This can also be used to compare oneself or suppliers to the industry average by comparing to the corresponding Exiobase emission factor as seen with below with Ignite's emission intensities.

With a combination of methods, it is important to be able to visualize the distribution of what data and what calculation methods that have been used on the relative portions of the total calculated emissions. The analytics below show examples of this directly from our own carbon accounting.

[^ghgp-scope3]: [Greenhouse Gas Protocol: Technical Guidance for Calculating Scope 3 Emissions](https://ghgprotocol.org/sites/default/files/standards/Scope3_Calculation_Guidance_0.pdf)
