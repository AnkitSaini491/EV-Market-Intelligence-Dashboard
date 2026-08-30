
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# EV MARKET INTELLIGENCE DASHBOARD
# PART 1 - DATA + BASIC ANALYTICS
# ==========================================

np.random.seed(42)

# ==========================================
# CREATE SYNTHETIC EV DATA
# ==========================================

brands = [
    "Tesla",
    "BYD",
    "Tata",
    "Hyundai",
    "Kia",
    "BMW",
    "Mercedes",
    "MG",
    "Nissan",
    "Volkswagen"
]

models = [
    "Model 3",
    "Model Y",
    "Atto 3",
    "Nexon EV",
    "Ioniq 5",
    "EV6",
    "i4",
    "EQB",
    "ZS EV",
    "Leaf",
    "ID.4",
    "Seal",
    "Kona Electric",
    "Tiago EV",
    "X1 EV"
]

vehicle_types = [
    "Sedan",
    "SUV",
    "Hatchback",
    "Crossover"
]

countries = [
    "USA",
    "China",
    "India",
    "Germany",
    "UK",
    "Norway",
    "France",
    "Canada"
]

n = 1000

# ==========================================
# GENERATE DATA
# ==========================================

df = pd.DataFrame({

    "EV_ID": range(10001, 10001 + n),

    "Brand": np.random.choice(
        brands,
        n
    ),

    "Model": np.random.choice(
        models,
        n
    ),

    "Vehicle_Type": np.random.choice(
        vehicle_types,
        n
    ),

    "Country": np.random.choice(
        countries,
        n
    ),

    "Year": np.random.randint(
        2020,
        2027,
        n
    ),

    "Price": np.random.randint(
        15000,
        120000,
        n
    ),

    "Battery_kWh": np.random.randint(
        25,
        120,
        n
    ),

    "Range_km": np.random.randint(
        150,
        650,
        n
    ),

    "Sales": np.random.randint(
        500,
        50000,
        n
    ),

    "Charging_Time": np.round(
        np.random.uniform(
            0.5,
            12,
            n
        ),
        1
    )
})

# ==========================================
# SAVE RAW DATA
# ==========================================

df.to_csv(
    "ev_market_data.csv",
    index=False
)

print("=" * 65)
print("🚗 EV MARKET INTELLIGENCE DASHBOARD")
print("=" * 65)

# ==========================================
# DATA INFORMATION
# ==========================================

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 10 Records:")
print(df.head(10))

print("\nDataset Information:")
df.info()

# ==========================================
# CHECK MISSING VALUES
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================================
# CHECK DUPLICATES
# ==========================================

print("\nDuplicate Records:")
print(df.duplicated().sum())

# ==========================================
# BASIC STATISTICS
# ==========================================

print("\nBasic Statistics:")
print(
    df[
        [
            "Price",
            "Battery_kWh",
            "Range_km",
            "Sales",
            "Charging_Time"
        ]
    ].describe()
)

# ==========================================
# KPI CALCULATIONS
# ==========================================

total_models = df["Model"].nunique()

total_brands = df["Brand"].nunique()

total_sales = df["Sales"].sum()

average_price = df["Price"].mean()

average_battery = df["Battery_kWh"].mean()

average_range = df["Range_km"].mean()

total_countries = df["Country"].nunique()

# ==========================================
# KPI DISPLAY
# ==========================================

print("\n" + "=" * 65)
print("📊 KEY PERFORMANCE INDICATORS")
print("=" * 65)

print(
    f"Total EV Models      : {total_models}"
)

print(
    f"Total Brands         : {total_brands}"
)

print(
    f"Total EV Sales       : {total_sales:,}"
)

print(
    f"Average Price        : ${average_price:,.0f}"
)

print(
    f"Average Battery      : {average_battery:.1f} kWh"
)

print(
    f"Average Range        : {average_range:.1f} km"
)

print(
    f"Countries Covered    : {total_countries}"
)

# ==========================================
# BRAND-WISE SALES
# ==========================================

brand_sales = (
    df.groupby("Brand")["Sales"]
    .sum()
    .sort_values(
        ascending=False
    )
)

print("\n" + "=" * 65)
print("🏆 BRAND-WISE EV SALES")
print("=" * 65)

print(brand_sales)

# ==========================================
# BRAND SALES CHART
# ==========================================

plt.figure(
    figsize=(11, 6)
)

plt.bar(
    brand_sales.index,
    brand_sales.values
)

plt.title(
    "EV Sales by Brand"
)

plt.xlabel(
    "Brand"
)

plt.ylabel(
    "Total Sales"
)

plt.xticks(
    rotation=45
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.show()

# ==========================================
# TOP 10 EV MODELS
# ==========================================

top_models = (
    df.groupby("Model")["Sales"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)
)

print("\n" + "=" * 65)
print("🏆 TOP 10 EV MODELS")
print("=" * 65)

print(top_models)

# ==========================================
# TOP MODELS CHART
# ==========================================

plt.figure(
    figsize=(11, 6)
)

plt.barh(
    top_models.index,
    top_models.values
)

plt.title(
    "Top 10 EV Models by Sales"
)

plt.xlabel(
    "Sales"
)

plt.ylabel(
    "EV Model"
)

plt.gca().invert_yaxis()

plt.grid(
    axis="x",
    alpha=0.3
)

plt.tight_layout()

plt.show()

# ==========================================
# VEHICLE TYPE ANALYSIS
# ==========================================

vehicle_sales = (
    df.groupby("Vehicle_Type")["Sales"]
    .sum()
    .sort_values(
        ascending=False
    )
)

print("\nVehicle Type Sales:")
print(vehicle_sales)

# ==========================================
# VEHICLE TYPE CHART
# ==========================================

plt.figure(
    figsize=(9, 6)
)

plt.bar(
    vehicle_sales.index,
    vehicle_sales.values
)

plt.title(
    "EV Sales by Vehicle Type"
)

plt.xlabel(
    "Vehicle Type"
)

plt.ylabel(
    "Sales"
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.show()

# ==========================================
# COUNTRY-WISE SALES
# ==========================================

country_sales = (
    df.groupby("Country")["Sales"]
    .sum()
    .sort_values(
        ascending=False
    )
)

print("\nCountry-wise Sales:")
print(country_sales)

# ==========================================
# COUNTRY SALES CHART
# ==========================================

plt.figure(
    figsize=(10, 6)
)

plt.bar(
    country_sales.index,
    country_sales.values
)

plt.title(
    "EV Sales by Country"
)

plt.xlabel(
    "Country"
)

plt.ylabel(
    "Sales"
)

plt.xticks(
    rotation=30
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.show()

# ==========================================
# PART 1 COMPLETE
# ==========================================

print("\n" + "=" * 65)
print("✅ PART 1 COMPLETED")
print("=" * 65)

print(
    "Dataset saved as: ev_market_data.csv"
)

print(
    "Next: Advanced EV analytics and dashboard"
)
# ==========================================
# PART 2 - ADVANCED EV MARKET ANALYTICS
# ==========================================

print("\n" + "=" * 65)
print("🚗 PART 2 - ADVANCED EV MARKET ANALYTICS")
print("=" * 65)


# ==========================================
# 1. YEAR-WISE EV SALES
# ==========================================

yearly_sales = (
    df.groupby("Year")["Sales"]
    .sum()
    .sort_index()
)

print("\n📈 YEAR-WISE EV SALES")
print(yearly_sales)


plt.figure(figsize=(11, 6))

plt.plot(
    yearly_sales.index,
    yearly_sales.values,
    marker="o",
    linewidth=3
)

plt.title(
    "EV Sales Growth by Year"
)

plt.xlabel(
    "Year"
)

plt.ylabel(
    "Total EV Sales"
)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()


# ==========================================
# 2. YEAR-OVER-YEAR GROWTH
# ==========================================

yearly_growth = (
    yearly_sales.pct_change() * 100
)

print("\n📊 YEAR-OVER-YEAR GROWTH (%)")

print(
    yearly_growth.round(2)
)


# ==========================================
# 3. BRAND MARKET SHARE
# ==========================================

brand_market_share = (
    brand_sales / brand_sales.sum()
) * 100

brand_market_share = (
    brand_market_share
    .sort_values(
        ascending=False
    )
)

print("\n🏆 BRAND MARKET SHARE (%)")

print(
    brand_market_share.round(2)
)


plt.figure(figsize=(11, 6))

plt.bar(
    brand_market_share.index,
    brand_market_share.values
)

plt.title(
    "EV Brand Market Share"
)

plt.xlabel(
    "Brand"
)

plt.ylabel(
    "Market Share (%)"
)

plt.xticks(
    rotation=45
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.show()


# ==========================================
# 4. PRICE VS RANGE
# ==========================================

plt.figure(figsize=(11, 6))

plt.scatter(
    df["Price"],
    df["Range_km"],
    alpha=0.5
)

plt.title(
    "EV Price vs Driving Range"
)

plt.xlabel(
    "Price ($)"
)

plt.ylabel(
    "Driving Range (km)"
)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()


# ==========================================
# 5. BATTERY VS RANGE
# ==========================================

plt.figure(figsize=(11, 6))

plt.scatter(
    df["Battery_kWh"],
    df["Range_km"],
    alpha=0.5
)

plt.title(
    "Battery Capacity vs Driving Range"
)

plt.xlabel(
    "Battery Capacity (kWh)"
)

plt.ylabel(
    "Driving Range (km)"
)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()


# ==========================================
# 6. CORRELATION ANALYSIS
# ==========================================

correlation = df[
    [
        "Price",
        "Battery_kWh",
        "Range_km",
        "Sales",
        "Charging_Time"
    ]
].corr()

print("\n🔗 CORRELATION MATRIX")

print(
    correlation.round(2)
)


# ==========================================
# 7. BEST VALUE EV
# ==========================================

df["Range_per_Dollar"] = (
    df["Range_km"]
    / df["Price"]
)

best_value = (
    df.sort_values(
        "Range_per_Dollar",
        ascending=False
    )
    .head(10)
)

print("\n💰 TOP 10 BEST VALUE EV RECORDS")

print(
    best_value[
        [
            "Brand",
            "Model",
            "Price",
            "Range_km",
            "Battery_kWh",
            "Range_per_Dollar"
        ]
    ]
)


# ==========================================
# 8. BEST RANGE EVs
# ==========================================

best_range = (
    df.sort_values(
        "Range_km",
        ascending=False
    )
    .head(10)
)

print("\n🔋 TOP 10 EVs BY RANGE")

print(
    best_range[
        [
            "Brand",
            "Model",
            "Range_km",
            "Battery_kWh",
            "Price"
        ]
    ]
)


# ==========================================
# 9. MOST AFFORDABLE EVs
# ==========================================

affordable_evs = (
    df.sort_values(
        "Price"
    )
    .head(10)
)

print("\n💵 TOP 10 AFFORDABLE EVs")

print(
    affordable_evs[
        [
            "Brand",
            "Model",
            "Price",
            "Range_km",
            "Battery_kWh"
        ]
    ]
)


# ==========================================
# 10. BRAND PERFORMANCE
# ==========================================

brand_performance = (
    df.groupby("Brand")
    .agg(
        Total_Sales=("Sales", "sum"),
        Average_Price=("Price", "mean"),
        Average_Range=("Range_km", "mean"),
        Average_Battery=("Battery_kWh", "mean")
    )
    .sort_values(
        "Total_Sales",
        ascending=False
    )
)

print("\n🏭 BRAND PERFORMANCE")

print(
    brand_performance.round(2)
)


# ==========================================
# 11. BRAND RANGE COMPARISON
# ==========================================

plt.figure(figsize=(11, 6))

plt.bar(
    brand_performance.index,
    brand_performance["Average_Range"]
)

plt.title(
    "Average Driving Range by Brand"
)

plt.xlabel(
    "Brand"
)

plt.ylabel(
    "Average Range (km)"
)

plt.xticks(
    rotation=45
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.show()


# ==========================================
# 12. PREMIUM VS AFFORDABLE
# ==========================================

df["Price_Category"] = np.where(
    df["Price"] < 40000,
    "Affordable",
    np.where(
        df["Price"] < 80000,
        "Mid-Range",
        "Premium"
    )
)

price_category_sales = (
    df.groupby("Price_Category")["Sales"]
    .sum()
    .sort_values(
        ascending=False
    )
)

print("\n💰 PRICE CATEGORY SALES")

print(
    price_category_sales
)


plt.figure(figsize=(9, 6))

plt.bar(
    price_category_sales.index,
    price_category_sales.values
)

plt.title(
    "EV Sales by Price Category"
)

plt.xlabel(
    "Price Category"
)

plt.ylabel(
    "Sales"
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.show()


# ==========================================
# 13. COUNTRY + BRAND ANALYSIS
# ==========================================

country_brand_sales = pd.pivot_table(
    df,
    values="Sales",
    index="Country",
    columns="Brand",
    aggfunc="sum",
    fill_value=0
)

print("\n🌎 COUNTRY-BRAND SALES")

print(
    country_brand_sales
)


# ==========================================
# 14. TOP COUNTRY
# ==========================================

top_country = country_sales.idxmax()

top_country_sales = country_sales.max()

print("\n🌎 TOP EV MARKET")

print(
    f"Country: {top_country}"
)

print(
    f"Sales: {top_country_sales:,}"
)


# ==========================================
# 15. TOP BRAND
# ==========================================

top_brand = brand_sales.idxmax()

top_brand_sales = brand_sales.max()

print("\n🏆 TOP EV BRAND")

print(
    f"Brand: {top_brand}"
)

print(
    f"Sales: {top_brand_sales:,}"
)


# ==========================================
# 16. BEST RANGE BRAND
# ==========================================

best_range_brand = (
    brand_performance[
        "Average_Range"
    ]
    .idxmax()
)

best_range_value = (
    brand_performance[
        "Average_Range"
    ].max()
)

print("\n🔋 BEST RANGE BRAND")

print(
    f"Brand: {best_range_brand}"
)

print(
    f"Average Range: "
    f"{best_range_value:.1f} km"
)


# ==========================================
# 17. BUSINESS INSIGHTS
# ==========================================

print("\n" + "=" * 65)
print("💡 AUTOMATED BUSINESS INSIGHTS")
print("=" * 65)

print(
    f"🏆 Leading EV Brand: {top_brand}"
)

print(
    f"🌎 Leading EV Market: {top_country}"
)

print(
    f"🔋 Best Average Range Brand: "
    f"{best_range_brand}"
)

print(
    f"💰 Highest Average EV Price: "
    f"{df.groupby('Brand')['Price'].mean().idxmax()}"
)

print(
    f"⚡ Highest Average Battery Brand: "
    f"{df.groupby('Brand')['Battery_kWh'].mean().idxmax()}"
)

print(
    f"📈 Best EV Model by Range: "
    f"{df.loc[df['Range_km'].idxmax(), 'Model']}"
)

print(
    f"💵 Most Affordable EV Model: "
    f"{df.loc[df['Price'].idxmin(), 'Model']}"
)


# ==========================================
# SAVE ADVANCED DATA
# ==========================================

brand_performance.to_csv(
    "brand_performance.csv"
)

yearly_sales.to_csv(
    "yearly_ev_sales.csv"
)

brand_market_share.to_csv(
    "brand_market_share.csv"
)

best_value.to_csv(
    "best_value_evs.csv",
    index=False
)

print("\n" + "=" * 65)
print("✅ PART 2 COMPLETED")
print("=" * 65)

print("Advanced analytics files saved successfully.")
# ==========================================
# PART 3 - FINAL EV MARKET DASHBOARD
# ==========================================

print("\n" + "=" * 70)
print("🚗⚡ CREATING EV MARKET INTELLIGENCE DASHBOARD")
print("=" * 70)

# ==========================================
# DASHBOARD DATA
# ==========================================

# Top brands
top_brand_data = (
    df.groupby("Brand")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Top models
top_model_data = (
    df.groupby("Model")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Yearly sales
year_data = (
    df.groupby("Year")["Sales"]
    .sum()
    .sort_index()
)

# Country sales
country_data = (
    df.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Vehicle type
vehicle_data = (
    df.groupby("Vehicle_Type")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Price category
price_data = (
    df.groupby("Price_Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# ==========================================
# CREATE FIGURE
# ==========================================

fig = plt.figure(
    figsize=(20, 12)
)

fig.suptitle(
    "🚗⚡ EV MARKET INTELLIGENCE DASHBOARD",
    fontsize=24,
    fontweight="bold",
    y=0.98
)

# ==========================================
# KPI CARDS
# ==========================================

kpis = [
    (
        "TOTAL SALES",
        f"{total_sales / 1e6:.2f}M"
    ),
    (
        "EV MODELS",
        f"{total_models}"
    ),
    (
        "BRANDS",
        f"{total_brands}"
    ),
    (
        "AVG PRICE",
        f"${average_price:,.0f}"
    ),
    (
        "AVG RANGE",
        f"{average_range:.0f} km"
    ),
    (
        "AVG BATTERY",
        f"{average_battery:.0f} kWh"
    )
]

kpi_positions = [
    0.08,
    0.245,
    0.41,
    0.575,
    0.74,
    0.905
]

for (title, value), position in zip(
    kpis,
    kpi_positions
):

    fig.text(
        position,
        0.875,
        f"{title}\n{value}",
        ha="center",
        va="center",
        fontsize=13,
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.7",
            facecolor="white",
            edgecolor="black",
            linewidth=1.5
        )
    )


# ==========================================
# CHART 1
# YEARLY SALES TREND
# ==========================================

ax1 = fig.add_axes(
    [0.05, 0.52, 0.28, 0.27]
)

ax1.plot(
    year_data.index,
    year_data.values,
    marker="o",
    linewidth=3
)

ax1.set_title(
    "📈 EV Sales Growth"
)

ax1.set_xlabel(
    "Year"
)

ax1.set_ylabel(
    "Sales"
)

ax1.grid(
    alpha=0.3
)


# ==========================================
# CHART 2
# BRAND SALES
# ==========================================

ax2 = fig.add_axes(
    [0.36, 0.52, 0.28, 0.27]
)

top_brands = top_brand_data.head(7)

ax2.bar(
    top_brands.index,
    top_brands.values
)

ax2.set_title(
    "🏆 Top EV Brands"
)

ax2.set_xlabel(
    "Brand"
)

ax2.set_ylabel(
    "Sales"
)

ax2.tick_params(
    axis="x",
    rotation=35
)

ax2.grid(
    axis="y",
    alpha=0.3
)


# ==========================================
# CHART 3
# COUNTRY SALES
# ==========================================

ax3 = fig.add_axes(
    [0.67, 0.52, 0.28, 0.27]
)

ax3.barh(
    country_data.index,
    country_data.values
)

ax3.set_title(
    "🌎 EV Sales by Country"
)

ax3.set_xlabel(
    "Sales"
)

ax3.invert_yaxis()

ax3.grid(
    axis="x",
    alpha=0.3
)


# ==========================================
# CHART 4
# PRICE VS RANGE
# ==========================================

ax4 = fig.add_axes(
    [0.05, 0.16, 0.28, 0.27]
)

ax4.scatter(
    df["Price"],
    df["Range_km"],
    alpha=0.5
)

ax4.set_title(
    "💰 Price vs Driving Range"
)

ax4.set_xlabel(
    "Price ($)"
)

ax4.set_ylabel(
    "Range (km)"
)

ax4.grid(
    alpha=0.3
)


# ==========================================
# CHART 5
# VEHICLE TYPE
# ==========================================

ax5 = fig.add_axes(
    [0.36, 0.16, 0.28, 0.27]
)

ax5.bar(
    vehicle_data.index,
    vehicle_data.values
)

ax5.set_title(
    "🚙 Sales by Vehicle Type"
)

ax5.set_xlabel(
    "Vehicle Type"
)

ax5.set_ylabel(
    "Sales"
)

ax5.tick_params(
    axis="x",
    rotation=25
)

ax5.grid(
    axis="y",
    alpha=0.3
)


# ==========================================
# CHART 6
# PRICE SEGMENT
# ==========================================

ax6 = fig.add_axes(
    [0.67, 0.16, 0.28, 0.27]
)

ax6.bar(
    price_data.index,
    price_data.values
)

ax6.set_title(
    "💵 Sales by Price Segment"
)

ax6.set_xlabel(
    "Price Category"
)

ax6.set_ylabel(
    "Sales"
)

ax6.grid(
    axis="y",
    alpha=0.3
)


# ==========================================
# FOOTER
# ==========================================

fig.text(
    0.5,
    0.045,
    "Python • Pandas • NumPy • Matplotlib | "
    "EV Market Analytics | Synthetic Educational Dataset",
    ha="center",
    fontsize=11
)


# ==========================================
# SAVE DASHBOARD
# ==========================================

plt.savefig(
    "ev_market_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================
# FINAL INSIGHTS
# ==========================================

best_brand = top_brand_data.idxmax()

best_country = country_data.idxmax()

best_vehicle_type = vehicle_data.idxmax()

best_price_segment = price_data.idxmax()

best_range_model = df.loc[
    df["Range_km"].idxmax(),
    "Model"
]

best_value_model = df.loc[
    df["Range_per_Dollar"].idxmax(),
    "Model"
]

most_expensive_model = df.loc[
    df["Price"].idxmax(),
    "Model"
]


print("\n")
print("=" * 70)
print("💡 EV MARKET BUSINESS INSIGHTS")
print("=" * 70)

print(
    f"🏆 Leading EV Brand       : {best_brand}"
)

print(
    f"🌎 Leading EV Market      : {best_country}"
)

print(
    f"🚙 Best Selling Vehicle   : {best_vehicle_type}"
)

print(
    f"💰 Strongest Price Segment: {best_price_segment}"
)

print(
    f"🔋 Best Range Model       : {best_range_model}"
)

print(
    f"💎 Best Value Model       : {best_value_model}"
)

print(
    f"💵 Most Expensive Model   : {most_expensive_model}"
)

print(
    f"📈 Highest Sales Year     : "
    f"{year_data.idxmax()}"
)

print("=" * 70)


# ==========================================
# SAVE INSIGHTS
# ==========================================

with open(
    "ev_business_insights.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "EV MARKET INTELLIGENCE - BUSINESS INSIGHTS\n"
    )

    file.write(
        "=" * 60 + "\n"
    )

    file.write(
        f"Leading EV Brand: {best_brand}\n"
    )

    file.write(
        f"Leading EV Market: {best_country}\n"
    )

    file.write(
        f"Best Selling Vehicle Type: "
        f"{best_vehicle_type}\n"
    )

    file.write(
        f"Best Price Segment: "
        f"{best_price_segment}\n"
    )

    file.write(
        f"Best Range Model: "
        f"{best_range_model}\n"
    )

    file.write(
        f"Best Value Model: "
        f"{best_value_model}\n"
    )

    file.write(
        f"Highest Sales Year: "
        f"{year_data.idxmax()}\n"
    )


print("\n✅ FINAL DASHBOARD CREATED!")
print(
    "📸 File: ev_market_dashboard.png"
)

print(
    "📄 File: ev_business_insights.txt"
)
