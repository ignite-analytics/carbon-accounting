# Changelog

A document describing the changes to this project, formatted based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

The versioning mainly follows the updates to the emission factor database (first two numbers). However, this changelog document also document other notable changes to this project, noted by the PATCH version (last number in the versioning).

## [1.1.3] - 2023-03-13

General updates to the texts in the three documents listed below. No major changes, only minor fixes of spelling and sentences to make the information more clear and concise.

### Updated

- Changelog
- Readme
- Methodology

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
