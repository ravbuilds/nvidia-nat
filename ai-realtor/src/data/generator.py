import pandas as pd
import numpy as np

def generate(n=5000):
    cities = ["San Jose", "Austin", "Seattle", "Denver", "Miami", "NYC", "SF"]

    df = pd.DataFrame({
        "city": np.random.choice(cities, n),
        "sqft": np.random.randint(500, 4000, n),
        "bedrooms": np.random.randint(1, 6, n),
        "bathrooms": np.random.randint(1, 5, n),
        "year": np.random.randint(1960, 2024, n),
        "price": np.random.randint(200000, 2000000, n)
    })

    df["price_per_sqft"] = df["price"] / df["sqft"]
    df.to_csv("real_estate.csv", index=False)

if __name__ == "__main__":
    generate()