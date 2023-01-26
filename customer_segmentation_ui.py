# streamlit_app.py

import streamlit as st
from snowflake.snowpark.session import Session
import pandas as pd
import numpy as np
import plotly.express as px

# Snowflake connection info is saved in config.py
# from config import snowflake_conn_prop

# Initialize connection.
# Uses st.experimental_singleton to only run once.
# session = Session.builder.configs(snowflake_conn_prop).create()

def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()

session = Session.builder.configs(connection=conn).create() 

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.

df = session.table("RFM_Clusters")

df_pd = df.to_pandas()

st.write("Hello")

st.write(df_pd.size)

st.dataframe(df_pd)

fig = px.scatter(
    df_pd,
    x="FREQUENCY",
    y="RECENCY",
    color="Cluster"
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)




