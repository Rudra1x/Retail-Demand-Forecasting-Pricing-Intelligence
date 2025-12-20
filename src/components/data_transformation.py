class DataTransformation:
    def transform(self, df):
        df["date"] = pd.to_datetime(df["date"])
        return df
