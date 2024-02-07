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


###	STYLE.XML 특징 
/word/style.xml : Microsoft Word 문서에서 사용되는 스타일을 정의하는 XML 파일이다. 문서의 서식, 글꼴, 크기, 간격 등을 지정하는 스타일 요소들이 포함된다. 문서 전체에 적용되는 기본 스타일부터 문서 내 정의된 폰트 스타일 까지 다양한 스타일이 포함된다.
서식 추출은  styles.xml 파일 내 자식 요소 중 "rPrDefault", "pPrDefault", "style" 태그를 가진 노드의 자식 요소를 순환하며 해당 요소의 속성의 키와 값을 추출한다.
rPrDefault는 현재 문서에 대한 기본 실행 속성 집합을 지정한다. 실제 실행 속성은 현재 요소의 rPr 하위 요소 내에 저장된다. 이 요소가 생략되면 현재 문서의 기본 실행 속성이 존재하지 않는다. 즉, 문서에 기본 실행 속성이 정의되지 않는다면 기본값은 응용프로그램에서 정의한 내용으로 표현된다. 
pPrDefault는 현재 문서에 대한 기본 단락 속성 집합을 지정한다. 실제 단락 속성은 현재 요소의 pPr 자식 요소 내에 저장된다. 이 요소가 생략되면 현재 문서의 기본 단락 속성이 존재하지 않는다. 즉, 문서에 기본 실행 속성이 정의되지 않는다면 기본값은 응용프로그램에서 정의한 내용으로 표현된다.  
style 요소는 type 속성(attribute) 값으로 문단, 글자, 표, 번호 지정(Paragraph, Character, Table, Numbering_ name)을 가지고 있으며, 이 값을 통해 어떤 요소를 지정한 스타일인지 식별할 수 있다. 해당 태그의 하위 요소(name)에서 스타일명과 함께 세부 스타일을 지정하여 style.xml 파일에 포함한다. 문서 내에 해당 필드명(paragraph_name, characher_name, table_name, numbering_name)으로 정의된 내용은 없으나 속성명은 각각 문단, 글자, 표, 번호 지정에 사용된 스타일 명 리스트라는 의미로 명명된 것이다.



파일 내 속성 경로 | 속성 명 | 속성 내용 | 필수 여부
-- | -- | -- | --
[rPrDefault]-[rPr]-[rFonts] | hint | 표시에 사용될 글꼴에 대한 힌트를   word 설정 (default, fareast, cs) | 선택
  | ascii | 아스키 코드 기본 폰트 | 선택
  | eastAsia | 한글 기본 폰트 (동아시아 문자에   사용되는 글꼴) | 선택
  | hAnsi | 안시 기본 폰트 | 선택
  | cs | 코드 기본 폰트 (복잡한 스크립트에   사용되는 글꼴) | 선택
[rPrDefault]-[rPr]-[i] | val | 기울임 꼴 (on/off) | 선택
[rPrDefault]-[rPr]-[smallCaps] | val | 소문자를 작은 대문자로 옵션 선택   (on/off) | 선택
[rPrDefault]-[rPr]-[dstrike] | val | 이중 취소선 효과 (on/off) | 선택
[rPrDefault]-[rPr]-[Color] | val | 모든 텍스트의 글꼴 색 (FF0000) | 선택
[rPrDefault]-[rPr]-[kern] | val | 요소는 텍스트 실행에 대한 기본   키닝(문자 간 간격)을 지정 | 필수
[rPrDefault]-[rPr]-[sz] | val | 텍스트 실행의 문자에 대한 기본 글꼴   크기 | 필수
[rPrDefault]-[rPr]-[szCs] | val | 텍스트 실행의 문자에 대한 기본 글꼴   크기(초기 값 저장) | 필수
[rPrDefault]-[rPr]-[lang] | val | 텍스트 실행의 기본 언어 (en-US)   (라틴어 설정) | 선택
  | eastAsia | ko-KR   (아시아 언어 설정) | 선택
  | bidi | ar-SA   (복잡한 스크립트 언어 설정) | 선택
[rPrDefault]-[rPr]-[rStyle] | val | 해당 r의 문자 스타일을 나타냄 | 필수
[rPrDefault]-[rPr]-[b-cs] | val | 복잡한 스크립트 문자를 굵게 설정   (on/off) | 선택
[rPrDefault]-[rPr]-[i-cs] | val | 복잡한 스크립트 문자를 이탤릭체로 설정   (on/off) | 선택
[rPrDefault]-[rPr]-[caps] | val | 소문자 텍스트를 대문자로 포맷합니다.   숫자, 문장 부호, 알파벳이 아닌 문자 또는 대문자에는 영향을 주지 않음. | 선택
[rPrDefault]-[rPr]-[strike] | val | 텍스트를 통해 선을 그림(on/off) | 선택
[rPrDefault]-[rPr]-[outline] | val | 각 문자의 내부 및 외부 테두리 표시 | 필수
[rPrDefault]-[rPr]-[shadow] | val | 텍스트 뒤, 텍스트 아래 및 오른쪽에   그림자 추가 (on/off) | 선택
[rPrDefault]-[rPr]-[emboss] | val | 텍스트가 양각으로 페이지에서 올라온   것처럼 보이게 함 (on/off) | 선택
[rPrDefault]-[rPr]-[imprint] | val | 선택한 텍스트가 각인되거나 페이지에   눌려진 것처럼 보이게 함. (조각이라고도 함) (on/off) | 선택
[rPrDefault]-[rPr]-[noProof] | val | 이 실행에서 맞춤법 및 문법 오류가   무시되도록 텍스트 서식 지정. (on/off) | 선택
[rPrDefault]-[rPr]-[snapToGrid] | val | 현재 섹션 속성의 docGrid 요소에   지정된 문자 수와 일치하도록 줄 당 문자 수 설정 (on/off) | 선택
[rPrDefault]-[rPr]-[vanish] | val | 이 실행의 텍스트가 표시되거나 인쇄되지   않도록 함 (on/off) | 선택
[rPrDefault]-[rPr]-[webHidden] | val | 이 문서가 웹 페이지로 저장될 때 이   실행의 텍스트가 표시되지 않도록 함 (on/off) | 선택
[rPrDefault]-[rPr]-[spacing] | val | 문자 사이의 간격이 확장되거나 축소되는   양 나타냄(on/off) | 필수
[rPrDefault]-[rPr]-[w] | val | 텍스트를 현재 크기의 백분율로 가로로   늘리거나 줄임. (minInclusive = 1 / maxInclusive = 600) | 선택
[rPrDefault]-[rPr]-[position] | val | 기준선과 관련하여 텍스트를 올리거나   내려야 하는 양 나타냄. | 필수
[rPrDefault]-[rPr]-[highlight] | val | 주변 텍스트에서 눈에 띄도록 텍스트를   강조 표시   (black/blue/cyan/green/magenta/red/yellow/white/dark-blue/dark-cyan/dark-green/dark-magenta/dark-red/dark-yellow/dark-gray/light-gray/none) | 필수
[rPrDefault]-[rPr]-[u] | val | 이 실행에 대한 밑줄 서식 나타냄 | 선택
[rPrDefault]-[rPr]-[effect] | val | 이 실행에 대한 애니메이션 텍스트 효과   나타냄 (blink-background/lights/ants-black/ants-red/shimmer/sparkle/none) | 필수
[rPrDefault]-[rPr]-[bdr] | val | 이 실행에서 문자의 테두리 나타냄 | 필수
  | color | 테두리 색상 설정 | 선택
  | sz | 테두리 너비 설정 | 선택
  | space | 포인트의 1/8 지점에서 테두리 공간   설정 | 선택
  | shadow | 테두리에 그림자가 있는지 여부   설정(on/off) | 선택
  | frame | 테두리를 반전시켜 프레임 효과를 만들   것인지 여부 설정(on/off) | 선택
  | wx:bdrwidth | 외부 네임스페이스 참조 | 선택
[rPrDefault]-[rPr]-[shd] | val | 음영 스타일 값 설정 | 필수
  | color | 전경 음영 색상 값 설정 | 선택
  | fill | 배경 채우기 색상 값 설정 | 선택
  | wx:bgcolor | 외부 네임스페이스 참조 | 선택
[rPrDefault]-[rPr]-[fitText] | val | 텍스트가 들어갈 공간의 너비 설정. | 필수
  | id | 맞춤 텍스트의 여러 실행을 연결하는   고유한 내부 ID 설정 | 선택
[rPrDefault]-[rPr]-[vertAlign] | val | 기준선을 기준으로 텍스트의 세로 위치를   조정하고 가능한 경우 글꼴 크기를 변경합니다. 글꼴 크기를 줄이지 않고 텍스트를 올리거나 내리려면 위치 요소 지정   (baseline/superscript/subscript) | 필수
[rPrDefault]-[rPr]-[rtl] | val | 정렬 및 읽기 순서를 오른쪽에서   왼쪽으로 설정(on/off) | 선택
[rPrDefault]-[rPr]-[cs] | val | 텍스트가 복잡한 스크립트 텍스트인지   여부 지정 (true 또는 false). | 선택
[rPrDefault]-[rPr]-[em] | val | 강조 표시 유형 설정   (none/dot/comma/circle/under-dot) | 필수
[rPrDefault]-[rPr]-[hyphen] | val | 하이픈 넣기 스타일 (1포인트의   20분의 1, 1인치의 1/1440) 단위의 양수 측정 값 설정 | 필수
[rPrDefault]-[rPr]-[asianLayout] | id | 여러 아시아 텍스트 실행을 연결하는   고유한 내부 ID설정 | 선택
특별한 아시아   레이아웃 서식 속성을 나타냅니다. | combine | 줄을 결합할지 문자를 결합할지 나타내는   값 설정 (lines/letters) | 선택
  | combine-brackets | 결합된 텍스트 주위에 넣을 대괄호   스타일 설정 (none/round/square/angle/curly) | 선택
  | vert | 세로 텍스트로 제대로 표시되도록 아시아   반각 문자의 회전 값 설정합니다. (on/off) | 선택
  | vert-compress | 한 문자 단위에 맞도록 회전된 텍스트의   압축 값 설정 (on/off) | 선택
[rPrDefault]-[rPr]-[specVanish] | val | 텍스트를 항상 숨김으로 만드는 특수   숨겨진 속성을 나타냄 (on/off) | 선택
[rPrDefault]-[rPr]-[wx:font] | val | 기본 편지 병합 문서가 표시하는 활성   레코드 지정 | 필수
[rPrDefault]-[rPr]-[wx:sym] | val | 기본 편지 병합 문서가 표시하는 활성   레코드 지정 | 필수
[rPrDefault]-[rPr]-[aml:annotation] | val | 기본 편지 병합 문서가 표시하는 활성   레코드 지정 | 필수


