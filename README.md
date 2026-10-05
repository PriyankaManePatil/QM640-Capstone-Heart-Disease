# QM640 Capstone – Heart Disease

## Project Title
**Population-Level Classification and Risk-Factor Analysis of Coronary Heart Disease or Myocardial Infarction Among U.S. Adults Using CDC BRFSS 2024 Data**

## Course
QM 640 – Data Analytics Capstone  
Walsh College

## Student
Priyanka Mane-Patil

## Project Overview
This capstone analyzes demographic, behavioral, socioeconomic, and health-related factors associated with self-reported coronary heart disease (CHD) or myocardial infarction (MI) among U.S. adults using the 2024 Behavioral Risk Factor Surveillance System (BRFSS) public-use dataset from the U.S. Centers for Disease Control and Prevention (CDC).

The study combines survey-weighted descriptive statistics, hypothesis testing, multivariable logistic regression, and supervised machine-learning classification. Because BRFSS is cross-sectional and self-reported, the project focuses on association and classification of prevalent CHD/MI rather than causal inference or prospective clinical risk prediction.

## Primary Outcome
CDC calculated variable `_MICHD`:
- 1 = Respondent reported coronary heart disease or myocardial infarction
- 2 = Respondent did not report coronary heart disease or myocardial infarction

Variables used to construct `_MICHD` will not be used as predictors in machine-learning models to avoid target leakage.

## Research Questions
1. Does reported CHD/MI prevalence differ across age and sex groups?
2. Are smoking, physical inactivity, BMI category, and diabetes associated with reported CHD/MI?
3. After adjustment for demographic and socioeconomic characteristics, which measured factors are independently associated with the odds of reported CHD/MI?
4. How accurately can supervised machine-learning models classify reported CHD/MI status using demographic, behavioral, and health predictors?

## Data Source
CDC BRFSS 2024 annual public-use data and documentation:  
https://www.cdc.gov/brfss/annual_data/annual_2024.html

The dataset is publicly available and does not require an account or data-use application.

## Planned Sample
The project synopsis specifies a minimum analytic sample of **N = 56,920**, selected as the largest requirement across RQ1–RQ4 after accounting for model-evaluation needs.

## Planned Analytical Methods
- Survey-weighted descriptive statistics
- Prevalence estimates with 95% confidence intervals
- Chi-square / survey-adjusted association testing
- Unadjusted and adjusted odds ratios
- Multivariable logistic regression
- Baseline logistic-regression classifier
- Decision tree
- Random forest
- Gradient boosting
- Cross-validation
- Leakage-safe preprocessing
- Class-imbalance-aware evaluation
- AUROC, AUPRC, sensitivity, specificity, precision, F1-score, balanced accuracy, confusion matrix, and Brier score

## Repository Structure
```
QM640-Capstone-Heart-Disease/
├── README.md
├── requirements.txt
├── data/
│   ├── README_data_access.md
│   └── data_dictionary.csv
├── notebooks/
│   ├── 01_import_clean.ipynb
│   ├── 02_eda_rq1.ipynb
│   ├── 03_rq2_rq3_statistics.ipynb
│   └── 04_rq4_modeling.ipynb
├── src/
│   ├── preprocessing.py
│   ├── survey_analysis.py
│   └── modeling.py
└── outputs/
    ├── tables/
    └── figures/
```

## Reproducibility
Raw CDC files will not be re-hosted unless appropriate. The `data/README_data_access.md` file contains authoritative source links and instructions for obtaining the raw BRFSS data. All transformations and analysis steps will be documented in notebooks and reusable source files.

## Ethical and Methodological Notes
This project uses publicly released, de-identified survey data. Results will be reported at aggregate level. The project will not make causal claims, provide patient-level diagnosis, or be presented as a replacement for validated clinical cardiovascular risk tools.

## Status
Capstone synopsis and repository setup in progress.
