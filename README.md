# OULAD Deadline Risk Prediction

MSc Dissertation Project — Predicting student deadline risk using machine learning on the Open University Learning Analytics Dataset (OULAD).

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=oulad_venv --display-name "OULAD (venv)"
```

## Project Structure
├── data/
│   ├── raw/          # Symlink to OULAD CSVs (not committed to Git)
│   └── processed/    # Engineered features (not committed to Git)
├── notebooks/        # Jupyter notebooks (one per phase)
├── src/              # Reusable Python modules
├── models/           # Saved trained models
├── reports/          # Figures and output charts
├── logs/             # Experiment logs
└── config.yaml       # All project constants — no magic numbers in code

## Phases
- **Phase 1:** Exploratory Data Analysis (EDA)
- **Phase 2:** Feature Engineering & Preprocessing
- **Phase 3:** Model Training & Evaluation
- **Phase 4:** Fairness Analysis & Ethics
