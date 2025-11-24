# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot 




df=pd.read_csv(r'E:\ProjectsFinal\DataAnalysis_Python\Project2_Bitcoin Data Analysis\Bitcoin/bitcoin_price_Training - Training.csv')

df['Date']=df['Date'].astype('datetime64[ns]') 
data=df.sort_index(ascending=False).reset_index()
data.drop('index',axis=1,inplace=True)
data.set_index('Date',inplace=True)
data['close_price_pct_change']=data['Close'].pct_change()*100 

bitcoin_sample=data[0:100]

st.set_page_config(page_title='Bitcoin Dashboard',
                   layout='wide')

st.title('Comprehensive Bitcoin Price Analysis Dashboard')


## 1st plot :


st.subheader('Bitcoin Candlestick Chart(First 100 Days')  

trace=go.Candlestick(x=bitcoin_sample.index,
               high=bitcoin_sample['High'],
               open=bitcoin_sample['Open'],
               low=bitcoin_sample['Low'],
               close=bitcoin_sample['Close'])    

candle_data=[trace]
layout= {
              'title':'Bitcoin Historical Price',
              'xaxis':{'title':'Date'}                                
}

fig_candle=go.Figure(data=candle_data,layout=layout)    
fig_candle.update_layout(
                yaxis_title='Price (USD)',
                xaxis_rangeslider_visible=False,
                  width=1000,
                height=600 ) 
                   # to remove the slider



st.plotly_chart(fig_candle,use_container_width=True )  #to render plotly chart in streamlit application
  
    #to run this file open anaconda terminal and run streamlit run C:/Users/palla/.spyder-py3/temp.py
    #as streamline did not run directly in spider .
    

## 2nd Plot

st.subheader("Daily Percentange Change in Closing Price")

fig_pct=go.Figure([
    go.Scatter(x=data.index,
               y=data['close_price_pct_change'],
               mode="lines",
               name="Close % Change")
])

fig_pct.update_layout(
     title="Daily % Change in Close Price",
    xaxis_title="Date",
    yaxis_title="Percentage_change",
    template="plotly_white"
    )

st.plotly_chart(fig_pct,use_container_width= True)



## 3rd plot :
    
st.subheader("Bitcoin Price Trends Over Time ")
price_type=st.selectbox("Select Price Type:",options=['Open', 'High', 'Low', 'Close'],index=3)


fig_trend=go.Figure([
    go.Scatter(x=data.index,
               y=data[price_type],
               mode="lines",
                name=price_type)
])    

fig_trend.update_layout(
    title=f"{price_type} Price Over Time",
    xaxis_title="Date",
    yaxis_title="Price(USD)",
    template="plotly_white"
    )

st.plotly_chart(fig_trend,use_container_width= True)



## 4th plot :
    
col1,col2,col3=st.columns(3)

with col1:
    st.subheader("Yearly Average close Price ")
    yearly_avg=data['Close'].resample('YE').mean()
    fig_year=px.bar(
        x=yearly_avg.index.strftime('%Y'),
        y=yearly_avg.values,
        labels={'x':'year','y':'Average value'},
        title='Yearly avg Trend'
        
        )
    st.plotly_chart(fig_year,use_container_width= True)
    
    
with col2:
    st.subheader("Quarterly Average Close Price")
    quarterly_avg = data['Close'].resample('Q').mean()
    # Convert to "YYYY-Qn" format
    quarters = quarterly_avg.index.to_period("Q").astype(str)
    fig_quarter = px.bar(
        x=quarters,
        y=quarterly_avg.values,
        labels={'x': 'Quarter', 'y': 'Average Close Price'},
        title='Quarterly Average Close Price Trend'
    )
    st.plotly_chart(fig_quarter, use_container_width=True)

# ---- Monthly ----
with col3:
    st.subheader("Monthly Average Close Price")
    monthly_avg = data['Close'].resample('M').mean()
    # Format as "YYYY-MM"
    months = monthly_avg.index.strftime('%Y-%m')
    fig_month = px.line(
        x=months,
        y=monthly_avg.values,
        labels={'x': 'Month', 'y': 'Average Close Price'},
        title='Monthly Average Close Price Trend'
    )
    st.plotly_chart(fig_month, use_container_width=True)    
    
    
## 5th plot :
    
col4,col5=st.columns(2)

with col4:
    st.subheader("Closing Price(Normal Scale) ")
    fig_normal=px.line(
        data_frame=data,
        x=data.index,
        y='Close',
        labels={'x':'Date','Close':'Closing Price'},
        title='Bitcoin Closing Price Trend (Normal Scale)'
        
        )
    st.plotly_chart(fig_normal,use_container_width= True)
    


with col5:
    st.subheader("Closing Price(Log Scale) ")
    fig_log=px.line(
        data_frame=data,
        x=data.index,
        y=np.log1p(data['Close']),
        labels={'x':'Date','Close':'log(Closing_price+1)'},
        title='Bitcoin Closing Price Trend (Log Scale)'
        
        )
    st.plotly_chart(fig_log,use_container_width= True)
    
    
    
## now open Anaconda powershell and nevigate to the folder then run streamlit run app.py    
    
    

    
    
    
    
    
    
        
    
    
    
    




    
