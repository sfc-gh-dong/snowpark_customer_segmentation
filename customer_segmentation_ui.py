import streamlit as st
import snowflake.connector
from snowflake.snowpark.session import Session
import pandas as pd
import numpy as np
import plotly.express as px

# Initialize connection.
# Refer to https://docs.streamlit.io/knowledge-base/tutorials/databases/snowflake for format of secrets
session = Session.builder.configs(st.secrets["snowflake"]).create()

# Perform query.
st.header('Customer Segmentation example with Snowpark using K-Means')

st.write('Sample cluster data that shows the recency, frequency and monetary attributes of each customer')
df = session.table("RFM_Clusters")
df_pd = df.to_pandas()
st.dataframe(df_pd)
df_pd["Cluster"] = df_pd["Cluster"].astype(str)

st.subheader('Frequency vs Recency')

fig = px.scatter(
    df_pd,
    x="FREQUENCY",
    y="RECENCY",
    color="Cluster",
    opacity=0.5
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

st.subheader('Frequency vs Monetary')

fig = px.scatter(
    df_pd,
    x="FREQUENCY",
    y="MONETARY",
    color="Cluster",
    opacity=0.5
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

st.subheader('Recency vs Monetary')

fig = px.scatter(
    df_pd,
    x="RECENCY",
    y="MONETARY",
    color="Cluster",
    opacity=0.5
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)

st.markdown("**:red[Cluster 3]** are your Loyalists. They generally spend more money and more frequently.")
st.markdown("**:blue[Cluster 1]** are your Growing customers. They spend less money and less frequently, but they spent in the last 5 months.")
st.markdown("**:orange[Cluster 2]** are your Churning customers. They spend less money and less frequently, and they spent beyond the last 5 months.")
st.markdown("**Cluster** **0** sit somewhere in between.")
