#%% 

# reference : https://ai-creator.tistory.com/307#contents_3_1


#%%
# 1. make stock_code function

import pandas as pd

def get_stock_code():

    # 1) download stockcode

    stock_code = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header = 0)[0] # 데이터프레임으로 불러오려면 [0]이 필요함

    #stock_code

    # 2) delete unnecessary columns 

    stock_code = stock_code[['회사명', '종목코드']]
    stock_code

    # 3) rename columns (kr -> en)
    stock_code = stock_code.rename(columns = {'회사명': 'company', '종목코드': 'code'})

    # 4) set 6 digits
    stock_code.code = stock_code.code.map('{:06d}'.format)
    #stock_code.code 

    # stock_code.code를 입력하면 code 칼럼의 값이 뽑힘. 여기에 map을 넣어서 6자리로 만들어줌 

    return stock_code

# %%
# 2. load daily price
    
df = pd.DataFrame() # 데이터프레임 생성

for page in range(1, 40):
    # daily price URL
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code = stock_code.code)
    url = '{url}&page={page}'.format(url = url, page = page)
    #print(url) 
    current_df = pd.read_html(url, header = 0)[0] # pip install html5lib, HTML문서를 트리구조로 분석해주는 라이브러리
    print(current_df)     
    

# %%
