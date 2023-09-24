# DFC-TECH-2023
DFC-TECH-2023

# docx_GUI

- 워드 파일 전처리 후 분류하는 코드 정리

![image](https://github.com/joseoyeon/DFC-TECH-2023/assets/46625602/babde063-5dc9-49a7-9571-d14297f4d2f7)

---

### EXE 빌드 명령어 

```python
pyinstaller --noconfirm  --windowed --icon "WORD_LOGO.ico" "main.py"
```

### cx_freeze로 앱 만들때 필요한 모듈
- PyQt5.QtWidgets
- PyQt5.QtCore
- PyQt5.QtGui
- pandas
- numpy
- sklearn
- functools
- re
- zipfile
- xml.etree.ElementTree

# 도구 사용 방법
1.	서로간의 유사도를 파악하고 싶은 Docx 문서를 모아 하나의 폴더에 넣습니다.
A.	본 예시에서는 NapiorOne에서 제공하는 데이터 셋을 대상으로, 인간이 판단했을 때, 조직 로고와 외형적으로 유사하다 판단이 되는 문서를 폴더별로 분류해서 사용했습니다.
 
![image](https://github.com/joseoyeon/DFC-TECH-2023/assets/46625602/86a253f8-7e53-468c-9445-2ecc3e142445)


2.	Word Search 프로그램을 실행합니다.  실행 파일은 WordSearch.exe 입니다. 
 
![image](https://github.com/joseoyeon/DFC-TECH-2023/assets/46625602/189b2597-7716-4295-8b90-d18acdf22c1d)

 
3.	Word Search 프로그램을 실행하여 문서 데이터 셋이 존재하는 폴더 경로를 넣고,  프로그램이 출력한 전처리 csv 를 저장할 저장할 경로를 넣습니다.
* GUI가 나타나기 까지 약 10초정도의 시간이 필요합니다
 
![image](https://github.com/joseoyeon/DFC-TECH-2023/assets/46625602/2e4ac91d-bf6f-41e1-96e8-7ddcc16f6f7c)


4.	전처리 시작을 누르면 폴더 경로에 넣은 Word 파일에서 필요한 정보를 추출하여 출력 파일 경로의 CSV 파일에 저장합니다. 
 
![image](https://github.com/joseoyeon/DFC-TECH-2023/assets/46625602/7993c0c6-ca7e-43fc-af12-cdbc2b3e871a)

A.	검색에 사용되는 Feature 들을 추출한 CSV 예시 
i.	(“[20230915] preprocessing_DOCX-NOMAGIC-total.csv”)
 
![image](https://github.com/joseoyeon/DFC-TECH-2023/assets/46625602/62602360-ddda-4ed1-a8a9-8f6568d71b6e)

5.	파일 로드 버튼을 눌러서 출력 파일 경로에 있는 CSV 파일을 넣습니다.

![image](https://github.com/joseoyeon/DFC-TECH-2023/assets/46625602/db82f19a-592c-4b8b-921a-e6abd8c0260d)


6.	검색 옵션을 설정합니다. 프로그램에서 Default 로 지정한 값을 그대로 사용해도 됩니다.  
A.	[유사도 측정 알고리즘], [유사 측정 기준], [사용하는 피처 개수] 옵션을 조정 가능
i.	유사도 측정 알고리즘 : 문서간 유사도를 계산하는 알고리즘 (cosine/pearson)
ii.	유사 측정 기준 : 문서 간 유사도가 유사 측정 기준 이상인 파일만 결과로 출력 (0~100)
iii.	사용하는 피처 개수 : 사용된 전체 피처들 개수는 default 값으로 설정되며, Feature 선정 체크 박스를 선택하고 사용하는 피처 개수를 조정하면 해당 피처만을 이용하여 검색 가능  
 
![image](https://github.com/joseoyeon/DFC-TECH-2023/assets/46625602/cc9cc8f1-0f9e-49f1-a9c5-9cb46e45c384)


7.	왼쪽 검색 텍스트 박스에 검색하고 싶은 이름을 검색하면 왼쪽 화면에 필터링 되어서 리스트를 보여줍니다. 
 
![image](https://github.com/joseoyeon/DFC-TECH-2023/assets/46625602/e0011bfe-941b-4e60-89f0-644d16394579)

8.	왼쪽 화면 리스트에서 검색하고 싶은 파일 이름을 클릭하면, 오른쪽 검색 대상 파일 명에 해당 파일의 이름이 들어갑니다. 검색 버튼을 누르면 검색 대상 파일과 유사한 외형적 구조를 가진 문서의 리스트를 띄워줍니다. 
 
![image](https://github.com/joseoyeon/DFC-TECH-2023/assets/46625602/fd29e726-dd5b-4992-bd7f-00328f0860cb)


9.	왼쪽 오른쪽 화면에 출력되는 DOCX 문서 이름 목록 중 하나를 클릭하고 파일 열기 버튼을 누르면 해당파일을 WORD 프로그램을 열어 파일을 볼 수 있습니다. 
 
![image](https://github.com/joseoyeon/DFC-TECH-2023/assets/46625602/6e4c6bf4-c7a5-431c-98d5-42e227998279)


10.	Export CSV 버튼을 누르면 검색 결과가 되는 파일 목록과 함께 유사도 알고리즘 계산에 사용한 특징 정보를 CSV 파일로 저장합니다. 저장 경로는 출력 파일 경로로 설정한 폴더 경로 입니다.
 
![image](https://github.com/joseoyeon/DFC-TECH-2023/assets/46625602/59d90a51-9808-4522-b1d9-75f1657f01ee)

# 고려한 특징 정보 

![image](https://user-images.githubusercontent.com/46625602/230552907-c8c020a0-9f82-47ae-af96-019b001397c4.png)

![image](https://user-images.githubusercontent.com/46625602/230552950-4f2c88ac-f91c-4562-86d8-089317ea98c9.png)

![image](https://user-images.githubusercontent.com/46625602/230552969-547c1142-0958-4160-8708-e0de8c93bcce.png)

![image](https://user-images.githubusercontent.com/46625602/230552986-d2003da3-5338-4a5c-8d5d-3710edbb8e65.png)

![image](https://user-images.githubusercontent.com/46625602/230553018-9788a06b-e519-4571-bcb9-0bc0f2eadc6a.png)
