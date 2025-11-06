import streamlit as st
import os
import io
from PIL import Image, ImageDraw, ImageFont

def badge_display(purchases):
    st.markdown("""
    <div style='background: #264027; border-radius: 14px; padding: 18px; margin-bottom: 10px;'>
        <h2 style='color: #e9c46a; font-size: 2em;'>Your Badges 🏅</h2>
    </div>
    """, unsafe_allow_html=True)
    eco_saver = False
    low_impact = False
    badge_count = len(purchases) // 5 if not purchases.empty else 0
    # Example criteria
    if not purchases.empty:
        avg_co2 = purchases["CO2_kg"].mean()
        food_count = (purchases["ProductType"] == "Food").sum() if "ProductType" in purchases.columns else 0
        if avg_co2 < 0.5:
            eco_saver = True
        if food_count >= 3:
            low_impact = True
    st.markdown(f"<span style='color: #f4a261; font-size: 1.3em;'>You've earned {badge_count} badge(s)!</span>", unsafe_allow_html=True)
    badge_images = []
    # Use st.badge if available (Streamlit v1.50+)
    try:
        if eco_saver:
            st.badge("Eco Saver", color="#b7c68b", icon="🌱")
        if low_impact:
            st.badge("Low Impact Shopper", color="#a3b18a", icon="🛒")
        if badge_count > 0:
            st.badge("Eco Hero", color="#f4a261", icon="🏅")
    except Exception:
        # Fallback to markdown if st.badge not available
        if eco_saver:
            st.markdown("<h4 style='color: #e9c46a;'>Eco Saver Badge 🌱</h4>", unsafe_allow_html=True)
        if low_impact:
            st.markdown("<h4 style='color: #e9c46a;'>Low Impact Shopper Badge 🛒</h4>", unsafe_allow_html=True)
        if badge_count > 0:
            st.markdown("<h4 style='color: #e9c46a;'>Eco Hero Badge 🏅</h4>", unsafe_allow_html=True)
    # Generate badge images using PIL (headless)
    def draw_badge(btype):
        width, height = 120, 120
        img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        # background circle
        if btype == "Eco Saver":
            draw.ellipse((10, 10, 110, 110), fill=(183,198,139,255))
            draw.text((60, 45), "🌱", anchor="mm", fill=(75,70,55,255), font=ImageFont.load_default())
        elif btype == "Low Impact Shopper":
            draw.ellipse((10, 10, 110, 110), fill=(163,177,138,255))
            draw.text((60, 45), "🛒", anchor="mm", fill=(75,70,55,255), font=ImageFont.load_default())
        else:
            draw.ellipse((10, 10, 110, 110), fill=(244,162,97,255))
            draw.text((60, 45), "🏅", anchor="mm", fill=(75,70,55,255), font=ImageFont.load_default())
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        return buf.getvalue()
    if eco_saver:
        badge_images.append(draw_badge("Eco Saver"))
    if low_impact:
        badge_images.append(draw_badge("Low Impact Shopper"))
    if badge_count > 0:
        badge_images.append(draw_badge("Eco Hero"))
    if badge_images:
        import base64
        st.markdown("<div style='display:flex; gap:16px;'>", unsafe_allow_html=True)
        for img_bytes in badge_images:
            b64_img = base64.b64encode(img_bytes).decode()
            st.markdown(f"<img src='data:image/png;base64,{b64_img}' width='80' style='border-radius:24px;' />", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    if not (eco_saver or low_impact or badge_count > 0):
        st.info("Log more purchases to earn badges!")
