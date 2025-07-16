Credit Risk Prediction Dashboard

What is this?

This is an interactive AI-powered dashboard that helps estimate whether a loan applicant is likely to default.

Instead of uploading datasets or writing code, the user simply fills out a form — things like income, loan amount, FICO score, and reason for loan — and with one click, the app tells them:

- **How risky the applicant is**
- **The probability that they'll default**
- **Whether they’re flagged as a High-Risk or Low-Risk borrower**

It’s built for clarity and speed — giving lenders or analysts a fast, simple, and intelligent tool to evaluate credit risk.

---

## 🎯 Why I Built This

In real-world banking and fintech systems, **credit scoring** is a key process. But most machine learning projects focus only on model accuracy — not usability.

I wanted to build something that’s:
- 🔍 **Easy to understand** (no technical background needed)
- ⚡ **Instantly usable** (no file uploads, just a form)
- 💡 **Realistic** (using features that banks actually consider)
- 🤖 **Powered by AI** (XGBoost classifier under the hood)

Whether you're evaluating a new customer, demonstrating AI in action, or just exploring fintech ML — this app bridges the gap between **AI predictions** and **human decisions**.

---

## 📈 What It Predicts

After you enter the applicant details, the model returns:

| Metric                  | What It Means                                      |
|-------------------------|----------------------------------------------------|
| **Default Probability** | A number between `0.00` and `1.00` (higher = risky)|
| **Risk Flag**           | ✅ Low Risk or ⚠️ High Risk (based on threshold)  |

> For example: A score of `0.84` means there’s an 84% chance the applicant might default — flagged as high risk.

---


## 📌 Features

- 🔍 Real-time prediction of loan default risk
- 📋 Simple form-based UI — no need to upload files
- ⚙️ Trained on synthetic data with industry-style features
- 📊 Default probability score + risk flag
- ✅ Ready for deployment or extension to real datasets

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/credit-risk-dashboard-streamlit.git
cd credit-risk-dashboard-streamlit

# Install dependencies
pip install -r requirements.txt

# Launch the dashboard
streamlit run app.py
