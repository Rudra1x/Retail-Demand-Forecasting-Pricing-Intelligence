import great_expectations as ge

class DataValidation:
    def validate(self, df):
        ge_df = ge.from_pandas(df)

        ge_df.expect_column_values_to_not_be_null("date")
        ge_df.expect_column_values_to_be_between("units_sold", min_value=0)
        ge_df.expect_column_values_to_not_be_null("sell_price")

        result = ge_df.validate()
        if not result["success"]:
            raise Exception("Data validation failed")

        return True
