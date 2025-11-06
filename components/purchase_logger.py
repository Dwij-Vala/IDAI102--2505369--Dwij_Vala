import streamlit as st
import pandas as pd
from datetime import datetime

def purchase_logger(purchases, data_path):
    import streamlit.components.v1 as components
    import base64
    import io
    from PIL import Image, ImageDraw, ImageFont
    import random
    st.markdown("""
    <div style='background: #264027; border-radius: 14px; padding: 18px; margin-bottom: 10px;'>
        <h2 style='color: #e9c46a; font-size: 2em;'>Log a Purchase 🛒</h2>
    </div>
    """, unsafe_allow_html=True)
    item = st.text_input("📝 Item Name", "", key="item")
    product_type = st.selectbox("🛍️ Product Type", ["Food", "Clothing", "Electronics", "Other"], key="product_type")
    brand = st.text_input("🏷️ Brand", "", key="brand")
    price = st.number_input("💲 Price ($)", min_value=0.0, format="%.2f", key="price")
    # Real-time CO₂ calculation based on product type and price
    co2_factors = {
        "Food": 0.5,           # 0.5 kg CO₂ per $ spent
        "Clothing": 0.3,       # 0.3 kg CO₂ per $ spent
        "Electronics": 1.2,    # 1.2 kg CO₂ per $ spent
        "Other": 0.7           # 0.7 kg CO₂ per $ spent
    }
    co2_kg = round(price * co2_factors.get(product_type, 0.7), 2)
    st.info(f"Estimated CO₂ impact: {co2_kg} kg (Factor: {co2_factors.get(product_type, 0.7)} kg CO₂/$)")
    st.markdown("<small style='color:#f4a261;'>CO₂ factors: Food=0.5, Clothing=0.3, Electronics=1.2, Other=0.7 (kg CO₂ per $)</small>", unsafe_allow_html=True)
    if st.button("✨ Add Purchase", key="add_purchase"):
        new_row = {"Item": item, "ProductType": product_type, "Brand": brand, "Category": product_type, "Price": price, "CO2_kg": co2_kg, "Timestamp": datetime.now()}
        # pandas.DataFrame.append was removed in pandas 2.x; use concat instead
        purchases = pd.concat([purchases, pd.DataFrame([new_row])], ignore_index=True)
        purchases.to_csv(data_path, index=False)
        st.success(f"Added {item} to purchases!")
        # Suggest greener alternatives
        alternatives = {
            "Food": "Try more plant-based or local foods 🌱",
            "Clothing": "Choose organic cotton or recycled materials ♻️",
            "Electronics": "Look for energy-efficient or refurbished options 💡",
            "Other": "Consider reusable or low-impact alternatives 🌿"
        }
        st.info(f"Greener alternative: {alternatives.get(product_type, 'Explore eco-friendly options!')}")
        # Headless badge/graphic drawing using PIL (avoids tkinter/turtle GUI)
        def draw_graphic(ptype):
            width, height = 200, 200
            img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            # base circle/background
            draw.ellipse((20, 20, 180, 180), fill=(75, 70, 55, 255))
            if ptype == "Food":
                # footprint: draw big oval + three toes
                draw.ellipse((70, 90, 130, 140), fill=(58, 90, 64, 255))
                draw.ellipse((50, 60, 70, 80), fill=(58, 90, 64, 255))
                draw.ellipse((90, 50, 110, 70), fill=(58, 90, 64, 255))
                draw.ellipse((120, 60, 140, 80), fill=(58, 90, 64, 255))
            elif ptype == "Clothing":
                # badge: circle with ribbon-like rectangle
                draw.ellipse((50, 30, 150, 130), fill=(233, 196, 106, 255))
                draw.rectangle((85, 120, 95, 170), fill=(233, 196, 106, 255))
            elif ptype == "Electronics":
                # leaf: simple polygon
                draw.polygon([(100, 40), (140, 100), (100, 160), (60, 100)], fill=(167, 177, 138, 255))
            else:
                draw.ellipse((70, 60, 130, 120), fill=(244, 162, 97, 255))
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            return buf.getvalue()
import streamlit as st
import pandas as pd
from datetime import datetime

def purchase_logger(purchases, data_path):
    import streamlit.components.v1 as components
    import base64
    import io
    from PIL import Image, ImageDraw, ImageFont
    import random
    st.markdown("""
    <div style='background: #264027; border-radius: 14px; padding: 18px; margin-bottom: 10px;'>
        <h2 style='color: #e9c46a; font-size: 2em;'>Log a Purchase 🛒</h2>
    </div>
    """, unsafe_allow_html=True)
    item = st.text_input("📝 Item Name", "", key="item")
    product_type = st.selectbox("🛍️ Product Type", ["Food", "Clothing", "Electronics", "Other"], key="product_type")
    brand = st.text_input("🏷️ Brand", "", key="brand")
    price = st.number_input("💲 Price ($)", min_value=0.0, format="%.2f", key="price")
    # Real-time CO₂ calculation based on product type and price
    co2_factors = {
        "Food": 0.5,           # 0.5 kg CO₂ per $ spent
        "Clothing": 0.3,       # 0.3 kg CO₂ per $ spent
        "Electronics": 1.2,    # 1.2 kg CO₂ per $ spent
        "Other": 0.7           # 0.7 kg CO₂ per $ spent
    }
    co2_kg = round(price * co2_factors.get(product_type, 0.7), 2)
    st.info(f"Estimated CO₂ impact: {co2_kg} kg (Factor: {co2_factors.get(product_type, 0.7)} kg CO₂/$)")
    st.markdown("<small style='color:#f4a261;'>CO₂ factors: Food=0.5, Clothing=0.3, Electronics=1.2, Other=0.7 (kg CO₂ per $)</small>", unsafe_allow_html=True)
    if st.button("✨ Add Purchase", key="add_purchase"):
        new_row = {"Item": item, "ProductType": product_type, "Brand": brand, "Category": product_type, "Price": price, "CO2_kg": co2_kg, "Timestamp": datetime.now()}
        # pandas.DataFrame.append was removed in pandas 2.x; use concat instead
        purchases = pd.concat([purchases, pd.DataFrame([new_row])], ignore_index=True)
        purchases.to_csv(data_path, index=False)
        st.success(f"Added {item} to purchases!")
        # Suggest greener alternatives
        alternatives = {
            "Food": "Try more plant-based or local foods 🌱",
            "Clothing": "Choose organic cotton or recycled materials ♻️",
            "Electronics": "Look for energy-efficient or refurbished options 💡",
            "Other": "Consider reusable or low-impact alternatives 🌿"
        }
        st.info(f"Greener alternative: {alternatives.get(product_type, 'Explore eco-friendly options!')}")
        # Headless badge/graphic drawing using PIL (avoids tkinter/turtle GUI)
        def draw_graphic(ptype):
            width, height = 200, 200
            img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            # base circle/background
            draw.ellipse((20, 20, 180, 180), fill=(75, 70, 55, 255))
            if ptype == "Food":
                # footprint: draw big oval + three toes
                draw.ellipse((70, 90, 130, 140), fill=(58, 90, 64, 255))
                draw.ellipse((50, 60, 70, 80), fill=(58, 90, 64, 255))
                draw.ellipse((90, 50, 110, 70), fill=(58, 90, 64, 255))
                draw.ellipse((120, 60, 140, 80), fill=(58, 90, 64, 255))
            elif ptype == "Clothing":
                # badge: circle with ribbon-like rectangle
                draw.ellipse((50, 30, 150, 130), fill=(233, 196, 106, 255))
                draw.rectangle((85, 120, 95, 170), fill=(233, 196, 106, 255))
            elif ptype == "Electronics":
                # leaf: simple polygon
                draw.polygon([(100, 40), (140, 100), (100, 160), (60, 100)], fill=(167, 177, 138, 255))
            else:
                draw.ellipse((70, 60, 130, 120), fill=(244, 162, 97, 255))
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            return buf.getvalue()

        try:
            img_bytes = draw_graphic(product_type)
            b64_img = base64.b64encode(img_bytes).decode()
            st.markdown(f"<img src='data:image/png;base64,{b64_img}' width='120' style='border-radius:16px;' />", unsafe_allow_html=True)
        except Exception:
            st.warning("Eco graphic could not be displayed.")
        # Random eco tip (shown after each purchase)
        eco_tips = [
            "Did you know bamboo has a lower footprint than plastic? 🎋",
            "Switching to LED bulbs saves energy and CO₂! 💡",
            "Reusable bags reduce waste and emissions. 🛍️",
            "Eating local food cuts transport emissions. 🚚",
            "Repairing items extends their life and lowers impact. 🔧"
        ]
        st.info(f"Eco Tip: {random.choice(eco_tips)}")
    st.markdown("<h3 style='color: #f4a261;'>Your Purchases</h3>", unsafe_allow_html=True)
    st.dataframe(purchases, width='stretch')
