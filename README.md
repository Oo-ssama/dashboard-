# 📊 Supply Chain Dashboard (Streamlit)

An interactive **Supply Chain Dashboard** built with **Streamlit** that lets you upload, explore, and visualize supply chain data — including supplier performance, top SKUs, shipping, and customer insights.

---

## 🧩 Features

- 📂 Upload CSV or Excel files  
- 📈 Dashboard with KPIs and visual charts  
- 🧹 Data overview and cleaning options  
- 🏭 Supplier performance and defect rate analysis  
- 🚚 Shipping performance visualization  
- 🧑‍🤝‍🧑 Customer segmentation insights  
- 🎯 Full analytics showcase  

---

## ⚙️ Installation

Follow these steps to install and launch the app.

### 1️⃣ Clone the repository and access 
```bash
git clone https://github.com/Oo-ssama/dashboard-

cd dashboard
```

### 2️⃣ Install required dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application
Once dependencies are installed, start the Streamlit app using:
```bash
streamlit run Dashboard.py
```
Then open the local URL displayed in your terminal (usually [http://localhost:8501](http://localhost:8501)).

---

## 📋 Example `requirements.txt`
If you don’t already have a `requirements.txt` file, create one with this content:
```
streamlit
pandas
seaborn
matplotlib
plotly
openpyxl
```

---

## 🧾 How to Use

1. Launch the app with the command above.  
2. On the **🏠 Home** page, upload your dataset in CSV or Excel format.  
3. Use the sidebar to navigate through the different sections:

| Page | Description |
|------|--------------|
| 🏠 Home | Upload and preview your dataset |
| 📊 Dashboard | Visualize KPIs and key metrics |
| 📁 Data Overview | Clean and inspect your data |
| 🏷️ Top SKUs | Identify best-performing SKUs |
| 🏭 Supplier Analysis | Evaluate supplier performance |
| 🚚 Shipping Analysis | Analyze carrier efficiency |
| 🧑‍🤝‍🧑 Customer Analysis | Segment and analyze customers |
| 🎯 Showcase | Summary of all analytics |

---

## 🧩 Expected Dataset Columns

To make the most of the dashboard, your dataset should include some or all of these columns:

| Column Name | Description |
|--------------|-------------|
| `SKU` | Product SKU identifier |
| `Product type` | Product category/type |
| `Revenue generated` | Total revenue from sales |
| `Number of products sold` | Quantity sold |
| `Supplier name` | Supplier’s name |
| `Lead time` | Average delivery time |
| `Defect rates` | Percentage of defective products |
| `Manufacturing costs` | Cost of production |
| `Shipping carriers` | Carrier name |
| `Shipping times` | Average delivery duration |
| `Shipping costs` | Average cost of shipping |
| `Transportation modes` | Transport method (Air, Sea, Road, etc.) |
| `Customer demographics` | Customer group or segment |
| `Price` | Unit selling price |


