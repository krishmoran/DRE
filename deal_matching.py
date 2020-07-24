import pandas as pd
from numerize import numerize
# slider for min-max investment


def match_deal(industry, issuance_type, country, min_invest, max_invest):
    # INPUT THIS FILENAME MANUALLY FOR NOW
    filename = "C:/Users/Krish/Documents/GitHub/The-Great-Auto-Suggester/Mock_Deal_Database1.csv"
    df = pd.read_csv(filename)
    currency_type = min_invest[:1]

    # Convert everything to lowercase
    df = df.applymap(lambda s: s.lower() if type(s) == str else s)

    # Configure Pandas display options
    pd.set_option('mode.chained_assignment', None)
    pd.options.display.width = 0

    df['Target Raise'] = df['Target Raise'].apply(lambda x: (normalize(x) if x != "n/a" else x))


    # Handling when the user decides to leave an input blank for their query
    if industry != "":
        indust = (df['Industry Type'] == industry.lower())
    else:
        indust = True

    if issuance_type != "":
        issuance = (df['Issuance Type'] == issuance_type.lower())
    else:
        issuance = True

    if country != "":
        loc = (df["Location"] == country.lower())
    else:
        loc = True

    if min_invest != "":
        min_investment = normalize(min_invest.lower())
        min = (df['Target Raise'] > min_investment)
    else:
        min = True

    if max_invest != "":
        max_investment = normalize(max_invest.lower())
        max = (df['Target Raise'] <= max_investment)
    else:
        max = True



    # formats the visual output of the dataframe
    output_df = df[indust & issuance & loc & min & max]
    output_df['Target Raise'] = output_df['Target Raise'].apply(lambda x: currency_type + (numerize.numerize(x) if x != "n/a" else x))


    if output_df.empty:
        print("No results. Please tweak your search criteria.")

    print(output_df)
    return(output_df)


# takes the string amount value in form e.g. "$500k", and will convert to raw format -> 500,000
def normalize(amount_text, bad_data_val=0):
    d = {
        'k': 1000,
        'm': 1000000,
        'b': 1000000000
    }
    if not isinstance(amount_text, str):
        # Non-strings are bad are missing data in poster's submission
        return bad_data_val

    elif amount_text[-1] in d:
        # separate out the K, M, or B
        num, magnitude = amount_text[:-1], amount_text[-1]
        return int(float(num[1:]) * d[magnitude])
    else:
        return float(amount_text[1:])


# PARAMETERS: match_deal(industry, issuance type, country, minimum investment, maximum investment)
# * Empty strings as an input will disregard the certain field as a filter
match_deal("", "", "USA", "$1M", "$5M")








