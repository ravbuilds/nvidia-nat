import pandas as pd

def build_dataset():
    df = pd.read_csv("real_estate.csv")
    dataset = []

    for _, r in df.iterrows():
        prompt = f"""
        Estimate the market price and explain:
        City: {r.city}
        Sqft: {r.sqft}
        Beds: {r.bedrooms}
        Baths: {r.bathrooms}
        Year Built: {r.year}
        """

        answer = f"""
        Estimated Price: ${int(r.price)}
        Price per sqft: ${int(r.price_per_sqft)}
        """

        dataset.append({"input": prompt, "output": answer})

    return dataset