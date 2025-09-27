import streamlit as st

import yfinance as yf
st.title('Stock Price App')
st.write('''Below shown are the stock Prices og Google''')
tickersymbol='GOOGL'
tickerdata= yf.Ticker(tickersymbol)
st.text_input('Enter Stock Ticker', 'GOOGL')
a=st.date_input("Enter start date ")
b=st.date_input("Enter end date ")
tickerDf= tickerdata.history( start=a, end=b)
st.write("Closing Price")
st.line_chart(tickerDf.Close)
st.write("Volume")
st.line_chart(tickerDf.Volume)