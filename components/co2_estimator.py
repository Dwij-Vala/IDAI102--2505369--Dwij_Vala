import streamlit as st

def co2_estimator(purchases):
    st.markdown("""
    <div style='background: #264027; border-radius: 14px; padding: 18px; margin-bottom: 10px;'>
        <h2 style='color: #e9c46a; font-size: 2em;'>CO₂ Estimator 🌍</h2>
        <p style='color: #f4a261;'>Estimate the CO₂ impact of your purchases.</p>
    </div>
    """, unsafe_allow_html=True)
    total_co2 = purchases["CO2_kg"].sum() if not purchases.empty else 0
    st.metric("Total CO₂ (kg)", f"{total_co2:.2f}")
    st.markdown(f"<span style='color: #f4a261; font-size: 1.3em;'>Average per purchase: {purchases['CO2_kg'].mean():.2f}</span>" if not purchases.empty else "<span style='color: #f4a261; font-size: 1.3em;'>Average per purchase: 0.00</span>", unsafe_allow_html=True)
