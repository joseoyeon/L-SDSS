import zipfile
import xml.etree.ElementTree as ET

# Define the XML namespace used in the OpenXML package relationships
ns = {"r": "http://schemas.openxmlformats.org/package/2006/relationships"}

def feature_extraction(file_name) : 
    # print(file_name)
    doc_zip = zipfile.ZipFile(file_name)
    doc_xml = doc_zip.read('word/document.xml')
    doc_xml = ET.fromstring(doc_xml)

    docx_dic = {}
    docx_dic['file_name'] = file_name

    #print(" DOCUMENT ")
    for body in doc_xml:
        sectPrPre_count = 0
        for child in body :
            ##  p 에 종속된 내용이고, ind 빼기로 했음 
            # if child.tag.split('}')[1] == 'p' : 
            #     for pPr in child : 
            #         if pPr.tag.split('}')[1] == "pPr" : 
            #             for ind in pPr :  
            #                 if ind.tag.split('}')[1] == "ind" : 
            #                     docx_dic["ind"] = docx_dic["ind"] + 1

            ##  p 에 종속된 내용 중 secPr(구역에 적용된) 마다 적용되는 글자 크기 등등의 것들  
            # 섹션마다 적용 
            
            if child.tag.split('}')[1] == 'p' and sectPrPre_count < 1: 
                for pPr in child : 
                    if pPr.tag.split('}')[1] == "pPr" : 
                        for sectPrPre in pPr:
                            if sectPrPre.tag.split('}')[1] == "sectPr":
                                sectPrPre_count = sectPrPre_count + 1
                                for pgSz_Mar in sectPrPre : 
                                    if pgSz_Mar.tag.split('}')[1] == "footerReference" or pgSz_Mar.tag.split('}')[1] == "headerReference":
                                        # Open the relationships XML file and parse the contents
                                        root = ET.fromstring(doc_zip.read('word/_rels/document.xml.rels'))
                                        
                                        for key, value in pgSz_Mar.attrib.items() :
                                            if "type" in key : 
                                                docx_dic["sectPr" + "_" + pgSz_Mar.tag.split('}')[1] + "_"  + key.split('}')[1]] = value
                                                type_name = pgSz_Mar.tag.split('}')[1] + "_" + value
                                            if "id" in key  :          
                                                for rel in root.findall("r:Relationship", ns):
                                                    rid = rel.attrib.get("Id")
                                                    target = rel.attrib.get("Target")
                                                    if (rid == value) : 
                                                        header_footer_xml = ET.fromstring(doc_zip.read('word/'+target))
                                                        for body in header_footer_xml:
                                                            if body.tag.split('}')[1] == 'p': 
                                                                for pPr in body : 
                                                                    if pPr.tag.split('}')[1] == "pPr" : 
                                                                        for sectPrPre in pPr:
                                                                            for key, value in sectPrPre.attrib.items():
                                                                                docx_dic["sectPrpPr" + str(sectPrPre_count) + "_" + type_name  + "_" + sectPrPre.tag.split('}')[1] + "_" + key.split('}')[1]] = value
                                                                                # print("sectPrPre" + str(sectPrPre_count) + "_" + type_name  + "_" + sectPrPre.tag.split('}')[1] + "_" + key.split('}')[1], ' : ', value)
                                                            
                                    else :                                  
                                        for key, value in pgSz_Mar.attrib.items():
                                            docx_dic["sectPrPre" + str(sectPrPre_count) + "_" + pgSz_Mar.tag.split('}')[1] + "_" + key.split('}')[1]] = value
                                        
                                        
                                # 적용된 스타일 까지 가져오려면 header1.xml 같은거 참조해서 글자마다 적용된 스타일 긁어와야 함 
                            else:
                                break


            if child.tag.split('}')[1] == 'sectPr' :
                # https://learn.microsoft.com/en-us/previous-versions/office/developer/office-2003/aa196610(v=office.11) 
                for pgSz_Mar in child : 
                    # 헤더 푸터 내용 스타일 파싱 
                    if pgSz_Mar.tag.split('}')[1] == "footerReference" or pgSz_Mar.tag.split('}')[1] == "headerReference":
                        # Open the relationships XML file and parse the contents
                        root = ET.fromstring(doc_zip.read('word/_rels/document.xml.rels'))
                        
                        for key, value in pgSz_Mar.attrib.items() :
                            if "type" in key : 
                                docx_dic["sectPr" + "_" + pgSz_Mar.tag.split('}')[1] + "_"  + key.split('}')[1]] = value
                                type_name = pgSz_Mar.tag.split('}')[1] + "_" + value
                            if "id" in key  :          
                                for rel in root.findall("r:Relationship", ns):
                                    rid = rel.attrib.get("Id")
                                    target = rel.attrib.get("Target")
                                    if (rid == value) : 
                                        header_footer_xml = ET.fromstring(doc_zip.read('word/'+target))
                                        for body in header_footer_xml:
                                            if body.tag.split('}')[1] == 'p': 
                                                for pPr in body : 
                                                    if pPr.tag.split('}')[1] == "pPr" : 
                                                        for sectPrPre in pPr:
                                                            for key, value in sectPrPre.attrib.items():
                                                                docx_dic[type_name  + "_" + sectPrPre.tag.split('}')[1] + "_" + key.split('}')[1]] = value

                    else : 
                        for key, value in pgSz_Mar.attrib.items() :
                            docx_dic[child.tag.split('}')[1] + "_"+pgSz_Mar.tag.split('}')[1]+"_"+key.split('}')[1]] = value
                        
    #print()
    #print(" STYLE ")
    styles_xml = doc_zip.read('word/styles.xml')
    root = ET.fromstring(styles_xml)
    for body in root:

        for child in body :
            # print(child.tag)
            if child.tag.split('}')[1] == "rPrDefault" : 
                for rPr in child :
                    # print(rPr.tag)
                    for P in rPr :
                        # print(P.tag)
                        # print('==' + P.tag.split('}')[1])
                        for key, value in P.attrib.items() :
                            docx_dic["rPrDefault_" +P.tag.split('}')[1]+"_"+key.split('}')[1]] = value
                            # print("rPrDefault_" +P.tag.split('}')[1]+"_"+key.split('}')[1], ' : ', value)
            
            if child.tag.split('}')[1] == "pPrDefault" : 
                for pPr in child :
                    for P in pPr :
                        #print('==' + P.tag.split('}')[1])
                        value = -1
                        for key, value in P.attrib.items() :
                            docx_dic["pPrDefault_" + P.tag.split('}')[1]+"_"+key.split('}')[1]] = value
                            # print("pPrDefault_" + P.tag.split('}')[1]+"_"+key.split('}')[1], ' : ', value)

        if body.tag.split('}')[1] == "style" :
            style_dic = {k.split('}')[1]: v for k, v in body.attrib.items()}
            for name in body : 
                if name.tag.split('}')[1] == "name" : 
                    style_name_dic = {k.split('}')[1]: v for k, v in name.attrib.items()}
                    if style_dic['type'] + "_name" in docx_dic.keys() : 
                        docx_dic[style_dic['type'] + "_name"].append(style_name_dic['val'])
                    else : 
                        docx_dic[style_dic['type'] + "_name"] = list()
                        docx_dic[style_dic['type'] + "_name"].append(style_name_dic['val'])
                    # print(style_dic['type'] + "_name  :", style_name_dic['val'])

    #print()
    #print(" FONT TABLE ")
    fontTable_xml = doc_zip.read('word/fontTable.xml')
    root = ET.fromstring(fontTable_xml)
    docx_dic["fontList"] = list()
    for body in root:
        if body.tag.split('}')[1] == "font" : 
            font_dic = {k.split('}')[1]: v for k, v in body.attrib.items()}
            docx_dic["fontList"].append(font_dic['name'])
            #print(body.tag.split('}')[1], " : ",font_dic['name'])

    #print()
    #print(" NUMBERING ")
    # try : 
    #     numbering_xml = doc_zip.read('word/numbering.xml')
    #     root = ET.fromstring(numbering_xml)
    #     docx_dic["numbering_abstractNum"] = 0
    #     for abstractNum in root:
    #         for lvl in abstractNum : 
    #             if lvl.tag.split('}')[1] == "lvl" :
    #                 # 번호매기기 개수 설정
    #                 docx_dic["numbering_abstractNum"] = docx_dic["numbering_abstractNum"]  + 1 
    #                 # for child in lvl : 
    #                 #     for key, value in child.attrib.items() :
    #                 #         # 이 내용은 다 파싱하는 것들 
    #                 #         docx_dic["numbering_abstractNum_lvl_" +child.tag.split('}')[1]] = value
    #                 #         print("numbering_abstractNum_lvl_" +child.tag.split('}')[1], " : ",value)

    # except :
    #     pass

    #print()
    #print(" COLLECT FEATURE ")
    # for key, value in docx_dic.items() : 
    #     print(key, value)
     #여기까지가 디폴트 설정인데 27개 수집 가능 근데 설정을 세팅하면 기본 값이 아닐 경우 Feature 추가됨 
    return docx_dic

#   #전처리 하면서 
# 
# 
# 
# import os, datetime, tqdm
# import pandas as pd
# dataframe = pd.DataFrame()
# file_path = "[20230417] DOCX-NOMAGIC-total\\새 폴더"
# now = datetime.datetime.now()
# outputcsv = "[" + now.strftime("%Y%m%d") + "] testpre.csv"
# for dirname, _, filenames in os.walk(file_path):
#     for filename in  tqdm.tqdm(filenames):
#         file_path = os.path.join(dirname,filename)
#         dataframe = dataframe.append(feature_extraction(file_path), ignore_index=True)

# # dataframe = dataframe.applymap(lambda x: x.replace('\xa0','').replace('\xa9',''))
# dataframe.to_csv(outputcsv, encoding="utf-8-sig" )
# # DP.datapreprocessing(dataframe,outputcsv)