# 🩺 Data Doctor Application — Enterprise Data Quality

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Data Quality](https://img.shields.io/badge/Data%20Quality-Validation-orange)
![Testing](https://img.shields.io/badge/Testing-PyTest-green)

Production-style **data-quality and diagnostic toolkit** demonstrating how to validate datasets, profile schemas, detect common quality problems and generate actionable remediation reports.

## 👨‍💻 Author

**Kiran Tayde — Senior Data Scientist | Machine Learning | Data Quality | Analytics | NLP**

GitHub: https://github.com/kirangtayde

## 🎯 Objective

Reliable ML and analytics depend on reliable data. This project demonstrates a reusable framework for finding data-quality issues before they propagate into downstream analytics or models.

## 🔍 Capabilities

- Schema and data-type validation
- Missing-value detection
- Duplicate detection
- Outlier and distribution diagnostics
- Constraint validation
- Data-quality scoring
- Structured JSON reporting
- Reusable Python components
- API-ready architecture

## 🧩 Architecture

```text
Input Dataset
     ↓
Profiler
     ↓
Validation Rules
     ↓
Quality Score
     ↓
Diagnosis
     ↓
Remediation Report
```

## 📊 Example Quality Checks

| Check | Purpose |
|---|---|
| Schema | Detect unexpected columns/types |
| Missingness | Identify incomplete fields |
| Duplicates | Detect repeated records |
| Range | Validate business boundaries |
| Distribution | Identify unusual patterns |
| Constraints | Enforce data rules |

## 🔐 Responsible Use

This repository contains a clean portfolio implementation. It does **not** contain Blue Yonder proprietary source code, credentials, customer information or confidential assets.

## 🛠️ Stack

Python • Pandas • Validation concepts • PyTest • FastAPI-ready design

## 📁 Project Structure

```text
src/
├── profiler.py
├── validators.py
├── quality_score.py
└── reporting.py

tests/
requirements.txt
README.md
```

## 🚀 Quick Start

```bash
git clone https://github.com/kirangtayde/data-doctor-application.git
cd data-doctor-application
python -m venv .venv
pip install -r requirements.txt
pytest -q
```

## 📌 Resume Summary

**Data Doctor Application | Python, Pandas, Data Quality** — Designed a reusable data-quality diagnostic workflow for schema validation, missing-value analysis, duplicate detection, constraints, quality scoring and remediation reporting.

## 🔗 Connect

**Kiran Tayde** · Senior Data Scientist · Data Quality · Machine Learning · Analytics

https://github.com/kirangtayde