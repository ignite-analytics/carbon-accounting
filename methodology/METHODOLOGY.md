## Table of contents

- [Introduction](#introduction)
- [Ignite Carbon Accounting Methodology](#ignite-carbon-accounting-methodology)
  - [Step 1: Create heatmap](#step-create-heatmap)
  - [Step 2: Select activities](#step-select-activities)
  - [Step 3: Supplier specifics](#step-supplier-specifics)

## Introduction

Quite a lot of the indirect emissions covered by the 15 categories of scope 3 can usually be estimated using procurement data, especially when considering the typical sizes of the different categories. Scope 3 category 1: purchased goods and services, is usually the largest source of emissions for an organization, also when including scope 1 and 2. For Ignite, this one category covers around 90% of our total emissions. Naturally, this is a category where the most detailed information related to the emissions, i.e. what do you buy and from who do you buy it, is something procurement covers better than any other part of an organization. As Ignite Procurement in it's core is a data- and analytics platform focusing on strategic procurement, building on top of that functionality to include calculations on indirect emissions was a natural step.

There are also other parts of an organizations scope 3 emissions where procurement data can be used as the basis for calculation. These include

- Category 2: capital good
  - Calculated in the same way as category 1, just distinguished by what is considered capital goods in financial reporting.
- Category 3: fuel and energy-related activities
  - Only partly covered, as it is the cradle-to-gate emissions of purchased fuels that can be calculated from spend using the emission factors available. Other parts of this category is not currently covered by a spend-based approach, but could potentially be sometime in the future.
- Category 4: transportation and distribution
  - In the cases where the organization pays for this separately.
- Category 5: waste generated in operations
  - This is partly covered as yes, most organizations pay for this, but then again an activity-based method where the quantities and types of waste are combined with information about how the waste is handled, will give much more accurate results.
- Category 6: business travel
  - Indeed covered as this is something organizations pays for, but oftentimes bulked into joint invoices from travel agencies where it is hard to say how much is used on what part of the travel.

## Ignite carbon accounting methodology

Ignite follows a 3-step approach to upstream scope 3 carbon accounting:

1. Start by covering as many categories (both scope 3 categories and spend categories when based on procurement data) to create initial estimates that enables insights into where to focus further efforts.
2. Drill down into the categories of interest where more effort should be used to increase the accuracy, for instance by switching from a spend-based to an activity-based calculation.
3. Contact the most essential suppliers within targeted categories to approach supplier specific calculation. This is necessary to be able to directly compare two different suppliers within the same industry or products within the same product/service category.

![image](https://user-images.githubusercontent.com/88656160/204540717-3844d08e-604b-449a-9af9-49bc5b2e939c.png)

### Step 1: Create heatmap

What Ignite provides out of the box and which can be set up within a day of having access to a company's procurement data is the initial match of every single purchase with a spend-based Exiobase emission factor. There are three things that will have to be matched as those are the three dimensions to the Exiobase database: year, region and product category.

For mapping a purchase by its year, this is usually pretty straight forward, the most challenging decision is what date to chose if more are available. We try to use the year from the transaction date where possible, but invoice date can also be used, and if the company has fiscal years defined in their data, that information is used to match up the calculations with their financial reporting. Matching with an Exiobase region is usually also relatively simple, as most companies have supplier country as a field in their procurement data, where we have standard rulesets going from the different spellings of countries, as well as Alpha-2 codes, into the 49 Exiobase regions.

The third part of matching with an emission factor, matching each transaction with an Exiobase product/service category is the most challenging one, and is usually done in multiple iteration with increasing accuracies. The first iteration of this process utilize supplier industry information from 3rd-party databases like [Enin](https://www.enin.ai/) and [Infobel](https://www.infobel.com/), where all NACE and SIC industry codes on the lowest level have been matched to Exiobase as standard rulesets. Everything that is not categorized by this method at this stage will be put into the regional average bucket, where only the supplier region and purchase year will decide the emission factor. The next iteration involves creating rules from more accurate information like GL account, product description or spend categorization, depending on what is available. In some cases it will be possible to map all spend by a high-accuracy dimension such as by a product master. If this is the case, then this should be strived for. However, note that it is the most important categories (when accounting for spend size, emissions size and how vital the category is for the company) that should be prioritized in this iterative work towards more accurate calculations.

The flow of this process is described in the slide below.

![image](https://user-images.githubusercontent.com/88656160/204540792-8ecec762-a6d2-4c98-98ff-736653e1bd63.png)

For the other parts of scope 3 categories not related to procurement, other initial estimates should be conducted as a screening to add information on where further efforts should be focused.

### Step 2: Select activities

![image](https://user-images.githubusercontent.com/88656160/204543215-604eec5c-6444-402c-b2c4-ab0f6879c023.png)

### Step 3: Supplier specifics

![image](https://user-images.githubusercontent.com/88656160/204543274-40515d15-3727-40b0-9e5d-9d34d225aae4.png)
