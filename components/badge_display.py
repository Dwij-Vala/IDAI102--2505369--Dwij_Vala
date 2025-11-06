import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import base64

def draw_badge(badge_type):
    # Create a new image with a transparent background
    width, height = 200, 200
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw badge circle
    circle_color = {
        'Eco Saver': '#2ecc71',
        'Low Impact': '#3498db',
        'Green Elite': '#9b59b6',
        'Earth Guardian': '#f1c40f'
    }.get(badge_type, '#95a5a6')
    
    # Draw the outer circle
    draw.ellipse([10, 10, width-10, height-10], fill=circle_color)
    
    # Try to load a font, fallback to default if not found
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()

    # Add badge text
    text_bbox = draw.textbbox((0, 0), badge_type, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(text_position, badge_type, fill='white', font=font)

    # Convert to base64 for displaying in streamlit
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

def badge_display(purchases):
    st.markdown("""
    <div style='background: #264027; border-radius: 14px; padding: 18px; margin-bottom: 10px;'>
        <h2 style='color: #e9c46a; font-size: 2em;'>Your Eco Badges 🏅</h2>
        <p style='color: #f4a261;'>Earn badges for your eco-friendly shopping!</p>
    </div>
    """, unsafe_allow_html=True)

    if purchases.empty:
        st.info("Start making purchases to earn eco badges! 🌱")
        return

    # Calculate badge criteria
    avg_co2 = purchases["CO2_kg"].mean()
    total_purchases = len(purchases)
    food_purchases = len(purchases[purchases["Category"] == "Food"])
    
    # Define badge conditions
    badges_earned = []
    if avg_co2 < 0.5:
        badges_earned.append("Eco Saver")
    if food_purchases >= 3:
        badges_earned.append("Low Impact")
    if total_purchases >= 10 and avg_co2 < 0.7:
        badges_earned.append("Green Elite")
    if total_purchases >= 20 and avg_co2 < 0.4:
        badges_earned.append("Earth Guardian")

    if not badges_earned:
        st.info("Keep making eco-conscious choices to earn badges! 🌱")
        return

    # Display badges in a horizontal layout
    cols = st.columns(len(badges_earned))
    for col, badge in zip(cols, badges_earned):
        with col:
            badge_image = draw_badge(badge)
            st.markdown(f"""
                <div style='text-align: center;'>
                    <img src='{badge_image}' style='width: 150px;'>
                    <p style='color: #e9c46a; margin-top: 10px;'>{badge}</p>
                </div>
            """, unsafe_allow_html=True)