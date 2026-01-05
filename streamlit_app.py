# Compare and Save - Streamlit Price Comparison App
import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Compare and Save",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom font imports
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Lilita+One&display=swap" rel="stylesheet">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inconsolata&display=swap');
</style>
""", unsafe_allow_html=True)

# Title
st.title("💰 Compare and Save")
st.markdown("**Weekly Price Comparison Tool** — Generate printable comparison cards")

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    competitor = st.radio(
        "Which competitor are you comparing?",
        ["Winco", "Safeway/Albertsons"],
        help="Choose which competitor to generate cards for"
    )
    
    check_date = st.date_input(
        "Price Check Date",
        value=datetime.today(),
        help="Date to display on cards"
    )

# Main content tabs
tab1, tab2, tab3 = st.tabs(["📊 Input Data", "👁️ Preview", "🖨️ Print"])

with tab1:
    st.header("Enter Product Prices")
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        num_products = st.number_input(
            "How many products?",
            min_value=1,
            max_value=100,
            value=10,
            help="Add/remove products as needed"
        )
    
    with col1:
        st.markdown("**Pricing Data**")
    
    # Create column headers
    header_cols = st.columns([3, 1.5, 1.5, 1])
    with header_cols[0]:
        st.markdown("**Product Name**")
    with header_cols[1]:
        st.markdown("**Super 1 Price**")
    with header_cols[2]:
        st.markdown("**Competitor Price**")
    with header_cols[3]:
        st.markdown("**Carries?**")
    
    # Create input form for products
    products_data = []
    
    for i in range(num_products):
        col1, col2, col3, col4 = st.columns([3, 1.5, 1.5, 1])
        
        with col1:
            product_name = st.text_input(
                "Product Name",
                key=f"product_{i}",
                label_visibility="collapsed",
                placeholder=f"Product {i+1}"
            )
        
        with col2:
            super_one_price = st.number_input(
                "Super 1",
                min_value=0.0,
                step=0.01,
                key=f"super1_{i}",
                label_visibility="collapsed",
                format="%.2f"
            )
        
        with col3:
            competitor_price = st.number_input(
                "Competitor",
                min_value=0.0,
                step=0.01,
                key=f"competitor_{i}",
                label_visibility="collapsed",
                format="%.2f"
            )
        
        with col4:
            carries = st.selectbox(
                "Carries?",
                ["Yes", "DNC"],
                key=f"carries_{i}",
                label_visibility="collapsed"
            )
        
        if product_name:  # Only add if product name is filled
            products_data.append({
                'product': product_name,
                'super_one': super_one_price,
                'competitor': competitor_price,
                'carries': carries
            })
    
    # Add instructions
    st.info(
        "💡 **How to use:**\n"
        "1. Enter product names and prices\n"
        "2. Select 'DNC' (Does Not Carry) if the competitor doesn't have the item\n"
        "3. Go to 'Preview' tab to see how cards will look\n"
        "4. Use 'Print' tab to print or export"
    )

with tab2:
    st.header("Preview Cards")
    
    if not products_data:
        st.warning("No products entered yet. Go to 'Input Data' tab to add products.")
    else:
        # Filter valid comparisons
        valid_comparisons = []
        dnc_products = []
        
        for item in products_data:
            if item['carries'] == 'DNC':
                dnc_products.append(item)
            else:
                # Only show if both prices are entered
                if item['competitor'] > 0 and item['super_one'] > 0:
                    valid_comparisons.append(item)
        
        st.markdown(f"### {competitor} Comparisons")
        st.markdown(f"**Date**: {check_date.strftime('%m/%d/%Y')}")
        
        if valid_comparisons:
            st.success(f"✅ {len(valid_comparisons)} valid comparisons | 📦 {len(dnc_products)} items not carried")
            
            # Display cards in 2x2 grid
            for idx in range(0, len(valid_comparisons), 2):
                col1, col2 = st.columns(2)
                
                for col_idx, col in enumerate([col1, col2]):
                    if idx + col_idx < len(valid_comparisons):
                        item = valid_comparisons[idx + col_idx]
                        # Fixed formula: abs() to always show positive savings
                        savings = abs(item['competitor'] - item['super_one'])
                        
                        with col:
                            with st.container(border=True):
                                # Header - Cooper Black font with different sizes
                                st.markdown(
                                    "<div style='text-align: center; margin: 8px 0; padding: 10px 0;'>"
                                    "<h2 style='margin: 0; font-family: \"Cooper Black\", \"Arial Black\", sans-serif; font-weight: 900;'>"
                                    "<span style='font-size: 42px;'>Compare</span> "
                                    "<u style='font-size: 28px;'>AND</u> "
                                    "<span style='font-size: 42px;'>Save</span>"
                                    "</h2>"
                                    "</div>",
                                    unsafe_allow_html=True
                                )
                                
                                # Product Name - Arial (increased font size to 26px)
                                st.markdown(
                                    f"<h3 style='text-align: center; margin: 12px 0; font-family: Arial, sans-serif; font-weight: bold; font-size: 26px; border-bottom: 2px solid black; padding-bottom: 8px;'>{item['product']}</h3>",
                                    unsafe_allow_html=True
                                )
                                
                                # Main content: Two columns with vertical divider
                                left_col, divider_col, right_col = st.columns([0.9, 0.08, 1.1], gap="small")
                                
                                with left_col:
                                    # Competitor Price Label - Ink Free font (increased to 16px)
                                    st.markdown(
                                        f"<div style='text-align: center; font-style: italic; font-size: 16px; margin-bottom: 8px; font-family: \"Ink Free\", \"Segoe Print\", Arial, sans-serif;'>{competitor}<br/>Price</div>",
                                        unsafe_allow_html=True
                                    )
                                    # Competitor Price - Arial (increased to 44px)
                                    st.markdown(
                                        f"<div style='text-align: center; font-weight: bold; font-size: 44px; font-family: Arial, sans-serif; margin-bottom: 16px;'>${item['competitor']:.2f}</div>",
                                        unsafe_allow_html=True
                                    )
                                    
                                    # Divider line in left column
                                    st.markdown("<hr style='margin: 12px 0; border: 1px solid #666;'>", unsafe_allow_html=True)
                                    
                                    # Super 1 Price Label - Ink Free font (increased to 15px)
                                    st.markdown(
                                        "<div style='text-align: center; font-style: italic; font-size: 15px; margin-bottom: 6px; font-family: \"Ink Free\", \"Segoe Print\", Arial, sans-serif;'>Super 1 Price</div>",
                                        unsafe_allow_html=True
                                    )
                                    # Super 1 Price - Arial (increased to 40px)
                                    st.markdown(
                                        f"<div style='text-align: center; font-weight: bold; font-size: 40px; font-family: Arial, sans-serif;'>${item['super_one']:.2f}</div>",
                                        unsafe_allow_html=True
                                    )
                                
                                with divider_col:
                                    # Vertical divider line
                                    st.markdown(
                                        "<div style='border-left: 2px solid black; height: 180px; margin: 0 auto;'></div>",
                                        unsafe_allow_html=True
                                    )
                                
                                with right_col:
                                    # Savings Amount with Curved Text using SVG - Arial (increased to 60px)
                                    st.markdown(
                                        """
                                        <div style='display: flex; flex-direction: column; justify-content: center; align-items: center; height: 180px; text-align: center;'>
                                        <svg width="140" height="90" viewBox="0 0 140 90" style='margin-bottom: 8px;'>
                                          <defs>
                                            <path id="curve" d="M 10,70 A 60,60 0 0,1 130,70" fill="none"/>
                                          </defs>
                                          <text font-family="Arial, sans-serif" font-size="13" font-weight="bold" letter-spacing="1" fill="black">
                                            <textPath href="#curve" startOffset="50%" text-anchor="middle">
                                              BUYING POWER SAVINGS
                                            </textPath>
                                          </text>
                                        </svg>
                                        """ + f"<div style='font-weight: bold; font-size: 60px; color: darkgreen; font-family: Arial, sans-serif; margin-top: -8px;'>${savings:.2f}</div>" +
                                        """
                                        </div>
                                        """,
                                        unsafe_allow_html=True
                                    )
                                
                                # Date Footer - Arial
                                st.markdown(
                                    f"<div style='text-align: center; font-size: 9px; margin-top: 12px; padding-top: 8px; border-top: 1px solid #ccc; font-family: Arial, sans-serif;'>Price Check Date: {check_date.strftime('%m/%d/%Y')}</div>",
                                    unsafe_allow_html=True
                                )
        else:
            st.warning("No valid comparisons found for this competitor.")
        
        if dnc_products:
            st.markdown("### Items Not Carried")
            for idx in range(0, len(dnc_products), 2):
                col1, col2 = st.columns(2)
                
                for col_idx, col in enumerate([col1, col2]):
                    if idx + col_idx < len(dnc_products):
                        item = dnc_products[idx + col_idx]
                        
                        with col:
                            with st.container(border=True):
                                # Header - Cooper Black font with different sizes
                                st.markdown(
                                    "<div style='text-align: center; margin: 8px 0; padding: 10px 0;'>"
                                    "<h2 style='margin: 0; font-family: \"Cooper Black\", \"Arial Black\", sans-serif; font-weight: 900;'>"
                                    "<span style='font-size: 42px;'>Compare</span> "
                                    "<u style='font-size: 28px;'>AND</u> "
                                    "<span style='font-size: 42px;'>Save</span>"
                                    "</h2>"
                                    "</div>",
                                    unsafe_allow_html=True
                                )
                                
                                # Product Name - Arial (increased font size to 26px)
                                st.markdown(
                                    f"<h3 style='text-align: center; margin: 12px 0; font-family: Arial, sans-serif; font-weight: bold; font-size: 26px; border-bottom: 2px solid black; padding-bottom: 8px;'>{item['product']}</h3>",
                                    unsafe_allow_html=True
                                )
                                
                                # Main content: Two columns with vertical divider
                                left_col, divider_col, right_col = st.columns([0.9, 0.08, 1.1], gap="small")
                                
                                with left_col:
                                    # Competitor Price Label - Ink Free font (increased to 16px)
                                    st.markdown(
                                        f"<div style='text-align: center; font-style: italic; font-size: 16px; margin-bottom: 8px; font-family: \"Ink Free\", \"Segoe Print\", Arial, sans-serif;'>{competitor}<br/>Price</div>",
                                        unsafe_allow_html=True
                                    )
                                    # Competitor Price - Arial (increased to 44px)
                                    st.markdown(
                                        "<div style='text-align: center; font-weight: bold; font-size: 44px; font-family: Arial, sans-serif; margin-bottom: 16px;'>$0.00</div>",
                                        unsafe_allow_html=True
                                    )
                                    
                                    # Divider line in left column
                                    st.markdown("<hr style='margin: 12px 0; border: 1px solid #666;'>", unsafe_allow_html=True)
                                    
                                    # Super 1 Price Label - Ink Free font (increased to 15px)
                                    st.markdown(
                                        "<div style='text-align: center; font-style: italic; font-size: 15px; margin-bottom: 6px; font-family: \"Ink Free\", \"Segoe Print\", Arial, sans-serif;'>Super 1 Price</div>",
                                        unsafe_allow_html=True
                                    )
                                    # Super 1 Price - Arial (increased to 40px)
                                    st.markdown(
                                        f"<div style='text-align: center; font-weight: bold; font-size: 40px; font-family: Arial, sans-serif;'>${item['super_one']:.2f}</div>",
                                        unsafe_allow_html=True
                                    )
                                
                                with divider_col:
                                    # Vertical divider line
                                    st.markdown(
                                        "<div style='border-left: 2px solid black; height: 180px; margin: 0 auto;'></div>",
                                        unsafe_allow_html=True
                                    )
                                
                                with right_col:
                                    # Does Not Carry with Curved Text using SVG
                                    st.markdown(
                                        """
                                        <div style='display: flex; flex-direction: column; justify-content: center; align-items: center; height: 180px; text-align: center;'>
                                        <svg width="140" height="90" viewBox="0 0 140 90" style='margin-bottom: 20px;'>
                                          <defs>
                                            <path id="curve2" d="M 10,70 A 60,60 0 0,1 130,70" fill="none"/>
                                          </defs>
                                          <text font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="darkred">
                                            <textPath href="#curve2" startOffset="50%" text-anchor="middle">
                                              DOES NOT CARRY
                                            </textPath>
                                          </text>
                                        </svg>
                                        </div>
                                        """,
                                        unsafe_allow_html=True
                                    )
                                
                                # Date Footer - Arial
                                st.markdown(
                                    f"<div style='text-align: center; font-size: 9px; margin-top: 12px; padding-top: 8px; border-top: 1px solid #ccc; font-family: Arial, sans-serif;'>Price Check Date: {check_date.strftime('%m/%d/%Y')}</div>",
                                    unsafe_allow_html=True
                                )

with tab3:
    st.header("Print Your Cards")
    
    if not products_data:
        st.warning("No products entered yet. Go to 'Input Data' tab to add products.")
    else:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 🖨️ Print Instructions")
            st.markdown(f"""
            1. **Choose your competitor**: {competitor}
            2. **Date**: {check_date.strftime('%m/%d/%Y')}
            3. **Paper type**: 8.5" × 11" perforated card stock
            4. **Cards per page**: 4 (2×2 grid)
            5. **Color option**: Choose preferred ink color
            
            **Print Setup:**
            - Use your browser's print function (Ctrl+P or Cmd+P)
            - Set margins to "None" or "Minimal"
            - Set scale to "100%"
            - Print to your preferred color or black & white
            """)
        
        with col2:
            st.markdown("### 📄 Print Summary")
            
            # Generate preview
            valid_comparisons = [item for item in products_data 
                               if item['carries'] != 'DNC' and item['competitor'] > 0 and item['super_one'] > 0]
            dnc_products = [item for item in products_data if item['carries'] == 'DNC']
            
            all_items = valid_comparisons + dnc_products
            
            num_pages = (len(all_items) + 3) // 4
            
            st.metric(
                label="Total Cards",
                value=len(all_items)
            )
            
            st.metric(
                label="Pages Needed",
                value=num_pages
            )
    
    st.markdown("---")
    
    # Add instructions for Streamlit Cloud deployment
    with st.expander("📋 How to Deploy This App"):
        st.markdown("""
        ### Deploy to Streamlit Cloud (Free)
        
        1. **Push to GitHub**:
           - Create a new GitHub repository
           - Push `streamlit_app.py` to the repo
        
        2. **Connect to Streamlit Cloud**:
           - Go to [share.streamlit.io](https://share.streamlit.io)
           - Click "New app"
           - Select your GitHub repo
           - Select branch and file (`streamlit_app.py`)
           - Click "Deploy"
        
        3. **Share the URL**:
           - You'll get a unique URL like `https://yourapp.streamlit.app`
           - Share it with your team!
        
        ### Requirements File
        Create a `requirements.txt` file with:
        ```
        streamlit>=1.28.0
        ```
        """)
