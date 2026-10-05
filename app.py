import streamlit as st

st.set_page_config(
    page_title="Yarn Count Calculator",
    page_icon="🧶",
    layout="centered"
)

# -----------------------------
# Conversion constants
# -----------------------------
YARDS_PER_HANK = 840
POUNDS_PER_HANK = 1
GRAMS_PER_POUND = 453.59237

st.title("🧶 Yarn Count Calculator")
st.caption("Calculate yarn count using pounds, yards, and hanks.")

st.divider()

st.subheader("Enter Yarn Information")

col1, col2 = st.columns(2)

with col1:
    weight_lbs = st.number_input(
        "Weight (lbs)",
        min_value=0.0001,
        value=1.0,
        step=0.1,
        format="%.4f"
    )

with col2:
    length_yards = st.number_input(
        "Length (yards)",
        min_value=0.0001,
        value=840.0,
        step=10.0,
        format="%.2f"
    )

# -----------------------------
# Calculations
# -----------------------------
hanks = length_yards / YARDS_PER_HANK

# English Cotton Count (Ne):
# Number of 840-yard hanks per pound.
ne_count = hanks / weight_lbs

# Equivalent length per pound.
yards_per_lb = length_yards / weight_lbs

# Weight in grams.
weight_grams = weight_lbs * GRAMS_PER_POUND

# -----------------------------
# Results
# -----------------------------
st.subheader("Results")

r1, r2 = st.columns(2)

with r1:
    st.metric("Yarn Count (Ne)", f"{ne_count:.2f}")

with r2:
    st.metric("Hanks", f"{hanks:.2f}")

r3, r4 = st.columns(2)

with r3:
    st.metric("Yards per Pound", f"{yards_per_lb:,.2f}")

with r4:
    st.metric("Weight", f"{weight_grams:,.2f} g")

st.divider()

st.subheader("📐 Formula")

st.markdown(
    """
**English Cotton Count (Ne):**

`Ne = Number of 840-yard hanks ÷ Weight in pounds`

Since:

`Hanks = Yards ÷ 840`

Therefore:

`Ne = Yards ÷ (840 × Pounds)`
"""
)

st.info(
    "Example: If yarn weighs 1 lb and its length is 840 yards, "
    "the yarn count is Ne 1.00."
)

st.divider()

st.caption("Yarn Count Calculator • Streamlit Web App")
