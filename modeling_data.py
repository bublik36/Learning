import numpy as np
import get_data as main_data
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

df = main_data.df()

print(df)


def create_model(data, thing):
    returned_text = thing + " купят с вероятностью: "
    category_x = np.array(data["category"])
    price_y = np.array(data["buying_mean"])
    vectorizer = TfidfVectorizer()
    X_text = vectorizer.fit_transform(category_x)
    x_train, x_test, y_train, y_test = train_test_split(
        X_text, price_y, test_size=0.3, random_state=42
    )
    lr = LogisticRegression().fit(x_train, y_train)
    print(
        "\n"
        + "Модель работает с вероятностью ошибки: "
        + str(mean_absolute_error(lr.predict(x_test), y_test))
    )
    return (
        returned_text
        + str(lr.predict_proba(vectorizer.transform([thing]))[0][1])[2:4]
        + "%"
    )
