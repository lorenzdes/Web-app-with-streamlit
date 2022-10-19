from re import S
import streamlit as st
import yfinance as fn

st.write( """
My first app with streamlit""")
st.title("Stock Market App with *streamlit*")
st.header("Simple Data Science web app")
st.sidebar.header("Bek Brace \n Code along with me ...")

# This is a function that fetches the company ticker
def get_ticker(name):
    company = fn.Ticker(name)
    return company

company_1= get_ticker("AAPL")
company_2 = get_ticker("MSFT")
company_3 = get_ticker("TSLA")

# fetch data for df
apple = fn.download("AAPL", start = "2022-10-19", end = "2022-10-19")
microsoft = fn.download("MSFT", start = "2022-10-19", end = "2022-10-19")
tesla = fn.download("TSLA", start = "2022-10-19", end = "2022-10-19")

# fetch data by period (1d, 5d, 1mo,..)
data1 = company_1.history(period = "3mo")
data2 = company_2.history(period = "3mo")
data3 = company_3.history(period = "3mo")

# Markdown
st.write("""### Apple """)
# Detailed summary about apple
st.write(company_1.info['longBusinessSummary'])
st.write(apple)
st.line_chart(data1.values)

st.write("""### Microsoft """)
# Detailed summary about apple
st.write(company_2.info['longBusinessSummary'])
st.write(microsoft)
st.line_chart(data2.values)

st.write("""### Tesla """)
# Detailed summary about apple
st.write(company_3.info['longBusinessSummary'])
st.write(tesla)
st.line_chart(data3.values)


