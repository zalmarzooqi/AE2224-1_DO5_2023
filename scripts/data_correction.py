from commonimports import *


# Function Definition
def data_correction(df):

    # Set which columns need to be corrected
    corrected_columns = ["Perim.", "Circ.", "Feret", "FeretX", "FeretY",
                         "FeretAngle", "MinFeret", "AR", "Round", "Solidity"]

    # Iterate over the different rows in the dataframe
    for i, row in enumerate(df.values):

        # Iterate over the different columns in the dataframe
        for j, col in enumerate(df.columns):

            # Check whether the column needs to be corrected
            if col in corrected_columns:

                # Check if value needs to be corrected
                val = df.loc[i][j]
                if val >= 1:

                    # Correct value
                    val = val / 1000
                    df.iat[i, j] = val


if __name__ == "__main__":
    df = pd.DataFrame([[0.1, 0.1, 0.1, 0.1],
                       [200, 0.1, 0.1, 0.1],
                       [0.1, 0.1, 200, 0.1],
                       [0.1, 200, 0.1, 0.1]],
                      columns=["Area", "Circ.", "FeretX", "FeretY"])
    data_correction(df)
    print(df)
