import streamlit as st

def eco_suggestions(purchases):
    st.markdown("""
    <div style='background: #264027; border-radius: 14px; padding: 18px; margin-bottom: 10px;'>
        <h2 style='color: #e9c46a; font-size: 2em;'>Eco Suggestions 🌱</h2>
        <p style='color: #f4a261;'>Here are some ways to reduce your impact:</p>
    </div>
    """, unsafe_allow_html=True)
    suggestions = [
        "Buy local and seasonal products 🥕",
        "Choose reusable over disposable ♻️",
        "Opt for energy-efficient electronics 💡",
        "Repair instead of replace 🔧",
        "Use public transport or bike 🚲"
    ]
    st.markdown("\n".join([f"<span style='color: #e9c46a; font-size: 1.2em;'>• {s}</span>" for s in suggestions]), unsafe_allow_html=True)
    if not purchases.empty:
        st.markdown("<h4 style='color: #f4a261;'>Based on your purchases:</h4>", unsafe_allow_html=True)
        if (purchases["Category"] == "Food").any():
            st.info("Try plant-based meals for lower CO₂!")
        if (purchases["Category"] == "Electronics").any():
            st.info("Recycle old electronics responsibly.")
