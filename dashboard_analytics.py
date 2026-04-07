"""
LÉIA Analytics Dashboard
Business intelligence dashboard for client insights and sales analytics
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(
    page_title="LÉIA Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# =============================================
# COLLECTION COLOR PALETTE (consistent across ALL charts)
# =============================================
COLLECTION_COLORS = {
    'Eclipse':  '#F5C518',
    'Hatching': '#A855F7',
    'Amazon':   '#10B981',
    'Vanta':    '#64748B',
}

CITY_COLORS = ['#F97316', '#FB923C', '#FDBA74', '#FED7AA']  # Orange/amber for cities

# =============================================
# LOAD DATA
# =============================================
@st.cache_data
def load_data():
    kb_path = Path("knowledge_base")

    clients = pd.read_csv(kb_path / "client_profiles.csv", encoding='ISO-8859-1')
    clients = clients[~clients['client_id'].astype(str).str.startswith('#')]
    clients = clients.dropna(subset=['client_id'])

    purchases = pd.read_csv(kb_path / "purchase_history.csv", encoding='ISO-8859-1')
    purchases = purchases[~purchases['transaction_id'].astype(str).str.startswith('#')]
    purchases = purchases.dropna(subset=['transaction_id'])

    products = pd.read_csv(kb_path / "leia_products.csv", encoding='ISO-8859-1')
    products = products[~products['product_id'].astype(str).str.startswith('#')]
    products = products.dropna(subset=['product_id'])

    purchases['date'] = pd.to_datetime(purchases['date'], errors='coerce')
    clients['last_visit_date'] = pd.to_datetime(clients['last_visit_date'], errors='coerce')

    return clients, purchases, products

try:
    clients_df, purchases_df, products_df = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# =============================================
# SIDEBAR FILTERS
# =============================================
st.sidebar.header("🔍 Filters")

cities = ['All'] + sorted(clients_df['city'].dropna().unique().tolist())
selected_city = st.sidebar.selectbox("City", cities)

tiers = ['All'] + sorted(clients_df['vip_tier'].dropna().unique().tolist())
selected_tier = st.sidebar.selectbox("VIP Tier", tiers)

collections = ['All'] + sorted(products_df['collection'].dropna().unique().tolist())
selected_collection = st.sidebar.selectbox("Collection", collections)

st.sidebar.markdown("### Date Range")
min_date = purchases_df['date'].dropna().min()
max_date = purchases_df['date'].dropna().max()
date_range = st.sidebar.date_input(
    "Purchase Period",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Apply filters
filtered_clients = clients_df.copy()
if selected_city != 'All':
    filtered_clients = filtered_clients[filtered_clients['city'] == selected_city]
if selected_tier != 'All':
    filtered_clients = filtered_clients[filtered_clients['vip_tier'] == selected_tier]

filtered_purchases = purchases_df.copy()
if len(date_range) == 2:
    filtered_purchases = filtered_purchases[
        filtered_purchases['date'].notna() &
        (filtered_purchases['date'] >= pd.to_datetime(date_range[0])) &
        (filtered_purchases['date'] <= pd.to_datetime(date_range[1]))
    ]
if selected_collection != 'All':
    filtered_purchases = filtered_purchases[filtered_purchases['collection'] == selected_collection]

filtered_purchases = filtered_purchases[
    filtered_purchases['client_id'].isin(filtered_clients['client_id'])
]

# =============================================
# TITLE
# =============================================
st.title("LÉIA Analytics Dashboard")
st.markdown("Business intelligence for luxury retail")

# =============================================
# KPIs
# =============================================
st.markdown("---")
st.subheader("📈 Key Performance Indicators")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Clients", len(filtered_clients))

with col2:
    total_revenue = filtered_purchases['price_usd'].sum()
    st.metric("Total Revenue", f"${total_revenue:,.0f}")

with col3:
    avg_transaction = filtered_purchases['price_usd'].mean() if len(filtered_purchases) > 0 else 0
    st.metric("Avg Transaction", f"${avg_transaction:,.0f}")

with col4:
    total_clients = len(filtered_clients)
    vip_clients = len(filtered_clients[filtered_clients['vip_tier'].isin(['Platinum', 'Diamond'])])
    vip_pct = (vip_clients / total_clients * 100) if total_clients > 0 else 0
    st.metric("VIP Clients", f"{vip_clients}", f"{vip_pct:.1f}%")

with col5:
    st.metric("Total Purchases", len(filtered_purchases))

# =============================================
# ROW 1 : Revenue by Collection | City charts (all view) and Top 5 Best-selling Products (city view)
# =============================================
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Revenue by Collection")
    rev_col = filtered_purchases.groupby('collection')['price_usd'].sum().reset_index()
    rev_col = rev_col.sort_values('price_usd', ascending=False)

    fig_col = px.bar(
        rev_col,
        x='collection',
        y='price_usd',
        color='collection',
        color_discrete_map=COLLECTION_COLORS,
        labels={'price_usd': 'Revenue (USD)', 'collection': 'Collection'},
    )
    fig_col.update_layout(showlegend=False, height=400)
    st.plotly_chart(fig_col, use_container_width=True)

with col2:
    if selected_city == 'All':
        # ALL CITIES → Bar chart Revenue by City
        st.subheader("🏙️ Revenue by City")
        rev_city = filtered_purchases.groupby('boutique_city')['price_usd'].sum().reset_index()
        rev_city = rev_city.sort_values('price_usd', ascending=False)

        fig_rev_city = px.bar(
            rev_city,
            x='boutique_city',
            y='price_usd',
            color='boutique_city',
            labels={'price_usd': 'Revenue (USD)', 'boutique_city': 'City'},
            color_discrete_sequence=CITY_COLORS
        )
        fig_rev_city.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig_rev_city, use_container_width=True)

    else:
        # SPECIFIC CITY → Top 5 Best-selling Products
        st.subheader(f"Top 5 Best-selling Products — {selected_city}")

        top_5_city = (
            filtered_purchases
            .groupby(['product_name', 'collection'])
            .size()
            .reset_index(name='sales')
            .sort_values('sales', ascending=False)
            .head(5)
        )
        
        fig_top5_city = px.bar(
            top_5_city,
            x='sales',
            y='product_name',
            color='collection',
            color_discrete_map=COLLECTION_COLORS,
            orientation='h',
            labels={'sales': 'Sales', 'product_name': '', 'collection': 'Collection'},
        )
        
        fig_top5_city.update_layout(
            height=400,
            showlegend=True,
            xaxis_title='',
            yaxis=dict(
                autorange='reversed',
                tickfont=dict(size=9)
            ),
            margin=dict(l=5, r=20, t=10, b=0)
        )
        
        st.plotly_chart(fig_top5_city, use_container_width=True)

# =============================================
# ROW 2 : ALL : Clients by City | VIP Tier Distribution | CITY : VIP Tier Breakdown | Purchases Over Time
# =============================================
col1, col2 = st.columns(2)

with col1:
    if selected_city == 'All':
        # ALL CITIES → Pie chart Clients by City
        st.subheader("🌍 Clients by City")
        clients_city = filtered_clients.groupby('city').size().reset_index(name='count')

        fig_clients_city = px.pie(
            clients_city,
            values='count',
            names='city',
            color_discrete_sequence=['#1E3A5F', '#2D6A9F', '#5B9BD5', '#A8C8E8']
        )
        fig_clients_city.update_layout(height=400)
        st.plotly_chart(fig_clients_city, use_container_width=True)

    else:
        # SPECIFIC CITY → VIP Tier breakdown
        st.subheader(f"👑 VIP Tier Breakdown — {selected_city}")
        vip_dist = filtered_clients.groupby('vip_tier').size().reset_index(name='count')
        vip_order = ['Member', 'Gold', 'Platinum', 'Diamond']
        vip_dist['vip_tier'] = pd.Categorical(vip_dist['vip_tier'], categories=vip_order, ordered=True)
        vip_dist = vip_dist.sort_values('vip_tier')

        fig_vip_city = px.bar(
            vip_dist,
            x='vip_tier',
            y='count',
            color='vip_tier',
            labels={'count': 'Number of Clients', 'vip_tier': 'VIP Tier'},
            color_discrete_map={
                'Member':   '#94a3b8',
                'Gold':     '#fbbf24',
                'Platinum': '#cbd5e1',
                'Diamond':  '#3b82f6'
            }
        )
        fig_vip_city.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig_vip_city, use_container_width=True)

with col2:
    st.subheader("👑 VIP Tier Distribution" if selected_city == 'All' else "📅 Purchases Over Time")

    if selected_city == 'All':
        vip_dist = filtered_clients.groupby('vip_tier').size().reset_index(name='count')
        vip_order = ['Member', 'Gold', 'Platinum', 'Diamond']
        vip_dist['vip_tier'] = pd.Categorical(vip_dist['vip_tier'], categories=vip_order, ordered=True)
        vip_dist = vip_dist.sort_values('vip_tier')

        fig_vip = px.bar(
            vip_dist,
            x='vip_tier',
            y='count',
            color='vip_tier',
            labels={'count': 'Number of Clients', 'vip_tier': 'VIP Tier'},
            color_discrete_map={
                'Member':   '#94a3b8',
                'Gold':     '#fbbf24',
                'Platinum': '#cbd5e1',
                'Diamond':  '#3b82f6'
            }
        )
        fig_vip.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig_vip, use_container_width=True)

    else:
        purch_time = filtered_purchases[filtered_purchases['date'].notna()].copy()
        purch_time = purch_time.groupby(purch_time['date'].dt.to_period('M')).size().reset_index(name='count')
        purch_time['date'] = purch_time['date'].dt.to_timestamp()

        fig_time = px.line(
            purch_time, x='date', y='count',
            labels={'count': 'Number of Purchases', 'date': 'Month'},
            markers=True
        )
        fig_time.update_traces(line_color='#8b5cf6', line_width=2)
        fig_time.update_layout(height=400)
        st.plotly_chart(fig_time, use_container_width=True)

# =============================================
# ROW 3 All cities view only : Purchases Over Time | Top 5 Best-selling Products by Collection
# =============================================
if selected_city == 'All':
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📅 Purchases Over Time")
        purch_time = filtered_purchases[filtered_purchases['date'].notna()].copy()
        purch_time = purch_time.groupby(purch_time['date'].dt.to_period('M')).size().reset_index(name='count')
        purch_time['date'] = purch_time['date'].dt.to_timestamp()

        fig_time = px.line(
            purch_time, x='date', y='count',
            labels={'count': 'Number of Purchases', 'date': 'Month'},
            markers=True
        )
        fig_time.update_traces(line_color='#8b5cf6', line_width=2)
        fig_time.update_layout(height=400)
        st.plotly_chart(fig_time, use_container_width=True)

    with col2:
        st.subheader("🏆 Top 5 Best-Selling Products")
        top_5_products = (
            filtered_purchases
            .groupby(['product_name', 'collection'])
            .size()
            .reset_index(name='sales')
            .sort_values('sales', ascending=False)
            .head(5)
            )
    
    # Create horizontal bar chart
        fig_top5 = px.bar(
            top_5_products,
            x='sales',
            y='product_name',
            color='collection',
            color_discrete_map=COLLECTION_COLORS,
            orientation='h',
            labels={'sales': 'Number of Sales', 'product_name': '', 'collection': 'Collection'},
            text='sales'
            )
    
        fig_top5.update_traces(
            texttemplate='%{text} sales',
            textposition='outside',
            textfont_size=10
            )
    
        fig_top5.update_layout(
            height=400,
            showlegend=True,
            legend_title_text='Collection',
            xaxis_title='Sales Volume',
            yaxis=dict(autorange='reversed',side='left',tickmode='linear', tickfont=dict(size=9)),
            margin=dict(l=5, r=20, t=10, b=0)
            )
        st.plotly_chart(fig_top5, use_container_width=True)

    # =============================================
    # ROW 3 CITY view only: Top 5 Products by Collection
    # ROW 4 ALL cities view only : Top 5 Products by Collection
    # =============================================
    st.subheader("🗺️ Top 5 Products by Collection")
    
    # Get product sales data
    sales_product = (
        filtered_purchases
        .groupby(['collection', 'product_name'])
        .size()
        .reset_index(name='count')
        .sort_values(['collection', 'count'], ascending=[True, False])
    )
    
    # Get top 5 products per collection
    top_products = (
        sales_product
        .groupby('collection')
        .apply(lambda x: x.nlargest(5, 'count'))
        .reset_index(drop=True)
    )
    
    # Shorten product names for display
    top_products['short_name'] = top_products['product_name'].str.split().str[:2].str.join(' ')
    
    # Create stacked bar
    fig_stacked_products = px.bar(
        top_products,
        x='collection',
        y='count',
        color='product_name',
        text='short_name',
        labels={'count': 'Number of Sales', 'collection': 'Collection'},
        color_discrete_sequence=px.colors.qualitative.Set3,
        hover_data={'product_name': True, 'count': True, 'short_name': False}
    )
    
    # Show labels only on segments tall enough
    fig_stacked_products.update_traces(
        texttemplate='%{text}<br>%{y}',
        textposition='inside',
        textfont_size=9,
        hovertemplate='<b>%{customdata[0]}</b><br>Sales: %{y}<extra></extra>',
        insidetextanchor='middle'
    )
    
    # Hide text on small segments
    fig_stacked_products.update_layout(
        height=500,
        showlegend=False,
        xaxis_title='Collection',
        yaxis_title='Total Sales',
        uniformtext_minsize=8,
        uniformtext_mode='hide'  # Cache automatiquement si trop petit
    )
    
    st.plotly_chart(fig_stacked_products, use_container_width=True)

else:
    # City view: show stacked bar full width
    st.markdown("---")
    st.subheader(f"🗺️ Top 5 Products by Collection — {selected_city}")
    
    # Get product sales data
    sales_product = (
        filtered_purchases
        .groupby(['collection', 'product_name'])
        .size()
        .reset_index(name='count')
        .sort_values(['collection', 'count'], ascending=[True, False])
    )
    
    # Get top 5 products per collection
    top_products = (
        sales_product
        .groupby('collection')
        .apply(lambda x: x.nlargest(5, 'count'))
        .reset_index(drop=True)
    )
    
    # Shorten product names for display
    top_products['short_name'] = top_products['product_name'].str.split().str[:2].str.join(' ')
    
    # Create stacked bar
    fig_stacked_city = px.bar(
        top_products,
        x='collection',
        y='count',
        color='product_name',
        text='short_name',
        labels={'count': 'Number of Sales', 'collection': 'Collection'},
        color_discrete_sequence=px.colors.qualitative.Set3,
        hover_data={'product_name': True, 'count': True, 'short_name': False}
    )
    
    # Show labels only on segments tall enough
    fig_stacked_city.update_traces(
        texttemplate='%{text}<br>%{y}',
        textposition='inside',
        textfont_size=9,
        hovertemplate='<b>%{customdata[0]}</b><br>Sales: %{y}<extra></extra>',
        insidetextanchor='middle'
    )
    
    # Hide text on small segments
    fig_stacked_city.update_layout(
        height=450,
        showlegend=False,
        xaxis_title='Collection',
        yaxis_title='Total Sales',
        uniformtext_minsize=8,
        uniformtext_mode='hide'
    )
    
    st.plotly_chart(fig_stacked_city, use_container_width=True)

# =============================================
# TOP CLIENTS TABLE
# =============================================
st.markdown("---")
st.subheader("🌟 Top Clients by Spending")

top_clients = filtered_clients.nlargest(10, 'total_spent_usd')[[
    'first_name', 'last_name', 'city', 'vip_tier',
    'total_spent_usd', 'purchase_count', 'preferred_collections'
]].copy()
top_clients.columns = ['First Name', 'Last Name', 'City', 'VIP Tier', 'Total Spent ($)', 'Purchases', 'Preferred Collections']
top_clients['Total Spent ($)'] = top_clients['Total Spent ($)'].apply(lambda x: f"${x:,.0f}")
st.dataframe(top_clients, use_container_width=True, hide_index=True)

# =============================================
# RECENT PURCHASES TABLE
# =============================================
st.markdown("---")
st.subheader("🛒 Recent Purchases")

recent = filtered_purchases.nlargest(15, 'date')[[
    'date', 'client_id', 'product_name', 'collection', 'price_usd', 'boutique_city', 'advisor_name'
]].copy()
recent.columns = ['Date', 'Client ID', 'Product', 'Collection', 'Price ($)', 'Boutique', 'Advisor']
recent['Date'] = recent['Date'].dt.strftime('%Y-%m-%d')
recent['Price ($)'] = recent['Price ($)'].apply(lambda x: f"${x:,.0f}")
st.dataframe(recent, use_container_width=True, hide_index=True)

# =============================================
# ADVISOR PERFORMANCE
# =============================================
st.markdown("---")
st.subheader("👔 Advisor Performance")

advisor_stats = filtered_purchases.groupby('advisor_name').agg(
    Total_Sales=('transaction_id', 'count'),
    Total_Revenue=('price_usd', 'sum'),
    Avg_Transaction=('price_usd', 'mean')
).reset_index().sort_values('Total_Revenue', ascending=False)

advisor_stats.columns = ['Advisor', 'Total Sales', 'Total Revenue', 'Avg Transaction']
advisor_stats['Total Revenue'] = advisor_stats['Total Revenue'].apply(lambda x: f"${x:,.0f}")
advisor_stats['Avg Transaction'] = advisor_stats['Avg Transaction'].apply(lambda x: f"${x:,.0f}")
st.dataframe(advisor_stats, use_container_width=True, hide_index=True)

# =============================================
# COLLECTION INSIGHTS
# =============================================
st.markdown("---")
st.subheader("💎 Collection Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Average Price by Collection**")
    avg_price = products_df.groupby('collection')['price_usd'].mean().reset_index()
    avg_price = avg_price.sort_values('price_usd', ascending=False)
    avg_price['price_usd'] = avg_price['price_usd'].apply(lambda x: f"${x:,.0f}")
    avg_price.columns = ['Collection', 'Avg Price']
    st.dataframe(avg_price, hide_index=True)

with col2:
    st.markdown("**Products per Collection**")
    prod_count = products_df.groupby('collection').size().reset_index(name='count')
    prod_count = prod_count.sort_values('count', ascending=False)
    prod_count.columns = ['Collection', 'Product Count']
    st.dataframe(prod_count, hide_index=True)

st.markdown("---")
st.markdown("*LÉIA Analytics Dashboard • Data updated in real-time from knowledge base*")
