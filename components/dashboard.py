import streamlit as st
import pandas as pd
import altair as alt

def dashboard(purchases):
    st.markdown("""
    <div style='background: #264027; border-radius: 14px; padding: 18px; margin-bottom: 10px;'>
        <h2 style='color: #e9c46a; font-size: 2em;'>Dashboard 📊</h2>
    </div>
    """, unsafe_allow_html=True)
    if purchases.empty:
        st.warning("No purchases logged yet.")
        return
    purchases["Timestamp"] = pd.to_datetime(purchases["Timestamp"])
    purchases["Month"] = purchases["Timestamp"].dt.to_period("M")
    monthly = purchases.groupby("Month").agg({"Price": "sum", "CO2_kg": "sum"}).reset_index()
    st.markdown("<h3 style='color: #f4a261; border-radius:24px; background:#4b4637; padding:10px;'>Monthly Summary</h3>", unsafe_allow_html=True)
    st.dataframe(monthly, use_container_width=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 style='color: #b7c68b; border-radius:24px; background:#4b4637; padding:10px;'>CO₂ by Category</h3>", unsafe_allow_html=True)
        chart = alt.Chart(purchases).mark_bar().encode(
            x=alt.X("Category", axis=alt.Axis(labelColor="#e6d7b2", titleColor="#e6d7b2")),
            y=alt.Y("CO2_kg", axis=alt.Axis(labelColor="#e6d7b2", titleColor="#e6d7b2")),
            color=alt.Color("Category", scale=alt.Scale(scheme="dark2"))
        ).properties(width=300, height=350, background="#2d2a26")
        st.altair_chart(chart, use_container_width=True)
    with col2:
        st.markdown("<h3 style='color: #b7c68b; border-radius:24px; background:#4b4637; padding:10px;'>Spending Over Time</h3>", unsafe_allow_html=True)
        line_chart = alt.Chart(purchases).mark_line(point=True).encode(
            x=alt.X("Timestamp", axis=alt.Axis(labelColor="#e6d7b2", titleColor="#e6d7b2")),
            y=alt.Y("Price", axis=alt.Axis(labelColor="#e6d7b2", titleColor="#e6d7b2")),
            color=alt.Color("Category", scale=alt.Scale(scheme="dark2"))
        ).properties(width=300, height=350, background="#2d2a26")
        st.altair_chart(line_chart, use_container_width=True)
