import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Market Basket Analysis",
    layout="wide"
)

st.title("🛒 Market Basket Analysis")

st.write(
    "Association Rule Mining for Upselling and Cross Selling"
)

rules = pd.read_csv("association_rules.csv")

st.subheader("Association Rules")

st.dataframe(rules)

top_rules = rules.sort_values(
    by="lift",
    ascending=False
).head(10)

st.subheader("Top 10 Rules")

st.dataframe(top_rules)

st.subheader("Business Insights")

for index, row in top_rules.iterrows():

    st.write(
        f"If customer buys {row['antecedents']} "
        f"they are likely to buy {row['consequents']}"
    )

st.success("Analysis Completed Successfully")