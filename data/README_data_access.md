# Data Access Instructions

## Primary Source
Centers for Disease Control and Prevention (CDC), Behavioral Risk Factor Surveillance System (BRFSS), 2024 annual data.

Official annual data page:
https://www.cdc.gov/brfss/annual_data/annual_2024.html

## Recommended Download
Download the 2024 combined landline and cellular public-use file in SAS Transport (XPT) format from the official CDC page.

The same page also provides supporting documentation including:
- Codebook
- Variable layout
- Calculated-variable documentation
- Survey questionnaire
- Weighting guidance
- Data-quality / comparability documentation

## Important Notes
1. Do not use Kaggle mirrors or repackaged copies for the primary analysis.
2. Retain the original source filename and record the download date.
3. Keep raw files unchanged.
4. Store the raw XPT file locally under a `data/raw/` folder if working outside GitHub.
5. Do not commit large raw files to GitHub unless permitted and practical.
6. Use the official CDC documentation to interpret missing/refused/don't-know codes.
7. Use BRFSS survey-design variables and the final survey weight for population inference.

## Primary Outcome
`_MICHD` – CDC calculated indicator for reported myocardial infarction or coronary heart disease.

The component variables used to construct `_MICHD` must not be used as predictors in classification models because that would create target leakage.
