# Project Plan

## Title
<!-- Give your project a short title. -->
Analyzing Crime Rates in Uzbekistan: A Demographic Perspective

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How do the factors of Population Density and Income Levels affect the Crime Rates in Uzbekistan?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The primary goal of the project is to address the issue of rising crime rates in Uzbekistan, which is a major concern for the country's inhabitants and authorities. Crime rates have an impact on the population's safety and well-being, and knowing the underlying issues is critical for making informed decisions.

This research takes a data-driven approach, employing Multiple Regression Analysis, which integrates crime statistics with demographic data, such as population density and income levels. The purpose is to look at potential correlations and dependencies between these variables.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: CrimeRate
* Metadata URL: https://stat.uz/images/Docs/415-sotssfera_crime-en.pdf
* Data URL: https://api.stat.uz/api/v1.0/data/hududlar-kesimida-jami-royxatga-olingan-jinoyatla?lang=en&format=xlsx
* Data Type: XLSX

Short description of the DataSource: Recorded crimes across all services lines by region

### Datasource2: PopulationDensity
* Metadata URL: https://stat.uz/images/uploads/docs/21___Population_en.pdf
* Data URL: https://api.stat.uz/api/v1.0/data/aholining-zichligi?lang=en&format=xlsx
* Data Type: XLSX

Short description of the DataSource: Population density at the beginning of the year, the number of inhabitants per 1 sq. km

### Datasource3: IncomeLevels
* Metadata URL: https://stat.uz/images/uploads/docs/315___Total_per_capita_income_by_region_en.pdf
* Data URL: https://api.stat.uz/api/v1.0/data/hududlar-boyicha-aholi-jon-boshiga-umumiy-darom?lang=en&format=xlsx
* Data Type: XLSX

Short description of the DataSource: Total per capita income by region, thousand soums. For 2000-2009 given cash incomes, from 2010 total comprehensive income, since 2010 revised data. 

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Data Preparation [#1][i1]
2. Model Building [#2][i2]
3. Visualization [#3][i3]
4. Automated Tests [#4][i4]
5. Analysis and Conclusions [#5][i5]
6. Final Report [#6][i6]
7. Make the Repository Presentable [#7][i7]
8. Project Presentation and Blogpost [#8][i8]

[i1]: https://github.com/Ozodbek47/DataEngineering/issues/1
[i2]: https://github.com/Ozodbek47/DataEngineering/issues/2
[i3]: https://github.com/Ozodbek47/DataEngineering/issues/3
[i4]: https://github.com/Ozodbek47/DataEngineering/issues/4
[i5]: https://github.com/Ozodbek47/DataEngineering/issues/5
[i6]: https://github.com/Ozodbek47/DataEngineering/issues/6
[i7]: https://github.com/Ozodbek47/DataEngineering/issues/7
[i8]: https://github.com/Ozodbek47/DataEngineering/issues/8