## 분석한 MS-WORD 특징
 본 연구에서 분석한 Word(.docx) 파일에 포함된 사용자 서식 설정 값을 세부적으로 목록화아여 정리한다. 사용자 서식 설정 값은 document.xml/style.xml/fontTalble.xml/header.xml/footer.xml 에 포함되며, 각 파일에 포함된 서식 설정 값을 표로 정리했다. 정리한 표가 갖는 컬럼은 파일내 속성 경로, 속성명, 속성 내용, 필수 여부로, 각 컬럼에 대한 설명은 아래와 같다. 
 
* 파일 내 속성 경로 : xml 파일에서 해당 서식 설정을 찾기 위해 거쳐야 할 하위 자식 요소(element) 경로를 뜻한다. 
* 속성 명 : 해당 서식 설정 값이 저장되어 있는 속성(attribute)에 대한 명칭이다. 
* 속성 내용 : 해당 서식 설정 값에 대한 설명이다. 
* 필수 여부 : 사용자가 특별히 설정한 값이 없어도 사전 정의된 (default) 값으로 저장되어, 사용자의 설정 여부와 관계없이 필수적으로 존재하는 속성(attribute)에 대해서는 “필수”, 사용자가 설정할 때만 존재하는 속성(attribute)에 대해서는 “선택” 으로 표기했다. 

###	DOCUMENT.XML 특징
/word/document.xml : Microsoft Word문서의 실제 내용을 포함하는 XML 파일이다. 사용자가 입력한 텍스트 데이터와 그에 따른 문단의 서식, 글꼴, 크기, 스타일과 같은 서식 설정 값, 그림, 표, 등 문서를 구성하는 요소들이 이 파일에 포함된다.

파일 내 속성 경로 | 속성 명 | 속성 내용 | 필수 여부
-- | -- | -- | --
[sectPr] - [pgSz] | w | 용지 너비 | 필수
(페이지 크기) | h | 용지 높이 | 필수
  | orient | 페이지 방향 (portrait /   landscape) | 선택
  | code | 크기가 프린터에서 지원하는 여러 용지   유형의 크기와 일치하는 경우 적절한 유형이 선택되도록 내부 용지 코드를 가져오거나 설정. | 선택
[sectPr] - [pgMar] | top | 페이지 위쪽 여백 | 필수
(페이지 여백) | right | 페이지 오른쪽 여백 | 필수
  | bottom | 페이지 아래쪽 여백 | 필수
  | left | 페이지 왼쪽 여백 | 필수
  | header | 페이지 머리말 여백 | 필수
  | footer | 페이지 꼬릿말 여백 | 필수
  | gutter | 페이지 제본 여백 | 필수
[sectPr]-[pgBorders] | offsetFrom | 페이지 여백을 기준으로 페이지 테두리의   위치 지정 (page / text) | 선택
(페이지 테두리) | z-order | 교차하는 텍스트 및 개체를 기준으로   페이지 테두리가 배치되는 위치 지정(front / back) | 선택
  | display | 페이지 테두리가 인쇄되는 페이지   지정(all-pages / first-page / not-first-page) | 선택
[sectPr]-[pgBorders]-[Top] | val | 선종류(single) | 선택
[sectPr]-[pgBorders]-[Left] | sz | 선 굵기(4) | 선택
[sectPr]-[pgBorders]-[Bottom] | space | 여백(24) | 선택
[sectPr]-[pgBorders]-[Right] | color | 선 색 (auto) | 선택
  | shadow | 선 그림자 (on/off) | 선택
  | frame | 테두리를 반전시켜 프레임 효과를 만들   것인지 여부 설정(on/off) | 선택
  | wx:bdrwidth | 외부 네임 스페이스 | 선택
[sectPr]-[cols] | w | 열의 너비를 가져오거나 설정합니다 | 선택
  | space | 이 열과 다음 열 사이의 공백   설정, 마지막 열에는 필요하지 않음. | 선택
[sectPr]-[docGrid] | type | 그리드 유형 설정 | 선택
  | linePitch | 줄 피치와 줄 간격 설정 페이지당 줄   수는 줄 사이의 간격에 맞게 자동으로 조정. | 선택
  | char-space | 문서의 줄당 문자 수 설정 | 선택
