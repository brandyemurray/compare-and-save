# Compare and Save - Streamlit Price Comparison App
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
import html
import uuid

import streamlit as st


@dataclass(frozen=True)
class ProductRow:
    name: str
    super_one_price: float
    competitor_price: float
    carries: str  # "Yes" | "DNC"


def money(amount: float) -> str:
    return f"${amount:,.2f}"


def competitor_label_html(competitor: str) -> str:
    # Excel template breaks Safeway/Albertsons across lines
    if competitor.lower().startswith("safeway"):
        return '<span class="cs-label-line1">Safeway/Albertsons</span><span class="cs-label-line2">Price</span>'
    return f"{competitor} Price"


def render_card_html(
    *,
    competitor: str,
    check_date: date,
    row: ProductRow,
) -> str:
    uid = uuid.uuid4().hex
    # Cross-platform month/day without leading zeros (Excel-style)
    if hasattr(check_date, "strftime"):
        date_str = check_date.strftime("%m/%d/%Y").lstrip("0").replace("/0", "/")
    else:
        date_str = str(check_date)

    is_dnc = row.carries == "DNC" or row.competitor_price == 0
    competitor_price = 0.0 if is_dnc else float(row.competitor_price)
    super_one_price = float(row.super_one_price)

    # Savings display: for DNC we show (Super 1 Price) in red parentheses (Excel style).
    if is_dnc:
        savings_amount = abs(super_one_price)
        savings_text = f"({money(savings_amount)})"
        savings_class = "cs-savings cs-savings-negative"
        right_note = f'<div class="cs-dnc-note">{competitor} DOES NOT CARRY</div>'
    else:
        savings_amount = abs(competitor_price - super_one_price)
        savings_text = money(savings_amount)
        savings_class = "cs-savings cs-savings-positive"
        right_note = ""

    # IMPORTANT: keep every line left-aligned. If we indent HTML in Markdown,
    # Streamlit can interpret it as a code block and show raw tags.
    return "\n".join(
        [
            '<div class="cs-card">',
            '<div class="cs-header">',
            '<div class="cs-title">',
            '<span class="cs-title-compare">Compare</span>',
            '<span class="cs-title-and"><span>AND</span></span>',
            '<span class="cs-title-save">Save</span>',
            "</div>",
            f'<div class="cs-product">{html.escape(row.name)}</div>',
            "</div>",
            "",
            '<div class="cs-body">',
            '<div class="cs-left">',
            '<div class="cs-price-block">',
            f'<div class="cs-label">{competitor_label_html(competitor)}</div>',
            f'<div class="cs-price">{money(competitor_price)}</div>',
            "</div>",
            "",
            '<div class="cs-price-block">',
            '<div class="cs-label">Super 1 Price</div>',
            f'<div class="cs-price">{money(super_one_price)}</div>',
            "</div>",
            "</div>",
            "",
            '<div class="cs-divider" aria-hidden="true"></div>',
            "",
            '<div class="cs-right">',
            f'<svg class="cs-arc" viewBox="0 0 250 120" preserveAspectRatio="xMidYMid meet" aria-hidden="true">',
            "<defs>",
            f'<path id="arcPath_{uid}" d="M 25,100 A 100,100 0 0,1 225,100" fill="none" stroke="none"></path>',
            "</defs>",
            '<text class="cs-arc-text">',
            f'<textPath href="#arcPath_{uid}" startOffset="50%" text-anchor="middle">BUYING POWER SAVINGS</textPath>',
            "</text>",
            "</svg>",
            "",
            f'<div class="{savings_class}">{savings_text}</div>',
            "",
            '<div class="cs-date-row">',
            '<span class="cs-date-label">Price Check Date:</span>',
            f'<span class="cs-date-val">{date_str}</span>',
            "</div>",
            f"{right_note}" if right_note else "",
            "</div>",
            "</div>",
            "</div>",
        ]
    ).strip()


CARD_CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&display=swap');

  .cs-card {
    background: #fff;
    border: 3px solid #000;
    padding: 0.18in 0.2in;
    box-sizing: border-box;
    break-inside: avoid;
    page-break-inside: avoid;
  }

  .cs-header {
    text-align: center;
    margin-bottom: 0.06in;
  }

  .cs-title {
    line-height: 1;
    margin-bottom: 0.04in;
  }

  .cs-title-compare,
  .cs-title-save {
    font-family: "Cooper Black", "CooperBlack", Georgia, serif;
    font-size: 44px;
    font-weight: 800;
    letter-spacing: 0.5px;
  }

  .cs-title-and {
    display: inline-block;
    margin: 0 10px;
    font-family: "Cooper Black", "CooperBlack", Georgia, serif;
    font-weight: 900;
    font-size: 26px;
    position: relative;
    top: -8px;
  }

  .cs-title-and span {
    border-bottom: 4px solid #000;
    padding-bottom: 2px;
  }

  .cs-product {
    font-family: Arial, sans-serif;
    font-size: 20px;
    font-weight: 700;
    margin-top: 2px;
  }

  .cs-body {
    display: grid;
    grid-template-columns: 1fr 0.08in 1.2fr;
    align-items: stretch;
    gap: 0.12in;
  }

  .cs-divider {
    width: 0.08in;
    background: #000;
  }

  .cs-left {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 0.14in;
    padding-right: 0.06in;
  }

  .cs-price-block {
    text-align: left;
  }

  .cs-label {
    font-family: "Caveat", cursive;
    font-size: 28px;
    font-weight: 700;
    text-decoration: underline;
    text-underline-offset: 5px;
  }

  .cs-label-line1 {
    display: block;
    line-height: 1.05;
  }
  .cs-label-line2 {
    display: block;
    line-height: 1.05;
    text-align: center;
  }

  .cs-price {
    font-family: Arial, sans-serif;
    font-size: 44px;
    font-weight: 900;
    margin-top: 4px;
  }

  .cs-right {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-left: 0.06in;
    text-align: center;
  }

  .cs-arc {
    width: 230px;
    height: 115px;
    margin: 0 0 -8px 0;
  }

  .cs-arc-text {
    font-family: Arial, sans-serif;
    font-size: 22px;
    font-weight: 900;
    letter-spacing: 3px;
    fill: #000;
  }

  .cs-savings {
    font-family: Arial, sans-serif;
    font-size: 64px;
    font-weight: 900;
    line-height: 1;
  }

  .cs-savings-negative {
    color: #e00000;
  }

  .cs-savings-positive {
    color: #000;
  }

  .cs-date-row {
    width: 100%;
    display: flex;
    justify-content: space-between;
    margin-top: 8px;
    font-family: Arial, sans-serif;
    font-size: 14px;
  }

  .cs-dnc-note {
    margin-top: 6px;
    font-family: Arial, sans-serif;
    font-size: 12px;
    font-weight: 800;
  }

  /* Print-only behavior: hide Streamlit UI, show only the card grid */
  @page { size: letter; margin: 0.35in; }

  @media print {
    body * { visibility: hidden !important; }
    #print-area, #print-area * { visibility: visible !important; }
    #print-area { position: absolute; left: 0; top: 0; width: 100%; }

    .cs-pages { display: block; }
    .cs-page {
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-template-rows: 1fr 1fr;
      gap: 0.25in;
      break-after: page;
      page-break-after: always;
    }
    .cs-page.is-last {
      break-after: auto;
      page-break-after: auto;
    }
    .cs-card { margin: 0; }
  }
</style>
"""


st.set_page_config(
    page_title="Compare and Save",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(CARD_CSS, unsafe_allow_html=True)

st.title("💰 Compare and Save")
st.markdown("**Weekly Price Comparison Tool** — Generate printable comparison cards")

with st.sidebar:
    st.header("Settings")
    competitor = st.radio(
        "Which competitor are you comparing?",
        ["Winco", "Safeway/Albertsons"],
        help="Choose which competitor to generate cards for",
    )
    check_date = st.date_input(
        "Price Check Date",
        value=datetime.today(),
        help="Date to display on cards",
    )

tab1, tab2, tab3 = st.tabs(["📊 Input Data", "👁️ Preview", "🖨️ Print"])

products_data: list[ProductRow] = []
error_products: list[ProductRow] = []

with tab1:
    st.header("Enter Product Prices")

    left, right = st.columns([2, 1])
    with right:
        num_products = st.number_input(
            "How many products?",
            min_value=1,
            max_value=100,
            value=10,
            step=1,
            help="Add/remove products as needed",
        )

    with left:
        st.markdown("**Pricing Data**")

    header_cols = st.columns([3, 1.5, 1.5, 1])
    header_cols[0].markdown("**Product Name**")
    header_cols[1].markdown("**Super 1 Price**")
    header_cols[2].markdown("**Competitor Price**")
    header_cols[3].markdown("**Carries?**")

    for i in range(int(num_products)):
        c1, c2, c3, c4 = st.columns([3, 1.5, 1.5, 1])

        with c1:
            name = st.text_input(
                "Product Name",
                key=f"product_{i}",
                label_visibility="collapsed",
                placeholder=f"Product {i + 1}",
            ).strip()

        with c2:
            super_one_price = st.number_input(
                "Super 1",
                min_value=0.0,
                step=0.01,
                key=f"super1_{i}",
                label_visibility="collapsed",
                format="%.2f",
            )

        with c3:
            competitor_price = st.number_input(
                "Competitor",
                min_value=0.0,
                step=0.01,
                key=f"competitor_{i}",
                label_visibility="collapsed",
                format="%.2f",
            )

        with c4:
            carries = st.selectbox(
                "Carries?",
                ["Yes", "DNC"],
                key=f"carries_{i}",
                label_visibility="collapsed",
            )

        if not name:
            continue

        row = ProductRow(
            name=name,
            super_one_price=float(super_one_price or 0.0),
            competitor_price=float(competitor_price or 0.0),
            carries=str(carries),
        )
        products_data.append(row)

        if row.carries == "Yes" and row.competitor_price > 0 and row.super_one_price > row.competitor_price:
            error_products.append(row)

    if error_products:
        st.error(
            f"🚨 **HOLD UP!** 🚨\n\n"
            f"**{len(error_products)} product(s) have HIGHER Super 1 prices than the competitor!**\n\n"
            "This defeats the purpose of the comparison. Fix these ASAP."
        )
        for row in error_products:
            st.error(f"❌ **{row.name}** — Super 1: {money(row.super_one_price)} vs {competitor}: {money(row.competitor_price)}")

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
        valid = [r for r in products_data if r.carries != "DNC" and r.competitor_price > 0 and r.super_one_price > 0]
        dnc = [r for r in products_data if r.carries == "DNC" or r.competitor_price == 0]

        st.markdown(f"### {competitor} Comparisons")
        st.markdown(f"**Date**: {check_date.strftime('%m/%d/%Y')}")

        st.success(f"✅ {len(valid)} valid comparisons | 📦 {len(dnc)} items not carried")

        # Show valid then DNC (like your spreadsheet tabs)
        rows_to_show = valid + dnc

        for idx in range(0, len(rows_to_show), 2):
            col_a, col_b = st.columns(2)
            for j, col in enumerate([col_a, col_b]):
                if idx + j >= len(rows_to_show):
                    continue
                row = rows_to_show[idx + j]
                with col:
                    st.markdown(
                        render_card_html(competitor=competitor, check_date=check_date, row=row),
                        unsafe_allow_html=True,
                    )

with tab3:
    st.header("Print Your Cards")

    if not products_data:
        st.warning("No products entered yet. Go to 'Input Data' tab to add products.")
    else:
        valid = [r for r in products_data if r.carries != "DNC" and r.competitor_price > 0 and r.super_one_price > 0]
        dnc = [r for r in products_data if r.carries == "DNC" or r.competitor_price == 0]
        all_items = valid + dnc

        left, right = st.columns([1, 1])
        with left:
            st.markdown("### 🖨️ Print Instructions")
            st.markdown(
                f"""
1. **Choose your competitor**: {competitor}  
2. **Date**: {check_date.strftime('%m/%d/%Y')}  
3. **Paper type**: 8.5\" × 11\" perforated card stock  
4. **Cards per page**: 4 (2×2 grid)  

**Print Setup (important):**
- Open print (Ctrl+P / Cmd+P) **while on this Print tab**
- Turn **Headers and footers** OFF
- Turn **Background graphics** ON
- Margins: **None** or **Minimal**
- Scale: **100%**
"""
            )
        with right:
            st.markdown("### 📄 Print Summary")
            num_pages = (len(all_items) + 3) // 4
            st.metric(label="Total Cards", value=len(all_items))
            st.metric(label="Pages Needed", value=num_pages)

        st.markdown("---")
        st.markdown("### Printable Cards (4 per page)")

        # Build paginated HTML: 4 cards per page in a 2x2 grid
        pages: list[list[ProductRow]] = []
        for i in range(0, len(all_items), 4):
            pages.append(all_items[i : i + 4])

        pages_html = '<div class="cs-pages">'
        for pi, page_rows in enumerate(pages):
            is_last = pi == len(pages) - 1
            pages_html += f'<div class="cs-page{" is-last" if is_last else ""}">'
            for row in page_rows:
                pages_html += render_card_html(competitor=competitor, check_date=check_date, row=row)
            pages_html += "</div>"
        pages_html += "</div>"

        st.markdown(f'<div id="print-area">{pages_html}</div>', unsafe_allow_html=True)

