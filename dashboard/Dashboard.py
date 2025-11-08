# streamlit_dashboard_persistent.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# --- Initialize session state for persistence ---
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()  # empty dataframe initially

# --- Sidebar Navigation ---
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "📊 Dashboard",
        "📁 Data Overview",
        "🏷️ Top SKUs",
        "🏭 Supplier Analysis",
        "🚚 Shipping Analysis",
        "🧑‍🤝‍🧑 Customer Analysis",
        "🎯 Showcase",
    ]
)

# --- Home Page ---
if page == "🏠 Home":
    st.title("🏠 Supply Chain Dashboard Home")

    uploaded_file = st.file_uploader("📂 Upload a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            st.session_state.df = pd.read_csv(uploaded_file)
        else:
            st.session_state.df = pd.read_excel(uploaded_file)

        st.success(f"✅ File uploaded: {uploaded_file.name}")
        st.dataframe(st.session_state.df.head(10))

    st.write("📈 Number of records in dataset:", st.session_state.df.shape[0])

    if st.button("🧹 Clear Uploaded Data"):
        st.session_state.df = pd.DataFrame()
        st.success("🗑️ Data cleared!")

# --- Use df from session_state in all other pages ---
df = st.session_state.df

# --- Dashboard Page ---
if page == "📊 Dashboard":
    if df.empty:
        st.info("📥 Upload a dataset in Home to see dashboard metrics.")
    else:
        st.title("📊 Dashboard Overview")
        st.metric("🧾 Total Records", df.shape[0])
        st.metric("💰 Total Revenue", f"${df['Revenue generated'].sum():,.2f}")
        st.metric("📦 Total Products Sold", int(df['Number of products sold'].sum()))
        st.metric("🔢 Unique SKUs", df['SKU'].nunique())

        revenue_by_type = df.groupby('Product type')['Revenue generated'].sum()
        fig = px.pie(revenue_by_type, values='Revenue generated', names=revenue_by_type.index,
                     title="💡 Revenue by Product Type")
        st.plotly_chart(fig)

        st.bar_chart(df['Shipping carriers'].value_counts())
        st.dataframe(df.head(20))
        st.download_button("💾 Download CSV", df.to_csv(index=False), file_name="dashboard_data.csv")

# --- Data Overview Page ---
elif page == "📁 Data Overview":
    st.title("📁 Data Overview & Cleaning")
    if df.empty:
        st.info("📥 Upload a dataset in Home to explore and clean it.")
    else:
        st.subheader("👀 Data Preview")
        st.dataframe(df.head(20), use_container_width=True)

        st.subheader("🧠 Dataset Information")
        buffer = df.info()
        st.text(buffer)
        st.write("🧾 Shape:", df.shape)
        st.write("🧩 Columns:", list(df.columns))
        st.write("🚨 Missing values per column:")
        st.dataframe(df.isnull().sum())

        st.subheader("🧹 Data Cleaning Options")
        if st.checkbox("🗑️ Drop duplicate rows"):
            df = df.drop_duplicates()
            st.session_state.df = df
            st.write("✅ Duplicates dropped. New shape:", df.shape)
        if st.checkbox("🚫 Drop rows with missing values"):
            df = df.dropna()
            st.session_state.df = df
            st.write("✅ Rows with missing values dropped. New shape:", df.shape)

        st.download_button(
            "💾 Download Cleaned File",
            df.to_csv(index=False),
            file_name="cleaned_data.csv",
            mime="text/csv"
        )

# --- Top SKUs Page ---
elif page == "🏷️ Top SKUs":
    if df.empty:
        st.info("📥 Upload a dataset in Home to see SKU analysis.")
    else:
        st.title("🏷️ Top 10 SKUs by Revenue and Products Sold")
        top_products = df.groupby('SKU').agg({
            'Number of products sold': 'sum',
            'Revenue generated': 'sum'
        }).sort_values(by='Revenue generated', ascending=False).head(10)
        st.dataframe(top_products, use_container_width=True)

        fig, ax = plt.subplots(figsize=(10,5))
        sns.barplot(x=top_products.index, y=top_products['Revenue generated'], ax=ax)
        ax.set_ylabel("Revenue Generated")
        ax.set_xlabel("SKU")
        ax.set_title("Top 10 SKUs by Revenue")
        st.pyplot(fig)

        st.subheader("💵 Price Distribution for Top SKUs")
        fig2, ax2 = plt.subplots(figsize=(10,5))
        sns.boxplot(x='SKU', y='Price', data=df[df['SKU'].isin(top_products.index)], ax=ax2)
        st.pyplot(fig2)

# --- Supplier Analysis Page ---
elif page == "🏭 Supplier Analysis":
    if df.empty:
        st.info("📥 Upload a dataset in Home to see supplier analysis.")
    else:
        st.title("🏭 Supplier Performance Analysis")
        lead_time_avg = df.groupby('Supplier name')['Lead time'].mean().sort_values()
        st.bar_chart(lead_time_avg)

        st.subheader("⚙️ Manufacturing Costs vs Defect Rates")
        fig, ax = plt.subplots(figsize=(10,5))
        sns.scatterplot(x='Manufacturing costs', y='Defect rates', data=df, hue='Supplier name', ax=ax)
        st.pyplot(fig)

        defect_summary = df.groupby('Supplier name')['Defect rates'].mean().sort_values(ascending=False)
        st.subheader("🚨 Defect Rates by Supplier")
        st.dataframe(defect_summary)

# --- Shipping Analysis Page ---
elif page == "🚚 Shipping Analysis":
    if df.empty:
        st.info("📥 Upload a dataset in Home to see shipping analysis.")
    else:
        st.title("🚚 Shipping Performance")
        shipping_stats = df.groupby('Shipping carriers').agg({
            'Shipping times': 'mean',
            'Shipping costs': 'mean'
        }).reset_index()
        st.dataframe(shipping_stats)

        fig, ax = plt.subplots(figsize=(10,5))
        sns.barplot(x='Shipping carriers', y='Shipping times', data=shipping_stats, ax=ax)
        ax.set_ylabel("Avg Shipping Time")
        ax.set_xlabel("Carrier")
        st.pyplot(fig)

        mode_counts = df['Transportation modes'].value_counts()
        st.bar_chart(mode_counts)

# --- Customer Analysis Page ---
elif page == "🧑‍🤝‍🧑 Customer Analysis":
    if df.empty:
        st.info("📥 Upload a dataset in Home to see customer analysis.")
    else:
        st.title("🧑‍🤝‍🧑 Customer Segment Analysis")
        customer_rev = df.groupby('Customer demographics')['Revenue generated'].sum()
        st.bar_chart(customer_rev)

        total_rev = df['Revenue generated'].sum()
        customer_value = df.groupby('Customer demographics')['Revenue generated'].sum().reset_index()
        customer_value['Value Segment'] = pd.cut(customer_value['Revenue generated'],
                                                bins=[0, 0.33*total_rev, 0.66*total_rev, total_rev],
                                                labels=['Low', 'Medium', 'High'])
        st.subheader("💎 Customer Segment Value")
        st.dataframe(customer_value)

# --- Showcase Page ---
elif page == "🎯 Showcase":
    if df.empty:
        st.info("📥 Upload a dataset in Home to see showcase metrics.")
    else:
        st.title("🎯 Full Analytics Showcase")
        st.metric("💰 Total Revenue", f"${df['Revenue generated'].sum():,.2f}")
        st.metric("📦 Total Products Sold", int(df['Number of products sold'].sum()))
        st.metric("🔢 Unique SKUs", df['SKU'].nunique())

        revenue_by_type = df.groupby('Product type')['Revenue generated'].sum()
        st.plotly_chart(px.pie(revenue_by_type, values='Revenue generated', names=revenue_by_type.index,
                               title="💡 Revenue by Product Type"))

        st.bar_chart(df['Shipping carriers'].value_counts())
        st.dataframe(df.head(20))
        st.download_button("💾 Download CSV", df.to_csv(index=False), file_name="full_data.csv")
