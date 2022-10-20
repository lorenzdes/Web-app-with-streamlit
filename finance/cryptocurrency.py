import streamlit as st
import yfinance as yf
from PIL import Image
from urllib.request import urlopen


# Titles and subtitles
st.title("Cryptocurrency Daily Prices")
st.header("Main Dashboard")
st.subheader("You can add more crypto in code")

# Defining ticker
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple = 'XRP-USD'
BitcoinCash = 'BCH-USD'

# Access data from Yahoo Finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)

# Fetch data from Yahoo
BTCHis = BTC_Data.history(period = 'max')
ETHHis = ETH_Data.history(period = 'max')
XRPHis = XRP_Data.history(period = 'max')
BCHHis = BCH_Data.history(period = 'max')

# Fetch cytpo Data for the dataframe
BTC = yf.download(Bitcoin, start = '2022-10-19', end = '2022-10-19')
ETH = yf.download(Ethereum, start = '2022-10-19', end = '2022-10-19')
XRP = yf.download(Ripple, start = '2022-10-19', end = '2022-10-19')
BCH = yf.download(BitcoinCash, start = '2022-10-19', end = '2022-10-19')

st.write("Bitcoin ($)")
imageBTC = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"))
# Display image
st.image(imageBTC)
# Display dataframe
st.table(BTC)
#Display a chart
st.bar_chart(BTCHis.Close)


st.write("Ethereum ($)")
imageETH = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"))
# Display image
st.image(imageETH)
# Display dataframe
st.table(ETH)
#Display a chart
st.bar_chart(ETHHis.Close)




st.write("Ripple ($)")
imageXRP = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/52.png"))
# Display image
st.image(imageXRP)
# Display dataframe
st.table(XRP)
#Display a chart
st.bar_chart(XRPHis.Close)


st.write("Bitcoin Cash ($)")
imageBCH = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png"))
# Display image
st.image(imageBCH)
# Display dataframe
st.table(BCH)
#Display a chart
st.bar_chart(BCHHis.Close)




