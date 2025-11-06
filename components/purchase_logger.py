import streamlit as st
import pandas as pd
from datetime import datetime
import base64
import io
from PIL import Image, ImageDraw, ImageFont

def draw_graphic(product_type):
    """Draw and return a base64 encoded PNG for the given product type."""
    width, height = 300, 180
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw a simple graphic based on product type
    if product_type == 'Food':
        draw.ellipse([130, 70, 170, 110], outline='#2ecc71', width=3)
        draw.line([(150, 90), (150, 130)], fill='#2ecc71', width=3)
        draw.line([(150, 90), (180, 110)], fill='#2ecc71', width=3)
        draw.line([(150, 90), (120, 110)], fill='#2ecc71', width=3)
    elif product_type == 'Electronics':
        draw.rectangle([120, 70, 180, 110], outline='#3498db', width=3)
        draw.line([(130, 80), (170, 80)], fill='#3498db', width=3)
        draw.line([(130, 90), (170, 90)], fill='#3498db', width=3)
        draw.line([(130, 100), (170, 100)], fill='#3498db', width=3)
    elif product_type == 'Clothing':
        draw.arc([120, 70, 180, 90], 0, 180, fill='#e74c3c', width=3)
        draw.line([(120, 80), (120, 110)], fill='#e74c3c', width=3)
        draw.line([(180, 80), (180, 110)], fill='#e74c3c', width=3)
    else:
        draw.rectangle([120, 70, 180, 110], outline='#95a5a6', width=3)
        draw.line([(130, 80), (170, 100)], fill='#95a5a6', width=3)
        draw.line([(130, 100), (170, 80)], fill='#95a5a6', width=3)
    
    # Convert to base64
    buffered = io.BytesIO()
    image.save(buffered, format='PNG')
    return base64.b64encode(buffered.getvalue()).decode()

def purchase_logger(purchases, data_path):
    """Log purchase information and calculate environmental impact."""
    st.markdown("""
        <style>
        .purchase-form {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="purchase-form">', unsafe_allow_html=True)
    
    item = st.text_input('Item Name 🛍️')
    
    col1, col2 = st.columns(2)
    
    with col1:
        category = st.selectbox(
            'Category 📦',
            ['Food', 'Electronics', 'Clothing', 'Other']
        )
        
        price = st.number_input(
            'Price 💰',
            min_value=0.0,
            help='Enter the price you paid'
        )
    
    with col2:
        date = st.date_input(
            'Purchase Date 📅',
            datetime.now()
        )
        
        necessity = st.slider(
            'Necessity Level 🎯',
            0, 10, 5,
            help='Rate how necessary this purchase was (0: Not at all, 10: Essential)'
        )
    
    # CO2 impact factors (kg CO2 per currency unit)
    CO2_FACTORS = {
        'Food': 0.5,
        'Electronics': 1.2,
        'Clothing': 0.3,
        'Other': 0.7
    }
    
    submit = st.button('Log Purchase 📝')
    
    if submit and item and price > 0:
        # Calculate CO2 impact
        co2_impact = price * CO2_FACTORS[category]
        
        # Create new purchase entry
        new_purchase = {
            'Date': date.strftime('%Y-%m-%d'),
            'Item': item,
            'Category': category,
            'Price': price,
            'Necessity': necessity,
            'CO2_Impact': co2_impact
        }
        
        # Update purchases DataFrame
        purchases = pd.concat([purchases, pd.DataFrame([new_purchase])], ignore_index=True)
        purchases.to_csv(data_path, index=False)
        
        # Show success message with environmental impact
        st.markdown("""
            <div style='padding: 20px; background-color: #d4edda; border-radius: 5px; margin: 10px 0;'>
                <h3 style='color: #155724; margin: 0;'>✅ Purchase Logged Successfully!</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Show environmental impact
        st.markdown(f"""
            <div style='background-color: #e8f4f8; padding: 15px; border-radius: 5px; margin: 10px 0;'>
                <h4 style='color: #2c3e50; margin: 0;'>Environmental Impact 🌍</h4>
                <p style='color: #34495e; margin: 10px 0;'>
                    This purchase contributed approximately {co2_impact:.2f} kg of CO2 to your carbon footprint.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Display category-specific eco-friendly tips
        if category == 'Food':
            eco_tips = [
                'Consider buying local produce to reduce transportation emissions 🚛',
                'Try bringing your own reusable bags next time! 🛍️',
                'Look for products with minimal packaging 📦'
            ]
        elif category == 'Electronics':
            eco_tips = [
                'Remember to recycle your old electronics properly ♻️',
                'Consider energy-efficient alternatives 💡',
                'Look for products with good longevity ratings 🔋'
            ]
        elif category == 'Clothing':
            eco_tips = [
                'Consider second-hand or vintage options next time 👕',
                'Look for sustainable fabric choices 🧵',
                'Choose quality items that will last longer 👔'
            ]
        else:
            eco_tips = [
                'Consider if you can borrow or rent instead of buying 🤝',
                'Look for products made from recycled materials ♻️',
                'Research eco-friendly alternatives 🌱'
            ]
        
        # Display a random eco-tip
        import random
        tip = random.choice(eco_tips)
        
        st.markdown(f"""
            <div style='background-color: #fff3cd; padding: 15px; border-radius: 5px; margin: 10px 0;'>
                <h4 style='color: #856404; margin: 0;'>Eco-Friendly Tip 💡</h4>
                <p style='color: #856404; margin: 10px 0;'>{tip}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Display product icon
        img_b64 = draw_graphic(category)
        st.markdown(f"""
            <div style='text-align: center; margin: 20px 0;'>
                <img src='data:image/png;base64,{img_b64}' style='max-width: 150px;'>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)
    
    return purchases