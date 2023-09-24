import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler

def font_string_to_PCA(input_column):
    ## style local name 전처리
    font_list = []

    for font in input_column:
        text = []
        try:
            font = eval(font)
        except:
            pass

        try:
            text = ' '.join(re.sub(r'[-_,"\[\]\s]', '', word) for word in font)
            font_list.append(text)
        except:
            font_list.append(text)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(font_list)

    # Standardize
    scaler = StandardScaler()
    X = scaler.fit_transform(X.toarray())

    #  PCA
    pca = PCA(n_components=1)
    data = pca.fit_transform(X)

    return pd.Series(map(lambda x: x[0], data))

def string_list_to_tsne(input_column) :
        ## style local name 전처리 
    string_list = []

    for font in input_column: 
        text = []
        try : 
            font = eval(font)
        except :
            pass

        try : 
            text = ' '.join(re.sub(r'[-_,"\[\]\s]', '', word) for word in font)
            string_list.append(text)
        except : 
            string_list.append(text)

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(string_list)
    sequences = tokenizer.texts_to_sequences(string_list)
    max_len = 0
    for i in range(len(sequences)) :
        if max_len < len(sequences[i]) : 
            max_len = len(sequences[i])

    X = pad_sequences(sequences, maxlen=max_len)
    np.set_printoptions(threshold=np.inf, linewidth=np.inf)

    data = pd.DataFrame(X) .iloc[:,:].values

    # 3D
    tsne = TSNE(n_components=1)
    data = tsne.fit_transform(data)
    return pd.Series(map(lambda x: x[0], data))


def datapreprocessing (output_dataframe, output_csvfile=None) : 
    # PCA 적용 
    column_list = ['paragraph_name', 'character_name', 'table_name', 'numbering_name', 'fontList']
    try : 
        for col in column_list :
            output_dataframe[col] = font_string_to_PCA(output_dataframe[col]) * 10000
    except:
        print("this code is not PCA") 
        pass
    # 20230223 자동으로 타입 확인해서 전처리하기 
    for column_name in output_dataframe.columns[output_dataframe.dtypes == "object"] :
        if column_name == "file_name" : 
            pass
        elif all(num.isdigit() for num in output_dataframe[column_name].dropna().unique()) :  # 전부 다  int 라는 거임 
            # print("int ", column_name, output_dataframe[column_name].dropna().unique()[0])
            output_dataframe[column_name] = output_dataframe[column_name].astype(float)
        else : # 다 string, char 형이라는 거임
            output_dataframe[column_name] = output_dataframe[column_name].astype('category').cat.codes 
            # print("string ", column_name, output_dataframe[column_name].dropna().unique()[0])

    # 결측치 제거하기 
    for col in output_dataframe.columns : 
        output_dataframe[col] = output_dataframe[col].fillna(-2)
    
    # 데이터 저장하기 
    if output_csvfile != None :
        output_dataframe.to_csv(output_csvfile,index=False, encoding="utf-8-sig")
    return output_dataframe

# output_dataframe = pd.read_csv("[20230329] testpre.csv", encoding='utf-8')
# datapreprocessing (output_dataframe, "[20230329] PCA 처리 안한 중간 전처리TEST.csv")