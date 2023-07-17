# Changelog

A document describing the changes to this project, formatted based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

The versioning mainly follows the updates to the emission factor database (first two numbers). However, this changelog document also document other notable changes to this project, noted by the PATCH version (last number in the versioning).

## [1.1.6] - 2023-07-13

Updating the activity-based emission factors with more factors from BEIS/DEFRA for scope 3. Also adding some tooling for converting the emission factor CSV to the needed types for our Ignite carbon accounting module.

### Updated

- Activity-based emission factor database
- Script for generating keys

### Added

- Tooling for getting types from emission factor CSV

## [1.1.5] - 2023-06-22

### Added

- Method for generating keys for the activity-based emission factors

## [1.1.4] - 2023-05-02

Adding the first version of our database for activity based emission factors. This will be used in our Ignite app in the cases where activity-data is added in addition to spend-based calculations. Also fixing a faulty link.

### Updated

- Structure of emission factor directory

### Added

- First version of our activity-based emission factor database

### Fixed

- Link to Exiobase emission factor description from main README-file

## [1.1.3] - 2023-03-13

General updates to the texts in the three documents listed below. Primarily minor fixes of spelling and structure to make the information more clear and concise, but also the addition of concrete examples from Ignite's own carbon accounting.

### Updated

- Changelog
- Readme
- Methodology

### Added

- More specific examples from Ignite's own carbon accounting and results of using the methodology.

## [1.1.2] - 2023-01-13

A restructuring of the directory structure, preparing for more information on methodology past spend-based emission calculations and the addition of code and raw data used to extract the adapted version of Exiobase.

### Added

- Changelog
- Citation
- Methodology directory
  - Moved spend-based methodology to a new document
  - Added initial description of methodology on activities and supplier-specifics
- Exiobase emission factor directory
  - Exiobase raw data
  - Python notebook extracting and adjusting the Exiobase data
  - Updated emission factor excel document

## [1.1.1] - 2022-11-29

First version of methodology-description was developed and emission factors added.

### Added

- The v1.1 Ignite version of Exiobase
- Readme with information both about methodology and adaption of Exiobase
- License in accordance to the Exiobase terms of use

## [1.1.0] - 2022-11-21

Initiation of the Ignite Carbon Accounting public github repository. Only a single readme with some initial information was added at this time.

## [1.0] - N/A

The initial Ignite methodology and use of the Exiobase database. The methodology was solely based on supplier industry information for Nordic suppliers, matched to the second level of NACE, and Exiobase was not altered as matches with outliers were rather adjusted to a similar non-outlier emission factor.
