import streamlit as st

def mindful_reflection():
    st.markdown("""
    <div style='background: #264027; border-radius: 14px; padding: 18px; margin-bottom: 10px;'>
        <h2 style='color: #e9c46a; font-size: 2em;'>Mindful Reflection 🧘</h2>
        <p style='color: #f4a261;'>Take a moment to reflect on your shopping habits.</p>
    </div>
    """, unsafe_allow_html=True)
    reflection = st.text_area("How did your purchases make you feel? Any eco-friendly changes you'd like to try next time?", "")
    if st.button("🌿 Save Reflection"):
        st.success("Reflection saved! 🌿")
