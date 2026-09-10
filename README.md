\# Sales Performance \& Business Analytics



\## 1. Project Overview



Sales Performance \& Business Analytics is a data analytics project developed to analyze sales transactions and identify important business trends, patterns, and profitability opportunities.



The project uses Python, Pandas, NumPy, Matplotlib, Seaborn, SQL concepts, and Power BI to perform data preparation, exploratory data analysis, visualization, and business intelligence reporting.



The analysis is based on a public Superstore sales dataset containing 9,994 sales transactions and 21 original columns.



\---



\## 2. Problem Statement



Businesses generate large amounts of sales data, but raw transaction data can be difficult to interpret directly.



The objective of this project is to analyze sales data to understand:



\- Overall sales and profitability

\- Regional sales performance

\- Category and sub-category performance

\- Monthly sales trends

\- Relationships between sales, quantity, discount, and profit

\- Potential outliers and loss-making transactions



The final analysis is presented through visualizations and an interactive Power BI dashboard to support data-driven business decisions.



\---



\## 3. Dataset



Dataset Used: Public Superstore Sales Dataset



Original Records: 9,994



Original Columns: 21



Important fields include:



\- Order ID

\- Order Date

\- Ship Date

\- Ship Mode

\- Customer ID

\- Customer Name

\- Segment

\- Country

\- City

\- State

\- Postal Code

\- Region

\- Product ID

\- Category

\- Sub-Category

\- Product Name

\- Sales

\- Quantity

\- Discount

\- Profit



The cleaned dataset contains 9,994 rows and 20 columns after removing the unnecessary Row ID field.



\---



\## 4. Tools \& Technologies



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Power BI

\- DAX

\- Git

\- GitHub



\---



\## 5. Data Preparation \& Cleaning



The dataset was inspected before analysis to understand its structure and quality.



The following preprocessing steps were performed:



\- Inspected rows and columns

\- Checked data types

\- Checked missing values

\- Checked duplicate records

\- Converted Order Date and Ship Date into datetime format

\- Validated Sales values

\- Validated Quantity values

\- Checked Discount values

\- Removed the unnecessary Row ID column

\- Saved the cleaned dataset for further analysis



Final cleaned dataset:



\- Rows: 9,994

\- Columns: 20

\- Missing values: 0

\- Duplicate rows: 0



\---



\## 6. Exploratory Data Analysis



Descriptive statistics and exploratory analysis were performed using Python.



\### Overall Performance



\- Total Sales: $2,297,200.86

\- Total Profit: $286,397.02

\- Total Quantity: 37,873

\- Average Sales per transaction: $229.86

\- Average Profit per transaction: $28.66



\### Regional Analysis



Sales by region:



| Region | Sales |

|---|---:|

| West | $725,457.82 |

| East | $678,781.24 |

| Central | $501,239.89 |

| South | $391,721.91 |



West is the highest-performing region by sales.



\### Category Analysis



| Category | Sales |

|---|---:|

| Technology | $836,154.03 |

| Furniture | $741,999.80 |

| Office Supplies | $719,047.03 |



Technology is the highest-performing category by sales.



\### Profitability



Technology generated approximately $145,454.95 profit.



Office Supplies generated approximately $122,490.80 profit.



Furniture generated approximately $18,451.27 profit, indicating relatively low profitability compared with its sales volume.



\### Sub-Category Analysis



Tables generated approximately -$17,725.48 profit, making it the largest loss-making sub-category.



\### Loss-Making Transactions



The analysis identified 1,871 loss-making transactions with total losses of approximately $156,131.29.



\### Correlation Analysis



Important correlations include:



\- Sales and Profit: 0.479

\- Sales and Quantity: 0.201

\- Discount and Profit: -0.219

\- Sales and Discount: -0.028



The positive Sales-Profit relationship indicates that higher sales are generally associated with higher profit, although the relationship is not perfect.



\### Outlier Analysis



The IQR method was used to identify potential outliers in Sales.



\- Q1: $17.28

\- Q3: $209.94

\- IQR: $192.66

\- Upper limit: approximately $498.93

\- Potential sales outliers: 1,167



These records were treated as potential high-value transactions rather than automatically removing them because legitimate large transactions can occur in sales data.



\---



\## 7. Data Visualizations



Five visualizations were created using Python:



1\. Monthly Sales Trend

2\. Sales by Region

3\. Sales by Category

4\. Profit by Sub-Category

5\. Correlation Heatmap



The visualization files are available in the `Visualizations` folder.



\---



\## 8. Power BI Dashboard



An interactive Power BI dashboard was developed to provide a business-focused view of the sales data.



\### KPI Cards



\- Total Sales

\- Total Profit

\- Total Quantity

\- Profit Margin



\### Dashboard Visualizations



\- Monthly Sales Trend

\- Sales by Region

\- Sales by Category

\- Profit by Sub-Category



\### Filters / Slicers



\- Region

\- Category



\### Key Dashboard Metrics



\- Total Sales: $2.30M

\- Total Profit: $286.40K

\- Total Quantity: 37,873

\- Profit Margin: 12.47%



\---



\## 9. Key Business Insights



1\. West is the strongest region with approximately $725,457.82 in sales.



2\. South has the lowest regional sales at approximately $391,721.91 and represents an opportunity for improvement.



3\. Technology is the highest-performing category with approximately $836,154.03 in sales and $145,454.95 in profit.



4\. Furniture has high sales but comparatively low profit, indicating potential margin pressure.



5\. Tables is the largest loss-making sub-category with approximately -$17,725.48 profit.



6\. The dataset contains 1,871 loss-making transactions, highlighting an opportunity to improve profitability.



7\. November 2017 recorded the highest monthly sales at approximately $118,447.83.



\---



\## 10. Business Recommendations



\### 1. Improve South Region Performance



Use targeted promotions, regional marketing campaigns, and customer-specific offers to increase sales in the South region.



\### 2. Review Furniture Profitability



Analyze pricing, discounts, supplier costs, and shipping costs to improve Furniture margins.



\### 3. Reduce Losses in Tables



Review Tables products with recurring losses and evaluate pricing, discounts, and supplier costs.



\### 4. Focus on Profitable Products



Continue investing in high-performing and profitable products, particularly within the Technology category.



\### 5. Monitor Discounts



Analyze the effect of discounts on profitability and avoid excessive discounting on low-margin products.



\---



\## 11. Conclusion



This project demonstrates an end-to-end data analytics workflow from raw sales data preparation to exploratory analysis, visualization, and business intelligence reporting.



Python was used for data cleaning, statistical analysis, EDA, correlation analysis, outlier detection, and visualization. Power BI was used to create an interactive dashboard containing KPIs, charts, and filters.



The analysis identified important differences in regional, category, and sub-category performance and highlighted opportunities to improve profitability.



The project demonstrates how data can be transformed into meaningful business insights and actionable recommendations.



\---



\## 12. Project Structure



```text

Sales-Performance-Business-Analytics/

│

├── Dataset/

│   ├── Superstore\_Sales.csv

│   └── Superstore\_Sales\_Cleaned.csv

│

├── Python/

│   ├── Task3\_Data\_Preparation.py

│   ├── Task4\_EDA.py

│   └── Task5\_Visualizations.py

│

├── Visualizations/

│   ├── 01\_Monthly\_Sales\_Trend.png

│   ├── 02\_Sales\_by\_Region.png

│   ├── 03\_Sales\_by\_Category.png

│   ├── 04\_Profit\_by\_SubCategory.png

│   └── 05\_Correlation\_Heatmap.png

│

├── PowerBI/

│   └── Sales\_Performance\_Business\_Analytics.pbix

│

├── Report/

│

├── Presentation/

│

└── README.md

\## 13. Author



Data Analytics Internship Project



InternNova Internship Program



Project: Sales Performance \& Business Analytics

