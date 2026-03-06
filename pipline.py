import pandas as pd

# används för train/test split
from sklearn.model_selection import train_test_split

# preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

# används för att applicera olika preprocessing på olika kolumner
from sklearn.compose import ColumnTransformer

# pipeline kopplar ihop preprocessing i ett workflow
from sklearn.pipeline import Pipeline

from sklearn.impute import SimpleImputer


# ==================================
# behöver vet vi gör med null värden
# ==================================


def train_test_split_for_model(df: pd.DataFrame, traget_collum = "is_suspicious" ): #returns X_train, X_test, y_train, y_test
    y = df[traget_collum]
    X = X.drop(columns=["id"])
    X = df.drop(columns=[traget_collum])
    
    X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,     # 80% train, 20% test
    stratify=y,        # viktigt för klassificering
    random_state=42    # gör experiment reproducerbart
    )
    
    return X_train, X_test, y_train, y_test

def preprosseing():
    
    numeric_features = [
    "day",
    "account_age_days",
    "num_prev_listings",
    "prev_reports_30d",
    "price",
    "num_images",
    "verification_level",
    "contains_off_platform",
    "urgency_words",
    "payment_attempt",
    "message_length",
    "time_to_first_response_min"]

    categorical_features = [
    
    "event_type",
    "category",
    "region",
    "device"
   ]
    # fall om nya kategorier lägg tills vvv
    OneHotEncoder(handle_unknown="ignore")
    # ^^^^^^^^
    numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
    ])

    categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features)
        ]
    )
    return preprocessor

def create_pipeline(preprocessor):
    pipeline = Pipeline([
    ("preprocessing", preprocessor)
    ])
    return pipeline

def fit_train_pipeline(pipeline:Pipeline, X_train,X_test):
    pipeline.fit(X_train)
    X_train_processed = pipeline.transform(X_train)
    X_test_processed = pipeline.transform(X_test)
    return X_train_processed ,X_test_processed
        
if __name__ == "__main__":
    path = "data/historical_data.csv"
    df = pd.read_csv(path)
    