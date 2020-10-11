# ShinyColors assets classifier

인겜 애셋들을 opencv로 열어보고   
열리면 이미지 크기에 따라 분류하고  
열리지 않으면 `sorted/misc`에 저장합니다.  

## Usage
1. `https://chrome.google.com/webstore/detail/save-all-resources/abpdnfjocnmdomablahdcfnoggeeiedb`  
를 이용해 파일들을 저장합니다.  
2. 위 프로그램을 이용하면 `shinycolors.enza.fun.zip` 과 같은 형태의 압축 파일이 나옵니다  
3. 이 중 `shinycolors.enza.fun/shinycolors.enza.fun/assets` 폴더를 본 레포 메인 디렉토리 아래에 위치시킵니다.  
4. `python classifier.py`

## 분류 설명
현재 각 파일을 다음과 같이 분류하고 있습니다.  
`SD_Standing`, `SD_Head`, `Standing`, `Illust`, `Icon_Card`, `Icon_clothes`,  
`Icon_Character`, `Icon_Small`, `Banner`, `Img_Head`, `Sign`, `Parts`, `CardName`,  
`img_misc`, `misc`

`img_misc`의 경우 이미지이지만 분류 기준에 걸리지 않은 것들이 속하며,  
`misc`의 경우 이미지로 열리지 않는 파일들이 속합니다.

분류 기준은 `classifier.py`를 참고하시기 바랍니다.