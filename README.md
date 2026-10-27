# QM640 Capstone – Heart Disease

**Project:** Population-Level Classification and Risk-Factor Analysis of Coronary Heart Disease or Myocardial Infarction Among U.S. Adults Using CDC BRFSS 2024 Data

**Course:** QM 640 – Data Analytics Capstone, Walsh College  
**Student:** Priyanka Mane-Patil  
**Project stage:** Interim analysis completed; final validation and survey-design-adjusted inferential analyses remain in progress.

## Overview

This project studies factors associated with **self-reported coronary heart disease (CHD) or myocardial infarction (MI)** among U.S. adults using the CDC's 2024 Behavioral Risk Factor Surveillance System (BRFSS). It reports population-oriented descriptive prevalence, exploratory associations and adjusted odds ratios, and preliminary machine-learning classification results. BRFSS is a cross-sectional, self-reported survey: these analyses do **not** establish causation, predict future cardiovascular events, or provide a clinical diagnostic tool.

## Research questions

1. **RQ1 — Prevalence:** How does reported CHD/MI prevalence differ across age and sex groups?
2. **RQ2 — Associations:** Are smoking, physical inactivity, BMI category, and diabetes associated with reported CHD/MI?
3. **RQ3 — Adjusted associations:** Which measured factors are associated with CHD/MI after accounting for demographic and socioeconomic covariates?
4. **RQ4 — Classification:** How well do supervised learning models classify reported CHD/MI status?

## Data and outcome

- **Source:** [CDC BRFSS 2024 annual public-use data](https://www.cdc.gov/brfss/annual_data/annual_2024.html).
- **Outcome:** CDC calculated variable `_MICHD`, indicating reported CHD or MI (source codes 1 = Yes; 2 = No). The analysis creates a binary `heart_disease` outcome.
- **Eligible cleaned sample:** 452,464 respondents, including 42,338 positive and 410,126 negative records.
- **Survey design variables:** `_LLCPWT` (weight), `_STSTR` (stratum), and `_PSU` (primary sampling unit).
- **Data availability:** The original large BRFSS file and intermediate Parquet datasets are not stored in this repository. See [data access instructions](data/README_data_access.md) and the [variable dictionary](data/data_dictionary.csv). Reproduce the analysis using the official CDC data and the notebook.

## Interim results

| Research question | Interim evidence | Interpretation / status |
| --- | --- | --- |
| RQ1 | Survey-adjusted overall prevalence **6.80%** (95% CI **6.66%–6.94%**); male **8.12%**, female **5.53%** | Descriptive survey-adjusted estimates completed; further formal comparisons remain. |
| RQ2 | Weighted prevalence charts and exploratory Pearson chi-square tests for smoking, physical activity, BMI category, and diabetes | Descriptive weighted comparisons completed; hypothesis tests are **not survey-design-adjusted**. |
| RQ3 | Exploratory multivariable logistic regression with odds-ratio table | Based on an unweighted, regularized model; reported confidence intervals are approximate and should **not** be interpreted as design-adjusted inference. |
| RQ4 | Preliminary comparison of logistic regression, decision tree, random forest, and gradient boosting | Stratified 60,000-record modeling sample (48,000 train; 12,000 test); additional validation and threshold tuning remain. |

**RQ4 preliminary model metrics** (from [model comparison CSV](outputs/RQ4_preliminary_model_comparison.csv)):

| Model | AUROC | AUPRC | Precision | Recall | F1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Logistic regression | 0.824 | 0.318 | 0.225 | 0.794 | 0.350 |
| Decision tree | 0.764 | 0.263 | 0.217 | 0.652 | 0.325 |
| Random forest | 0.809 | 0.311 | 0.223 | 0.764 | 0.345 |
| Gradient boosting | 0.821 | 0.323 | 0.537 | 0.026 | 0.049 |

The prespecified recall target of at least 0.80 was **not met** by any of these models at the evaluated thresholds. All four met the exploratory precision target of at least 0.20. Model results are preliminary and must not be presented as external or clinical validation.

## Repository structure

```text
QM640-Capstone-Heart-Disease/
├── README.md
├── requirements.txt
├── data/
│   ├── README_data_access.md
│   └── data_dictionary.csv
├── notebooks/
│   ├── 01_import_clean.ipynb
│   ├── 01_import_clean_BRFSS_2024.ipynb
│   ├── 02_eda_rq1.ipynb
│   ├── 03_rq2_rq3_statistics.ipynb
│   └── 04_rq4_modeling.ipynb
├── src/
├── outputs/
│   ├── *.csv               # 23 exported analysis and validation tables
│   ├── figures/            # 6 exported PNG figures
│   └── tables/
```

The [BRFSS 2024 analysis notebook](notebooks/01_import_clean_BRFSS_2024.ipynb) contains the completed interim workflow. Some other notebook and source paths may be preliminary scaffolding; refer to the executed analysis notebook and exported evidence for completed results.

## Key evidence files

- [Overall weighted prevalence](outputs/RQ1_overall_survey_adjusted.csv), [sex estimates](outputs/RQ1_sex_survey_adjusted.csv), and [age-group estimates](outputs/RQ1_age_survey_adjusted.csv)
- [RQ2 exploratory association tests](outputs/RQ2_preliminary_association_tests.csv)
- [RQ3 report-ready exploratory odds ratios](outputs/RQ3_report_ready_odds_ratios.csv)
- [RQ4 preliminary model comparison](outputs/RQ4_preliminary_model_comparison.csv) and [confusion matrices](outputs/RQ4_confusion_matrices.csv)
- [Modeling sample and split metadata](outputs/modeling_metadata.csv)
- [Interim analysis status summary](outputs/QM640_interim_analysis_summary.csv) and [output validation](outputs/final_output_validation.csv)
- [Charts and figures](outputs/figures/)

## Reproducibility and methodological cautions

1. Obtain the official BRFSS 2024 data and documentation from the CDC. Do not commit large raw files or private access tokens.
2. Review the data access instructions, dictionary, requirements, and executed notebook before rerunning.
3. Distinguish **survey-weighted prevalence** from **unweighted exploratory hypothesis tests and modeling**; do not label the latter survey-adjusted.
4. Avoid leakage from variables used to construct `_MICHD` into classification features.
5. Treat regularized-model odds ratios and approximate confidence intervals as exploratory until appropriate inferential procedures are completed.
6. Planned next steps include survey-adjusted association tests, an appropriately specified explanatory model, fuller model validation, and threshold evaluation.

## Ethics and limitations

This analysis uses public-use, de-identified survey data and reports aggregate findings. Self-report, missing data, residual confounding, survey design, class imbalance, and the cross-sectional study design limit interpretation. No causal, individual-diagnostic, or prospective risk claims are made.
