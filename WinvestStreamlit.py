import streamlit as st

def login():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password")

def dashboard():
    # Add your main dashboard content here

    import pandas as pd
    import numpy as np
    import yfinance as yf
    import plotly.express as px
    from yahoo_fin import stock_info as si
    from datetime import date
    from plotly import graph_objs as go

    st.title('Main Dashboard')
    st.write('The best overall dashboard with the basic you need to make a informed decision!')


    START = "2010-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    tickerSymbol = 'GOOGL'

    stocks = si.tickers_other()
    stocks1 = si.tickers_nasdaq()
    stocks2 = si.tickers_sp500()
    tickerData = yf.Ticker(tickerSymbol)
    # tickerDf = tickerData.history(period='1d', start = '2010-5-31', end='2020-5-31')
    stocks = si.tickers_other()
    stocks1 = si.tickers_nasdaq()
    stocks2 = si.tickers_sp500()
    # tickerDf = tickerData.history(period='1d', start = '2010-5-31', end='2020-5-31')
    stockstots = (stocks + stocks1 + stocks2)
    # STOCK FILTRATION
    gokli = list(filter(lambda k: '.W' not in k, stockstots))
    mokli = list(filter(lambda k: '.U' not in k, gokli))
    pokli = list(filter(lambda k: '$B' not in k, mokli))
    zokli = list(filter(lambda k: '$C' not in k, pokli))
    lokli = list(filter(lambda k: '$A' not in k, zokli))
    qokli = list(filter(lambda k: '$D' not in k, lokli))
    nokli = list(filter(lambda k: '$E' not in k, qokli))
    xokli = list(filter(lambda k: '$F' not in k, nokli))
    aokli = list(filter(lambda k: '.A' not in k, xokli))
    eokli = list(filter(lambda k: '.B' not in k, aokli))
    hokli = list(filter(lambda k: '$F' not in k, eokli))
    tokli = list(filter(lambda k: '$G' not in k, hokli))
    sokli = list(filter(lambda k: '$H' not in k, tokli))
    dokli = list(filter(lambda k: '$I' not in k, sokli))
    yokli = list(filter(lambda k: '$J' not in k, dokli))
    fix1 = list(filter(lambda k: '$K' not in k, yokli))
    fix2 = list(filter(lambda k: '$L' not in k, fix1))
    fix3 = list(filter(lambda k: '$M' not in k, fix2))
    fix4 = list(filter(lambda k: '$N' not in k, fix3))
    fix5 = list(filter(lambda k: '$O' not in k, fix4))
    fix6 = list(filter(lambda k: '$P' not in k, fix5))
    fix7 = list(filter(lambda k: '$Q' not in k, fix6))
    fix8 = list(filter(lambda k: '$R' not in k, fix7))
    fix9 = list(filter(lambda k: '$S' not in k, fix8))
    fix10 = list(filter(lambda k: '$T' not in k, fix9))
    fix11 = list(filter(lambda k: '$U' not in k, fix10))
    fix12 = list(filter(lambda k: '$V' not in k, fix11))
    fix13 = list(filter(lambda k: '$W' not in k, fix12))
    fix14 = list(filter(lambda k: '$X' not in k, fix13))
    fix15 = list(filter(lambda k: '$Y' not in k, fix14))
    fix16 = list(filter(lambda k: '$Z' not in k, fix15))
    fix17 = list(filter(lambda k: '.D' not in k, fix16))
    fix18 = list(filter(lambda k: '.E' not in k, fix17))
    fix19 = list(filter(lambda k: '.F' not in k, fix18))
    fix20 = list(filter(lambda k: '.G' not in k, fix19))
    fix21 = list(filter(lambda k: '.H' not in k, fix20))
    fix22 = list(filter(lambda k: '.I' not in k, fix21))
    fix23 = list(filter(lambda k: '.J' not in k, fix22))
    fix24 = list(filter(lambda k: '.K' not in k, fix23))
    fix25 = list(filter(lambda k: '.L' not in k, fix24))
    fix26 = list(filter(lambda k: '.M' not in k, fix25))
    fix27 = list(filter(lambda k: '.N' not in k, fix26))
    fix28 = list(filter(lambda k: '.O' not in k, fix27))
    fix29 = list(filter(lambda k: '.P' not in k, fix28))
    fix30 = list(filter(lambda k: '.Q' not in k, fix29))
    fix31 = list(filter(lambda k: '.R' not in k, fix30))
    fix32 = list(filter(lambda k: '.S' not in k, fix31))
    fix33 = list(filter(lambda k: '.T' not in k, fix32))
    fix34 = list(filter(lambda k: '.U' not in k, fix33))
    fix35 = list(filter(lambda k: '.V' not in k, fix34))
    fix36 = list(filter(lambda k: '.W' not in k, fix35))
    fix37 = list(filter(lambda k: '.X' not in k, fix36))
    fix38 = list(filter(lambda k: '.Y' not in k, fix37))
    fix39 = list(filter(lambda k: '.Z' not in k, fix38))
    fix40 = list(filter(lambda k: '.C' not in k, fix39))
    fix41 = list(filter(lambda k: 'A$' not in k, fix40))
    fix42 = list(filter(lambda k: 'L$' not in k, fix41))
    fix43 = list(filter(lambda k: 'M$' not in k, fix42))
    fix44 = list(filter(lambda k: 'I$' not in k, fix43))
    fix45 = list(filter(lambda k: 'P$' not in k, fix44))
    fix46 = list(filter(lambda k: 'Y$' not in k, fix45))

    tickers = fix46

    selected_stock = st.selectbox("Enter ticker symbol", tickers)

    # st.line_chart(tickerDf.Close)
    # st.line_chart(tickerDf.Volume)
    @st.cache
    def load_data(selected_stock):
        data = yf.download(selected_stock, START, TODAY)
        data.reset_index(inplace=True)
        return data

    data_load_state = st.text("Loading data...Done!")
    data = load_data(selected_stock)

    st.subheader("Live Price")
    st.success(si.get_live_price(selected_stock))
    st.subheader('Raw data')
    st.write(data.tail())
    st.subheader('Interactive Graphs')

    def PRD():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='Stock_Open'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Stock_Close'))
        fig.layout.update(xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    PRD()

    start = st.date_input('Start Date', value=pd.to_datetime('2022-01-01'))
    end = st.date_input('End Date', value=pd.to_datetime('today'))
    if len(selected_stock) > 0:
        df = yf.download(selected_stock, start, end)['Adj Close']
        st.line_chart(df)
    st.subheader("Current Quote Data")
    st.write(si.get_quote_table(selected_stock))
    st.subheader("Ratios")
    st.write(si.get_stats_valuation(selected_stock))


def fundamental_evaluation():
    st.title("Manual 18 Point Checklist")

    import yfinance as yf
    from yahoo_fin import stock_info as si
    import pandas as pd
    from datetime import date
    import datetime
    today = date.today()
    import numpy as np
    import random
    st.write('The overall decision based on an interactive 18 point checklist')
    st.header("Fundamentals")
    check1 = st.checkbox("Is PE Ratio between 1 and 25?")
    check2 = st.checkbox("Is the Net Margin greater than 10%")
    check3 = st.checkbox("Are the Assets greater than the Liabilities?")
    check4 = st.checkbox("Does the company have more Free Cash Flow than the cost of Dividends?")
    checkscam = st.checkbox("Is the Debt to Equity less than 40%?")
    check5 = st.checkbox("Is the Current Ratio greater than 1?")
    check6 = st.checkbox("Have the Shareholders Diluted the shares in the last 3 years?")
    st.header("Momentum")
    check7 = st.checkbox("Is the 3 year Total Revenue positive(YOY)?")
    check8 = st.checkbox("Is the 3 year Gross Profit positive(YOY)?")
    check9 = st.checkbox("Is the 3 year Operating Income positive?")
    check10 = st.checkbox("Is the 3 year Net Income positive(YOY)?")
    check11 = st.checkbox("Is the 3 year Operating Cash Flow positive(YOY)?")
    check12 = st.checkbox("Is the 3 year Free Cash Flow positive(YOY)?")
    st.header("Growth")
    check13 = st.checkbox("Has the Share Price doubled since Inception or on the 10 Year mark?")
    check14 = st.checkbox("Is the Return on Equity greater than 10%?")
    check15 = st.checkbox("Is the Return on Asset greater than 10%?")
    check16 = st.checkbox("Is the Return on Invested Capital greater than 10%")
    check17 = st.checkbox("Does the EPS have a CAGR(Compound Annual Growth Rate) greater than 10%")
    values = []

    def valueone():
        if check1 == True:
            values.append(1)
        elif check1 == False:
            values.append(0)

    def valuetwo():
        if check2 == True:
            values.append(1)
        elif check2 == False:
            values.append(0)

    def valuethree():
        if check3 == True:
            values.append(1)
        elif check3 == False:
            values.append(0)

    def valuefour():
        if check4 == True:
            values.append(1)
        elif check4 == False:
            values.append(0)

    def valuefive():
        if check5 == True:
            values.append(1)
        elif check5 == False:
            values.append(0)

    def valuesix():
        if check6 == True:
            values.append(1)
        elif check6 == False:
            values.append(0)

    def valueseven():
        if check7 == True:
            values.append(1)
        elif check7 == False:
            values.append(0)

    def valueeight():
        if check8 == True:
            values.append(1)
        elif check8 == False:
            values.append(0)

    def valuenine():
        if check9 == True:
            values.append(1)
        elif check9 == False:
            values.append(0)

    def valueten():
        if check10 == True:
            values.append(1)
        elif check10 == False:
            values.append(0)

    def valueeleven():
        if check11 == True:
            values.append(1)
        elif check11 == False:
            values.append(0)

    def valuetwelve():
        if check12 == True:
            values.append(1)
        elif check12 == False:
            values.append(0)

    def value13():
        if check13 == True:
            values.append(1)
        elif check13 == False:
            values.append(0)

    def value14():
        if check14 == True:
            values.append(1)
        elif check14 == False:
            values.append(0)

    def value15():
        if check15 == True:
            values.append(1)
        elif check15 == False:
            values.append(0)

    def value16():
        if check16 == True:
            values.append(1)
        elif check16 == False:
            values.append(0)

    def value17():
        if check17 == True:
            values.append(1)
        elif check17 == False:
            values.append(0)

    def valuescam():
        if checkscam == True:
            values.append(1)
        elif checkscam == False:
            values.append(0)

    valueone()
    valuescam()
    valuetwelve()
    value17()
    value16()
    valueten()
    valueeleven()
    value13()
    value14()
    value15()
    valuenine()
    valueeight()
    valueseven()
    valuesix()
    valuefive()
    valuefour()
    valuethree()
    valuetwo()
    st.subheader("Your checklist score is")
    st.subheader(sum(values))
    total = sum(values)
    if total <= 6:
        st.write("Do more reasearch on this stock, not great for long term")
    elif total > 6 and total < 12:
        st.write("Solid Choice for long term make sure to consider news.")
    elif total >= 12:
        st.write("Great Company, hold for long term growth")

    # d3 = '{dt.month}/{dt.day}/{dt.year}'.format(dt = datetime.datetime.now())
    # df = si.get_stats_valuation("AMZN")
    # name = ("As of Date:" + " " + d3 + "Current")
    # peRatio = df.loc[2:2, name]
    # if int(float(peRatio)) > 1 and int(float(peRatio)) < 25:
    #   NCheck1 = st.checkbox("PE Ratio is between 1 and 25", value = True)
    # else:
    #  WCheck1 = st.checkbox("PE Ratio is not between 1 and 25", value = False)

    # Add your fundamental evaluation content here

def auto18():
    import numpy
    import streamlit as st
    import yfinance as yf
    from yahoo_fin import stock_info as si
    import pandas as pd
    from datetime import date
    import datetime
    from streamlit_option_menu import option_menu
    today = date.today()
    import numpy as np
    import random
    from fibooks import other

    st.title('Winvest Checklist')
    st.write('The overall decision based an automatic checklist for all stocks')


    stocks = si.tickers_other()
    stocks1 = si.tickers_nasdaq()
    stocks2 = si.tickers_sp500()
    # tickerDf = tickerData.history(period='1d', start = '2010-5-31', end='2020-5-31')
    stockstots = (stocks + stocks1 + stocks2)
    # STOCK FILTRATION
    gokli = list(filter(lambda k: '.W' not in k, stockstots))
    mokli = list(filter(lambda k: '.U' not in k, gokli))
    pokli = list(filter(lambda k: '$B' not in k, mokli))
    zokli = list(filter(lambda k: '$C' not in k, pokli))
    lokli = list(filter(lambda k: '$A' not in k, zokli))
    qokli = list(filter(lambda k: '$D' not in k, lokli))
    nokli = list(filter(lambda k: '$E' not in k, qokli))
    xokli = list(filter(lambda k: '$F' not in k, nokli))
    aokli = list(filter(lambda k: '.A' not in k, xokli))
    eokli = list(filter(lambda k: '.B' not in k, aokli))
    hokli = list(filter(lambda k: '$F' not in k, eokli))
    tokli = list(filter(lambda k: '$G' not in k, hokli))
    sokli = list(filter(lambda k: '$H' not in k, tokli))
    dokli = list(filter(lambda k: '$I' not in k, sokli))
    yokli = list(filter(lambda k: '$J' not in k, dokli))
    fix1 = list(filter(lambda k: '$K' not in k, yokli))
    fix2 = list(filter(lambda k: '$L' not in k, fix1))
    fix3 = list(filter(lambda k: '$M' not in k, fix2))
    fix4 = list(filter(lambda k: '$N' not in k, fix3))
    fix5 = list(filter(lambda k: '$O' not in k, fix4))
    fix6 = list(filter(lambda k: '$P' not in k, fix5))
    fix7 = list(filter(lambda k: '$Q' not in k, fix6))
    fix8 = list(filter(lambda k: '$R' not in k, fix7))
    fix9 = list(filter(lambda k: '$S' not in k, fix8))
    fix10 = list(filter(lambda k: '$T' not in k, fix9))
    fix11 = list(filter(lambda k: '$U' not in k, fix10))
    fix12 = list(filter(lambda k: '$V' not in k, fix11))
    fix13 = list(filter(lambda k: '$W' not in k, fix12))
    fix14 = list(filter(lambda k: '$X' not in k, fix13))
    fix15 = list(filter(lambda k: '$Y' not in k, fix14))
    fix16 = list(filter(lambda k: '$Z' not in k, fix15))
    fix17 = list(filter(lambda k: '.D' not in k, fix16))
    fix18 = list(filter(lambda k: '.E' not in k, fix17))
    fix19 = list(filter(lambda k: '.F' not in k, fix18))
    fix20 = list(filter(lambda k: '.G' not in k, fix19))
    fix21 = list(filter(lambda k: '.H' not in k, fix20))
    fix22 = list(filter(lambda k: '.I' not in k, fix21))
    fix23 = list(filter(lambda k: '.J' not in k, fix22))
    fix24 = list(filter(lambda k: '.K' not in k, fix23))
    fix25 = list(filter(lambda k: '.L' not in k, fix24))
    fix26 = list(filter(lambda k: '.M' not in k, fix25))
    fix27 = list(filter(lambda k: '.N' not in k, fix26))
    fix28 = list(filter(lambda k: '.O' not in k, fix27))
    fix29 = list(filter(lambda k: '.P' not in k, fix28))
    fix30 = list(filter(lambda k: '.Q' not in k, fix29))
    fix31 = list(filter(lambda k: '.R' not in k, fix30))
    fix32 = list(filter(lambda k: '.S' not in k, fix31))
    fix33 = list(filter(lambda k: '.T' not in k, fix32))
    fix34 = list(filter(lambda k: '.U' not in k, fix33))
    fix35 = list(filter(lambda k: '.V' not in k, fix34))
    fix36 = list(filter(lambda k: '.W' not in k, fix35))
    fix37 = list(filter(lambda k: '.X' not in k, fix36))
    fix38 = list(filter(lambda k: '.Y' not in k, fix37))
    fix39 = list(filter(lambda k: '.Z' not in k, fix38))
    fix40 = list(filter(lambda k: '.C' not in k, fix39))
    fix41 = list(filter(lambda k: 'A$' not in k, fix40))
    fix42 = list(filter(lambda k: 'L$' not in k, fix41))
    fix43 = list(filter(lambda k: 'M$' not in k, fix42))
    fix44 = list(filter(lambda k: 'I$' not in k, fix43))
    fix45 = list(filter(lambda k: 'P$' not in k, fix44))
    fix46 = list(filter(lambda k: 'Y$' not in k, fix45))

    selected_stock = st.selectbox("Enter Ticker Symbol", fix46)

    # COME BACK AND USE GOKLI TO FILTER OUT UNWANTED TICKERS :)

    st.subheader("Fundamentals")

    d3 = '{dt.month}/{dt.day}/{dt.year}'.format(dt=datetime.datetime.now())
    df = si.get_stats_valuation(selected_stock)
    dfc = list(df.columns)
    name = dfc[1]
    # name = df1.get_loc(0:0, 0)
    # name = column.loc[2:2, 0]
    # name = ("As of Date:" + " " + d3 + "Current")
    peRatio = df.loc[2:2, name]

    sik = str(list(peRatio))

    def OperPeRATIO(s):
        if s == '[nan]':
            return True
        else:
            return False

    left, right = st.columns(2)
    if OperPeRATIO(sik) == True:
        WCheck1 = st.checkbox("Is PE Ratio is in between 1 and 25?", value=False, disabled=True)
    else:

        if int(float(peRatio)) > 1 and int(float(peRatio)) < 25:
            with left:
                NCheck1 = st.checkbox("Is PE Ratio is between 1 and 25?", value=True, disabled=True)
            with right:
                st.write(float(peRatio))
            ##with right:


        else:
            with left:
                WCheck1 = st.checkbox("Is PE Ratio is between 1 and 25?", value=False, disabled=True)
            with right:
                st.write(float(peRatio))
            # with right:
            # st.write(float(peRatio))

    df1 = si.get_stats(selected_stock)
    netMargin = df1.loc[31:31, "Value"]
    if float(netMargin.str.strip('%')) / 100.0 > 0.1:
        with left:
            NCheck2 = st.checkbox("Is the Net Margin is greater then 10%?", value=True, disabled=True)
        with right:
            st.write(float(netMargin.str.strip('%')))
    else:
        WCheck2 = st.checkbox("Is the Net Margin is greater then 10%?", value=False, disabled=True)
        # st.write(float(netMargin.str.strip('%')))

    dfAs = other.info()
    st.write(dfAs)
    dfLia = si.get_financials(selected_stock)
    st.write(dfLia)
    # Assets = dfAs.loc[31:31, "Value"]
    # Liabilities = dfLia.loc[31:31, "Value"]
    columnlist1 = dfAs.columns
    dfALname = list(columnlist1)
    st.write(dfALname)
    ALname = dfALname[0]
    # assets and liabilites names column
    dfAs1 = dfAs.loc['totalAssets':'totalAssets', ALname]
    dfLia1 = dfLia.loc['totalLiab':'totalLiab', ALname]

    if float(dfAs1) > float(dfLia1):
        NCheck3 = st.checkbox("Is the Net Equity Positive?", value=True, disabled=True)
    else:
        WCheck3 = st.checkbox("Is the Net Equity Positive?", value=False, disabled=True)

    dfCash = si.get_stats(selected_stock)
    dfFree = dfCash.loc[50:50, 'Value']
    wog = str(dfFree)
    hog = wog.lstrip("'50 ")
    kog = hog.rstrip("Name:Value,dtype:object'")

    koggers = kog.rstrip('dtype:')

    # if 'B' in woggers:
    # hoggers = woggers.rstrip('B')
    # finalyoggers = hoggers.strip('.')
    # dogwater = int(finalyoggers)
    # st.write(dogwater)
    # else:
    # st.write("LOSER")

    dfFC = si.get_cash_flow(selected_stock)
    DIE = list(dfFC.columns)
    Times = DIE[0]
    doggers = str(Times)
    wowzers = doggers.split("'")
    yay = wowzers[0]
    KDATE = str(yay)

    # YOGGERS = int(dfFC.loc['issuanceOfStock':'issuanceOfStock', KDATE])

    # st.write(YOGGERS)

    dfDiv = si.get_dividends(selected_stock)
    # MAKE SURE UUU ACCOUNT FOR THE STOCKS WITH NO DIVDS
    dfLLL = list(dfDiv.iterrows())
    dfMula = dfDiv.tail(1)
    dfNone = (str(list(dfMula)))

    def OperDiv(dive):
        if dive == '[]':
            return True
        else:
            return False

    if OperDiv(dfNone) == True:
        WCheckwth = st.checkbox("Is Free CashFlow more than Dividend Payout?", value=False, disabled=True)
        st.write("(Company does not issue dividends)")
    else:

        dfKKK = dfLLL[-1]
        stringM = str(dfKKK)
        poggers = stringM.split("'")

        yoggers = poggers[1]

        yop = si.get_quote_data(selected_stock)
        poop = str(yop)
        pooper = poop.split(",")
        SONUM = [k for k in pooper if 'sharesOutstanding' in k]

        heheN = str(SONUM)
        Shares = heheN.split(':')

        Out = str(Shares[1])
        OutStand = Out.strip('"')

        Outstanding = OutStand.rstrip('"]')
        SHAREOUT = int(Outstanding)

        DIVIDEND = dfDiv.loc[yoggers:yoggers, 'dividend']
        hello = float(DIVIDEND) * SHAREOUT
        # if hello >=
        # df.columns = range(df.columns.size)

        sitnow = si.get_cash_flow(selected_stock)
        sitnow.columns = range(sitnow.columns.size)
        sitthen = sitnow.columns
        yozy = sitnow.loc['totalCashFromOperatingActivities':'totalCashFromOperatingActivities', 1]

        if float(yozy) >= float(hello) * float(DIVIDEND):
            NCheck4 = st.checkbox("Is Free Cash Flow is Greater than Divdends?", value=True, disabled=True)
        else:
            WCheck4 = st.checkbox("Is Free Cash Flow is Greater than Divdends?", value=False, disabled=True)

    st.subheader("Debt")

    yo = si.get_balance_sheet(selected_stock)

    debe = si.get_balance_sheet(selected_stock)
    debe.columns = range(debe.columns.size)
    equity = debe.loc['totalStockholderEquity':'totalStockholderEquity', 1]
    debt = debe.loc['longTermDebt':'longTermDebt', 1]
    if float(debt) / float(equity) <= 0.4:
        NCheckscam = st.checkbox("Is The Debt/Equity less than 40%?", value=True, disabled=True)
    else:
        WCheckscam = st.checkbox("Is The Debt/Equity less than 40%?", value=False, disabled=True)

    # Shareholders have not been diluted in the last 3 years

    CURATIO = (si.get_stats(selected_stock))

    cRatio = CURATIO.loc[47:47, "Value"]

    if float(cRatio) >= 1:
        NCheckCratio = st.checkbox("Is The Current Ratio greater than 1?", value=True, disabled=True)
    else:
        WCheckCratio = st.checkbox("Is the Current Ratio greater than 1? ", value=False, disabled=True)

    sitboi = si.get_cash_flow(selected_stock)
    sitboi.columns = range(sitboi.columns.size)
    sitok = sitboi.columns
    yozys = sitboi.loc['totalCashFromOperatingActivities':'totalCashFromOperatingActivities', 1]

    if float(yozys) / float(debt) >= 0.1:
        NCheckCRdebt = st.checkbox("Is The Free Cash Flow To Debt Ratio Greater than 10%?", value=True, disabled=True)
    else:
        WCheckCRdebt = st.checkbox("Is The Free Cash Flow To Debt Ratio Greater than 10%?", value=False, disabled=True)

    st.subheader("Momentum")

    # check7 = st.checkbox("Is the 3 year Total Revenue positive(YOY)?")
    # check8 = st.checkbox("Is the 3 year Gross Profit positive(YOY)?")
    # check9 = st.checkbox("Is the 3 year Operating Income positive?")
    # check10 = st.checkbox("Is the 3 year Net Income positive(YOY)?")
    # check11 = st.checkbox("Is the 3 year Operating Cash Flow positive(YOY)?")
    # check12 = st.checkbox("Is the 3 year Free Cash Flow positive(YOY)?")

    incomestats = si.get_income_statement(selected_stock)
    incomestats.columns = range(incomestats.columns.size)
    Revenue1 = incomestats.loc['totalRevenue':'totalRevenue', 0:0]
    Revenue2 = incomestats.loc['totalRevenue':'totalRevenue', 1:1]
    Revenue3 = incomestats.loc['totalRevenue':'totalRevenue', 2:2]

    def Mo(n):
        Revsplit = str(n)
        Tack = Revsplit.split()
        taco = float(int(Tack[3]))

        return taco

    Rv1 = (Mo(Revenue1))
    Rv2 = (Mo(Revenue2))
    Rv3 = (Mo(Revenue3))

    if Rv1 >= Rv2 and Rv2 >= Rv3:
        NCheckCRevenue = st.checkbox("Has the Revenue Been Increasing for the last 3 years?", value=True, disabled=True)
    else:
        WCheckCRevenue = st.checkbox("Has the Revenue Been Increasing for the last 3 years?", value=False,
                                     disabled=True)

    GrossP1 = incomestats.loc['grossProfit':'grossProfit', 0:0]
    GrossP2 = incomestats.loc['grossProfit':'grossProfit', 1:1]
    GrossP3 = incomestats.loc['grossProfit':'grossProfit', 2:2]

    GPro1 = (Mo(GrossP1))
    GPro2 = (Mo(GrossP2))
    GPro3 = (Mo(GrossP3))

    if GPro1 >= GPro2 and GPro2 >= GPro3:
        NCheckCRevenue = st.checkbox("Has the GrossProfit Been Increasing for the last 3 years?", value=True,
                                     disabled=True)
    else:
        WCheckCRevenue = st.checkbox("Has the GrossProfit Been Increasing for the last 3 years?", value=False,
                                     disabled=True)

    OpinP1 = incomestats.loc['operatingIncome':'operatingIncome', 0:0]
    OpinP2 = incomestats.loc['operatingIncome':'operatingIncome', 1:1]
    OpinP3 = incomestats.loc['operatingIncome':'operatingIncome', 2:2]

    Oper1 = (Mo(OpinP1))
    Oper2 = (Mo(OpinP2))
    Oper3 = (Mo(OpinP3))

    if Oper1 >= Oper2 and Oper2 >= Oper3:
        NCheckCRevenue = st.checkbox("Has the Operating Income Been Increasing for the last 3 years?", value=True,
                                     disabled=True)
    else:
        WCheckCRevenue = st.checkbox("Has the Operating Income Been Increasing for the last 3 years?", value=False,
                                     disabled=True)

    NetP1 = incomestats.loc['netIncome':'netIncome', 0:0]
    NetP2 = incomestats.loc['netIncome':'netIncome', 1:1]
    NetP3 = incomestats.loc['netIncome':'netIncome', 2:2]

    neti1 = (Mo(NetP1))
    neti2 = (Mo(NetP2))
    neti3 = (Mo(NetP3))

    if neti1 >= neti2 and neti2 >= neti3:
        NCheckCRevenue = st.checkbox("Has the Net Income Been Increasing for the last 3 years?", value=True,
                                     disabled=True)
    else:
        WCheckCRevenue = st.checkbox("Has the Net Income Been Increasing for the last 3 years?", value=False,
                                     disabled=True)

    cashstats = si.get_cash_flow(selected_stock)
    cashstats.columns = range(cashstats.columns.size)

    CashOper1 = cashstats.loc['totalCashFromOperatingActivities':'totalCashFromOperatingActivities', 0:0]
    CashOper2 = cashstats.loc['totalCashFromOperatingActivities':'totalCashFromOperatingActivities', 1:1]
    CashOper3 = cashstats.loc['totalCashFromOperatingActivities':'totalCashFromOperatingActivities', 2:2]

    def OperationFlow(oper):
        compy = str(oper)
        lappy = compy.split()
        noty = float(lappy[3])

        return noty

    coper1 = OperationFlow(CashOper1)
    coper2 = OperationFlow(CashOper2)
    coper3 = OperationFlow(CashOper3)

    if coper1 >= coper2 and coper2 >= coper3:
        NCheckCRevenue = st.checkbox("Has the Operating Cash Flow Been Increasing for the last 3 years?", value=True,
                                     disabled=True)
    else:
        WCheckCRevenue = st.checkbox("Has the Operating Cash Flow Been Increasing for the last 3 years?", value=False,
                                     disabled=True)

    Fcf1 = cashstats.loc['capitalExpenditures':'capitalExpenditures', 0:0]
    Fcf2 = cashstats.loc['capitalExpenditures':'capitalExpenditures', 1:1]
    Fcf3 = cashstats.loc['capitalExpenditures':'capitalExpenditures', 2:2]

    totalfree1 = OperationFlow(Fcf1)
    totalfree2 = OperationFlow(Fcf2)
    totalfree3 = OperationFlow(Fcf3)

    if (coper1 + totalfree1) >= (coper2 + totalfree2) and (coper2 + totalfree2) >= (coper3 + totalfree3):
        NCheckCRevenue = st.checkbox("Has the Free Cash Flow Been Increasing for the last 3 years?", value=True,
                                     disabled=True)
    else:
        WCheckCRevenue = st.checkbox("Has the Free Cash Flow Been Increasing for the last 3 years?", value=False,
                                     disabled=True)

    st.subheader("Growth")

    if float(neti1) / float(equity) >= 0.1:
        NCheckCRrass = st.checkbox("Is The Return on Equity Greater than 10%?", value=True, disabled=True)
    else:
        WCheckCRrass = st.checkbox("Is The Return on Equity Greater than 10%?", value=False, disabled=True)

    if float(neti1) / float(dfAs1) >= 0.1:
        NCheckCRrass = st.checkbox("Is The Return on Asset Greater than 10%?", value=True, disabled=True)
    else:
        WCheckCRrass = st.checkbox("Is The Return on Asset Greater than 10%?", value=False, disabled=True)

    Earnings = (si.get_earnings_history(selected_stock))
    ER1 = (Earnings[4])
    WOW1 = dict(list(ER1.items())[5:6])

    ER2 = (Earnings[8])
    WOW2 = dict(list(ER2.items())[5:6])

    ER3 = (Earnings[12])
    WOW3 = dict(list(ER3.items())[5:6])

    EPS1 = (WOW1["epsactual"])
    EPS2 = (WOW2["epsactual"])
    EPS3 = (WOW3["epsactual"])

    if (float(EPS3) * 0.1) + float(EPS3) <= float(EPS2) and (float(EPS2) * 0.1) + float(EPS2) <= float(EPS1):
        NCheckCREPSs = st.checkbox("Is the YoY EPS Growth greater than 10%?", value=True, disabled=True)
    else:
        WCheckCREPSs = st.checkbox("Is the YoY EPS Growth greater than 10%?", value=False, disabled=True)

    # Add your technical evaluation content here

def technical_evaluation():
    import streamlit as st
    import yfinance as yf
    import pandas as pd
    from yahoo_fin import stock_info as si

    st.title("Technical Evaluation")

    stocks = si.tickers_other()
    stocks1 = si.tickers_nasdaq()
    stocks2 = si.tickers_sp500()
    # tickerDf = tickerData.history(period='1d', start = '2010-5-31', end='2020-5-31')
    stockstots = (stocks + stocks1 + stocks2)
    # STOCK FILTRATION
    gokli = list(filter(lambda k: '.W' not in k, stockstots))
    mokli = list(filter(lambda k: '.U' not in k, gokli))
    pokli = list(filter(lambda k: '$B' not in k, mokli))
    zokli = list(filter(lambda k: '$C' not in k, pokli))
    lokli = list(filter(lambda k: '$A' not in k, zokli))
    qokli = list(filter(lambda k: '$D' not in k, lokli))
    nokli = list(filter(lambda k: '$E' not in k, qokli))
    xokli = list(filter(lambda k: '$F' not in k, nokli))
    aokli = list(filter(lambda k: '.A' not in k, xokli))
    eokli = list(filter(lambda k: '.B' not in k, aokli))
    hokli = list(filter(lambda k: '$F' not in k, eokli))
    tokli = list(filter(lambda k: '$G' not in k, hokli))
    sokli = list(filter(lambda k: '$H' not in k, tokli))
    dokli = list(filter(lambda k: '$I' not in k, sokli))
    yokli = list(filter(lambda k: '$J' not in k, dokli))
    fix1 = list(filter(lambda k: '$K' not in k, yokli))
    fix2 = list(filter(lambda k: '$L' not in k, fix1))
    fix3 = list(filter(lambda k: '$M' not in k, fix2))
    fix4 = list(filter(lambda k: '$N' not in k, fix3))
    fix5 = list(filter(lambda k: '$O' not in k, fix4))
    fix6 = list(filter(lambda k: '$P' not in k, fix5))
    fix7 = list(filter(lambda k: '$Q' not in k, fix6))
    fix8 = list(filter(lambda k: '$R' not in k, fix7))
    fix9 = list(filter(lambda k: '$S' not in k, fix8))
    fix10 = list(filter(lambda k: '$T' not in k, fix9))
    fix11 = list(filter(lambda k: '$U' not in k, fix10))
    fix12 = list(filter(lambda k: '$V' not in k, fix11))
    fix13 = list(filter(lambda k: '$W' not in k, fix12))
    fix14 = list(filter(lambda k: '$X' not in k, fix13))
    fix15 = list(filter(lambda k: '$Y' not in k, fix14))
    fix16 = list(filter(lambda k: '$Z' not in k, fix15))
    fix17 = list(filter(lambda k: '.D' not in k, fix16))
    fix18 = list(filter(lambda k: '.E' not in k, fix17))
    fix19 = list(filter(lambda k: '.F' not in k, fix18))
    fix20 = list(filter(lambda k: '.G' not in k, fix19))
    fix21 = list(filter(lambda k: '.H' not in k, fix20))
    fix22 = list(filter(lambda k: '.I' not in k, fix21))
    fix23 = list(filter(lambda k: '.J' not in k, fix22))
    fix24 = list(filter(lambda k: '.K' not in k, fix23))
    fix25 = list(filter(lambda k: '.L' not in k, fix24))
    fix26 = list(filter(lambda k: '.M' not in k, fix25))
    fix27 = list(filter(lambda k: '.N' not in k, fix26))
    fix28 = list(filter(lambda k: '.O' not in k, fix27))
    fix29 = list(filter(lambda k: '.P' not in k, fix28))
    fix30 = list(filter(lambda k: '.Q' not in k, fix29))
    fix31 = list(filter(lambda k: '.R' not in k, fix30))
    fix32 = list(filter(lambda k: '.S' not in k, fix31))
    fix33 = list(filter(lambda k: '.T' not in k, fix32))
    fix34 = list(filter(lambda k: '.U' not in k, fix33))
    fix35 = list(filter(lambda k: '.V' not in k, fix34))
    fix36 = list(filter(lambda k: '.W' not in k, fix35))
    fix37 = list(filter(lambda k: '.X' not in k, fix36))
    fix38 = list(filter(lambda k: '.Y' not in k, fix37))
    fix39 = list(filter(lambda k: '.Z' not in k, fix38))
    fix40 = list(filter(lambda k: '.C' not in k, fix39))
    fix41 = list(filter(lambda k: 'A$' not in k, fix40))
    fix42 = list(filter(lambda k: 'L$' not in k, fix41))
    fix43 = list(filter(lambda k: 'M$' not in k, fix42))
    fix44 = list(filter(lambda k: 'I$' not in k, fix43))
    fix45 = list(filter(lambda k: 'P$' not in k, fix44))
    fix46 = list(filter(lambda k: 'Y$' not in k, fix45))

    tickers = fix46

    dropdown = st.multiselect('Pick your assets', tickers)

    start = st.date_input('Start Date', value=pd.to_datetime('2022-01-01'))
    end = st.date_input('End Date', value=pd.to_datetime('today'))

    def relativeret(df):
        rel = df.pct_change()
        cumret = (1 + rel).cumprod() - 1
        cumret = cumret.fillna(0)
        return cumret

    if len(dropdown) > 0:
        # df = yf.download(dropdown,start,end)['Adj Close']

        df = relativeret(yf.download(dropdown, start, end)['Adj Close'])
        st.header('Relative Returns of {}'.format(dropdown))
        st.line_chart(df)

def news_data():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import yfinance as yf
    import plotly.express as px
    from yahoo_fin import stock_info as si
    from datetime import date
    from plotly import graph_objs as go
    import alpha_vantage
    st.title('News Data')
    st.write('More information to make a calculated desicion!')
    START = "2010-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    tickerSymbol = 'GOOGL'

    stocks = si.tickers_other()
    stocks1 = si.tickers_nasdaq()
    stocks2 = si.tickers_sp500()
    tickerData = yf.Ticker(tickerSymbol)
    # tickerDf = tickerData.history(period='1d', start = '2010-5-31', end='2020-5-31')
    stocks = si.tickers_other()
    stocks1 = si.tickers_nasdaq()
    stocks2 = si.tickers_sp500()
    # tickerDf = tickerData.history(period='1d', start = '2010-5-31', end='2020-5-31')
    stockstots = (stocks + stocks1 + stocks2)
    # STOCK FILTRATION
    gokli = list(filter(lambda k: '.W' not in k, stockstots))
    mokli = list(filter(lambda k: '.U' not in k, gokli))
    pokli = list(filter(lambda k: '$B' not in k, mokli))
    zokli = list(filter(lambda k: '$C' not in k, pokli))
    lokli = list(filter(lambda k: '$A' not in k, zokli))
    qokli = list(filter(lambda k: '$D' not in k, lokli))
    nokli = list(filter(lambda k: '$E' not in k, qokli))
    xokli = list(filter(lambda k: '$F' not in k, nokli))
    aokli = list(filter(lambda k: '.A' not in k, xokli))
    eokli = list(filter(lambda k: '.B' not in k, aokli))
    hokli = list(filter(lambda k: '$F' not in k, eokli))
    tokli = list(filter(lambda k: '$G' not in k, hokli))
    sokli = list(filter(lambda k: '$H' not in k, tokli))
    dokli = list(filter(lambda k: '$I' not in k, sokli))
    yokli = list(filter(lambda k: '$J' not in k, dokli))
    fix1 = list(filter(lambda k: '$K' not in k, yokli))
    fix2 = list(filter(lambda k: '$L' not in k, fix1))
    fix3 = list(filter(lambda k: '$M' not in k, fix2))
    fix4 = list(filter(lambda k: '$N' not in k, fix3))
    fix5 = list(filter(lambda k: '$O' not in k, fix4))
    fix6 = list(filter(lambda k: '$P' not in k, fix5))
    fix7 = list(filter(lambda k: '$Q' not in k, fix6))
    fix8 = list(filter(lambda k: '$R' not in k, fix7))
    fix9 = list(filter(lambda k: '$S' not in k, fix8))
    fix10 = list(filter(lambda k: '$T' not in k, fix9))
    fix11 = list(filter(lambda k: '$U' not in k, fix10))
    fix12 = list(filter(lambda k: '$V' not in k, fix11))
    fix13 = list(filter(lambda k: '$W' not in k, fix12))
    fix14 = list(filter(lambda k: '$X' not in k, fix13))
    fix15 = list(filter(lambda k: '$Y' not in k, fix14))
    fix16 = list(filter(lambda k: '$Z' not in k, fix15))
    fix17 = list(filter(lambda k: '.D' not in k, fix16))
    fix18 = list(filter(lambda k: '.E' not in k, fix17))
    fix19 = list(filter(lambda k: '.F' not in k, fix18))
    fix20 = list(filter(lambda k: '.G' not in k, fix19))
    fix21 = list(filter(lambda k: '.H' not in k, fix20))
    fix22 = list(filter(lambda k: '.I' not in k, fix21))
    fix23 = list(filter(lambda k: '.J' not in k, fix22))
    fix24 = list(filter(lambda k: '.K' not in k, fix23))
    fix25 = list(filter(lambda k: '.L' not in k, fix24))
    fix26 = list(filter(lambda k: '.M' not in k, fix25))
    fix27 = list(filter(lambda k: '.N' not in k, fix26))
    fix28 = list(filter(lambda k: '.O' not in k, fix27))
    fix29 = list(filter(lambda k: '.P' not in k, fix28))
    fix30 = list(filter(lambda k: '.Q' not in k, fix29))
    fix31 = list(filter(lambda k: '.R' not in k, fix30))
    fix32 = list(filter(lambda k: '.S' not in k, fix31))
    fix33 = list(filter(lambda k: '.T' not in k, fix32))
    fix34 = list(filter(lambda k: '.U' not in k, fix33))
    fix35 = list(filter(lambda k: '.V' not in k, fix34))
    fix36 = list(filter(lambda k: '.W' not in k, fix35))
    fix37 = list(filter(lambda k: '.X' not in k, fix36))
    fix38 = list(filter(lambda k: '.Y' not in k, fix37))
    fix39 = list(filter(lambda k: '.Z' not in k, fix38))
    fix40 = list(filter(lambda k: '.C' not in  k, fix39))
    fix41 = list(filter(lambda k: 'A$' not in k, fix40))
    fix42 = list(filter(lambda k: 'L$' not in k, fix41))
    fix43 = list(filter(lambda k: 'M$' not in k, fix42))
    fix44 = list(filter(lambda k: 'I$' not in k, fix43))
    fix45 = list(filter(lambda k: 'P$' not in k, fix44))
    fix46 = list(filter(lambda k: 'Y$' not in k, fix45))

    tickers = fix46

    selected_stock = st.selectbox("Enter ticker symbol", tickers)

    pricing_data, fundamental_data, news, ai_decision = st.tabs(
        ["Pricing Data", "Fundamental Data", "Top 10 News", "AI Insight"])
    data = yf.download(selected_stock, START, TODAY)
    with pricing_data:
        st.header('Price Movements')
        data2 = data
        data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
        data2.dropna(inplace=True)
        st.write(data2)
        annual_return = data2['% Change'].mean() * 252 * 100
        st.write('Annual Return is', annual_return, '%')
        stdev = np.std(data2['% Change']) * np.sqrt(252)
        st.write('Standard Deviation is ', stdev * 100, '%')
        st.write('Risk Adj. Return is ', annual_return / (stdev * 100))

    from alpha_vantage.fundamentaldata import FundamentalData
    with fundamental_data:
        st.header('Fundamental Data')
        key = 'Q8HJLXKZZ3YRHT6P'
        fd = FundamentalData(key, output_format='pandas')
        st.subheader('Balance Sheet')
        balance_sheet = fd.get_balance_sheet_annual(selected_stock)[0]
        bs = balance_sheet.T[2:]
        bs.columns = list(balance_sheet.T.iloc[0])
        st.write(bs)
        st.subheader('Income Statement')
        income_statement = fd.get_income_statement_annual(selected_stock)[0]
        is1 = income_statement.T[2:]
        is1.columns = list(income_statement.T.iloc[0])
        st.write(is1)
        st.subheader('Cash Flow Statement')
        cash_flow = fd.get_cash_flow_annual(selected_stock)[0]
        cf = cash_flow.T[2:]
        cf.columns = list(cash_flow.T.iloc[0])
        st.write(cf)

    from stocknews import StockNews
    with news:
        st.header(f'Latest News from {selected_stock}')
        sn = StockNews(selected_stock, save_news=False)
        df_news = sn.read_rss()
        for i in range(10):
            st.subheader(f'News {i + 1}')
            st.write(df_news['published'][i])
            st.write(df_news['title'][i])
            st.write(df_news['summary'][i])
            title_sentiment = df_news['sentiment_title'][i]
            st.write(f'Title Sentiment {title_sentiment}')
            news_sentiment = df_news['sentiment_summary'][i]
            st.write(f'News Sentiment {news_sentiment}')

    from pyChatGPT import ChatGPT

    session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..KJFBlF9woRCEn620.BFTOta1Y1oWELsjFxpAOWMJKkYc1wvLwxNbQsGZN-yz4vVHSFh0nt768ZKlEOyC11UWq5gcoXpr00HfvN8RrJCRUDD4u1yz4e2OkgbqFcAL0vAssvUcbebt3-ln4bJcEotKejib5TwajSI-H8tq_LPe828zMtDrR3xtFBY9K83YbyVjXsSeHVTeE_tls0MPeP4heQjbvrLwL2DIETc3rK0-9ha0afeyU8U6mgFUQWS6OkyVxyz3mn3b7cz2ocCAhbueAvBWj71eT9j6W7psTmIKhovdtJRGOyi8mDz9If6mLyBiHZ0h38ag1gI23ENwfCjm5zFD0MMJRxFthhYZJq9gUcovQLrjKvjhmJuMG13XPoFyD-ziYgpJm0WsDQPEv47sa5Tx34YMF4mZMzQjfZXvMztQegFb2rDftnlNmDQMxj9KpGi-Bbd0upT1NJFmTc58FhBQyTIUmxzFukFg9FmoahrlCE2V-wbLGt0GHhzNReR6kzsGqjVjgY5iZYpqfa-dhPkx4_s61kz2GK6_qDnEgBwDm_hlVqKl5XExxPlZeydz8Mg2LmNQ3WBxYF5-xaFiRBHvN1NFLp9ROMWQD8CwT5pWWxcK6KAQeozNJfBsbaL81JlvrOMpxvER7nGT9jg9h108YsueohfqEpdDZs5WEuP8-YBe1VIZVhuYssJe1n8sJF501LkFsDilZlWuGrVF9D5mWSGR-hUi_JWAGrBX_g9WkQ47tefC7ux_nvuqTVq8slfppj7rj0ml-bw_ub_FlCAICBKPfaWpQUT9kci0y0itBhC0Zcekk_Rw2GTpE78trfdlv8t0xjLOUZBVzITaYgKBaZtdAsh7kfyG7xDYjsxFPSxpQqy7DfdcXRSqqCFKvpLvdZDzT8WqlWr1keFoeXoe6Em2F5FS88a6tdA8epwsImtfbXQsxdclHtkCBdW94kzCIQmjkhi4X3c32kPo24cmvJgF44Bpyy7rZQRQGdyW5sXcSzWMQPiff8U7r9q-qFDQZT2b3_MZkJ8fCYThaZa6RpgDGd4lg6oax7OhauupMtqdd_E_pHfzse_zLq2GETFGkr72QfJkgXtOaLB7ZU2Nx892YR08wNjEMG0ZSwvePeAWRMGCZSR6lsoOMeklm-_UlycPfRfHciPZUoMOZwECFB4_xBo_pbUN5ob_WvsvK0rbg4kXAC4WUNE9VDP_AUz3qN0XFOf_M9JZYx-jFgk_t1tQxis9qJljGgCTm9JBtkf5vPTr_rnGzdj2pe0Pd3-STDmW8wiANBxiLf7C0Lscf9b8gsF4nswuQBfkj46o1kQCXhOlPSwe2Vvk5PjKfD9vE1ih3yizaefl7fg1dds05k8xOD_Q0Zkt6giUVpJ2LG5iSerfRhbChYfV9nn5E8YtBY7BrD3QGQDLZ6b3ftvPDowoMG_aMnLicF_HyepeMxFzujziZWVndwBDM5lvmhxtk_ti2lxlgVTdVYfsBVtsJSKXUku-tyfqxYdC8rhUwNA-i4fJTMmaePW6sBIqrzn0F20MLmKQvPmsIJi05Z7h_BGc3GUsB93BZMYdUnD0DAr5Dh9Ric7oI9IiHmDGzPY_Q0UGWWlO2ZObzqwueAcjoqsZnLOH1RHkpFTpmR33Kv5NWZuFU8w5w9q6jqx0Dmq-xLUzuen5pK2D2D6WeNz15Sh4DFPsvk2jA6Ca68lySX1bUOcL_6_1NEnRg5lkAZHP6ExSsQGO0O-2G56E04Tfn6lGrGEVK6qcMOZwsz77TdQa_odgRMetAaNVnYkeGaFycBkwCWMkuZ77pTaFFKQYXNvveX8tFU8lxumgp_62fyKjNp3VdnnT81BRtSycNokDS7Jjmu2ABwmd1bKDcxnveWiZ2BNz6p-aXoKvc0dYepoSrbZQ79Emxv72RgAsgswfWMxdL0Yx7CkiCaQrlbMXdZ1U-V9hzlTN6i4bq0dSgZit09f3zOyuF-YgbQXh0xpBOO7spTyvK9enBpSuGR5iKf8l4jUYDRTOAyhtbNe16i1suV7IYBSHEtrvWRitLM885J7GcLQkG4bOe1UqXwgpGx3njD7RruJv2tWkpsMNhj6mUo25ge-qfeO2xW1v-b8_ByjLFWMdFI_OJncctjLwUXjTBdDRi0iYuX2NVTkgmI6H10A0g-ZKvobVUnv2kyL5-z1lfTHHkCX0Bn8diOkUIAXR3xmY_SUdN78o8MNJ6_D9Drh4h6hMSwd4AKxjdd9jrldNKdAKeDF-4w1d4_CSyVwr4o6kIFypxwC8nlSu1CYopn63dfuq17zP6k9Xg3T1ue5zgxm9Og8dZFsWLrSyjdheeu2pg4nSdg6Pyao8ewRXyL0wtua4xSp08aP0EepXaPpfI376O6YNkuuqL7IyXP6fseOW2EcduT_si2MJF1ZqJfDro3Y9PMC_VCYOpQmrZP4nwQcdnsX_6QZJaJYmXa-LArUYU1JCc3AZq4Oxh9GU4qYHiCvj2zFfCbgxHUC9tCUaxi9pCTWyFzGNhzgzjfCDX_TzZ79hNoKvblUbcThrMKJjpKo4Anvgy4A.e3-FsWlyz5RxjFUHIP0C5A"
    api2 = ChatGPT(session_token, conversation_id='bf46c848-725b-45d3-aa82-f97a16239a4d')
    buy = api2.send_message(f'3 Reasons to buy {selected_stock} stock')
    sell = api2.send_message(f'3 Reasons to sell {selected_stock} stock')
    swot = api2.send_message(f'SWOT Analysis of {selected_stock} stock')
    with ai_decision:
        st.header('AI Insight')
        buy_reason, sell_reason, swot_analysis = st.tabs(['3 Reasons to buy', '3 Reasons to sell', 'SWOT Analysis'])
        with buy_reason:
            st.subheader(f'AI Insight on why to sell {selected_stock} Stock')
            st.write(buy['message'])

        with buy_reason:
            st.subheader(f'AI Insight on why to buy {selected_stock} Stock')
            st.write(sell['message'])

        with buy_reason:
            st.subheader(f'AI SWOT Analysis of {selected_stock} Stock')
            st.write(swot['message'])
def authenticate(username, password):
    # Here, you can replace this with your own logic for user authentication
    users = get_users()
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False

def get_users():
    # Here, you can replace this with your own logic for retrieving the list of users
    # For demonstration purposes, we use a hardcoded list of users
    return [
        {"username": "krish", "password": "password"},
        {"username": "karan", "password1": "test123"},
        {"username": "sudha", "password2": "abc123"},
    ]

if __name__ == "__main__":
    logo_image_url = "https://lh3.googleusercontent.com/pw/ABLVV86t7-gXEaq1Lkljb5kdl1sXKmPaEfPMTiqIroLYmw6XkkhrAgwvJ-5MqQyN33bRqvjJp6WgJds_JUkrfARN5Fc9jjyAvTBL78zbpoLy4eEvF0ypCAE9Fku9hez9FIfnk2l3EpB02voChM9CF0KTellJu5fc-S-pu2qbOMB77yiubKnm1pp5XhqNunnQ0GVgIwS1HUHZA40XhOMy7DLu0scpPMRkuznhNR3jofzu3KN1AfBqk-YyI7Fc5es_diUXyddQ0DMFz3mN0c6J7j_4VW87y4XfgNzoz7CdauzfTpd71-w-zMrwncTw546lYFbrOwu48R7p2pC_oHssXOcMTSn4xi7Xr_JKnei6qa60If0pPQpD7Pp9GFc2pb_K2Xa9dL4hc_ZU4j5weavJeq8BSWfaQtJC1TO7qVxceHcCDd9IfXuHI681hUC-skvCzWRr0_3vvCcAvczNgpnT_iBGFd_9OmX0zE2Up_vwtLJOaWXXvVVLixi6egQiJ1titF54PV_3UZy4wJlnyjubnLzQ8GQJOG6DH_i3V2ehi2iydTKAWgWXUpHbqVyk-YvDe9PFSfl0iSNvnswfVzsXJGSSDDGlryw6CqaPEZRnOZTEIT9ZZ7j6NXAQilZPnskLBAC_0a-iHAVGjzSEuER2iwbSweUWARgU5uT2p6KWzepaaaugbwEP-DGpjHX-xipcbh5IBU-nFAawp25g17lBjE9z6uvsI7gubZc-Jy2GQY0NaVsMp4s1dD52eF-NDrQi3xF-qajClOPfjntFbahkx9NeGFyyZqx4Ip73xgLl-ZFaAOnkxlIG3nFs0ysrZZOqscZ-u72FwAq2GVxUS8E6guUAAKC3Oftz1y63iX9pkWcOYezyvPZixLiQiVJrNlI7rPDrPf4ibGE=w200-h200-s-no-gm?authuser=0"
    # Add the URL you want to link to when the logo is clicked
    logo_link_url = "https://example.com"

    # Generate HTML markup for the logo image with hyperlink
    logo_html = f'<a href="{logo_link_url}" target="_blank"><img src="{logo_image_url}" width="200" alt="Logo"></a>'
    st.sidebar.markdown(logo_html, unsafe_allow_html=True)
    st.sidebar.title("Navigation")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        login()
    else:
        # Add the URL of your online logo image here

        page = st.sidebar.radio("Go to", ("Main Dashboard", "Manual 18 Point Checklist", "Automatic 18 Point Checklist", "Technical Evaluation", "News Data"))

        if page == "Main Dashboard":
            dashboard()
        elif page == "Manual 18 Point Checklist":
            fundamental_evaluation()
        elif page == "Automatic 18 Point Checklist":
            auto18()
        elif page == "Technical Evaluation":
            technical_evaluation()
        elif page == "News Data":
            news_data()

