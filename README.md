# Max Hours Pass Predictor

A beginner-friendly machine learning script that predicts whether a student
will **pass** or **fail** based on the number of hours they studied, using
Logistic Regression from scikit-learn.

## How it works

- Training data maps hours studied → pass (1) / fail (0):
  - 1 hour → Fail
  - 2 hours → Fail
  - 3 hours → Pass
  - 4 hours → Pass
- A `LogisticRegression` model is fit on this data.
- The script then asks the user to input their own study hours and predicts
  whether they will pass or fail.

## Requirements

```
pip install -r requirements.txt
```

## Usage

```
python main.py
```

Example:

```
Enter your number of study hours: 3.5
Based on hours=3.5, you likely PASS
```

## Notes

- This is a toy example with only 4 training points — it's meant for
  learning how `LogisticRegression` works, not for real predictions.
- Feature/label shapes matter in scikit-learn: `x` must be a list of lists
  (2D), one inner list per sample, e.g. `[[1], [2], [3], [4]]` — not
  `[1], [2], [3], [4]` (which is a tuple of separate lists and will raise
  an error).

## Possible next steps

- Add more training data points for a more reliable model.
- Plot the sigmoid decision boundary with matplotlib.
- Try `model.predict_proba()` to show the probability of passing.
