import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load data
df = pd.read_csv("dataset/raw_student_data_sem1.csv")

# ---- FIX 1: Encode Prev_Year_Label FIRST ----
prev_map = {
    "Poor": 0,
    "Average": 1,
    "Good": 2,
    "NIL": 3
}

df["Prev_Year_Label"] = df["Prev_Year_Label"].map(prev_map)
df["Prev_Year_Label"] = df["Prev_Year_Label"].fillna(3)

# ---- FIX 2: Encode target Label ----
label_enc = LabelEncoder()
df["Label"] = label_enc.fit_transform(df["Label"])

# ---- FIX 3: Features and target ----
X = df[["IAT1", "IAT2", "Model_Mark", "Prev_Year_Label"]]
y = df["Label"]

# ---- Scaling ----
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---- Train-test split ----
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# ---- Train SVM ----
svm = SVC(kernel="rbf", probability=True)
svm.fit(X_train, y_train)

# ---- Save model & tools ----
pickle.dump(svm, open("model/svm_model.pkl", "wb"))
pickle.dump(scaler, open("model/scaler.pkl", "wb"))
pickle.dump(label_enc, open("model/label_encoder.pkl", "wb"))

print("✅ Model trained and saved successfully")
