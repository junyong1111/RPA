import re

#-- 4개의 문자 중 3개만 기억이 남 --> ca?e


pattern = re.compile("ca.e") 
#-- . (ca.e) : 하나의 문자를 의미 --> care, cafe, case...(O) | caffe(X) 등등
#-- ^ (^de) : 문자열의 시작  --> desk, destination...(O)  | fade(X) 등등 de로 시작하는 문자열을 의미
#-- $ (se$) : 문자열의 끝 --> case, base... (O) | face(X) 등등 문자열의 끝이 se로 끝나는 것

#-- 매치되지 않다면 에러가 발생
def print_matchs(matchs):
    if matchs: 
        print("matchs.group() :", matchs.group()) #-- 일치하는 문자열 반환
        print("matchs.string :", matchs.string) #-- 입력받은 문자열 반환
        print("matchs.start() :", matchs.start()) #-- 일치하는 문자열의 시작 Index
        print("matchs.end() : ", matchs.end()) #-- 일치하는 문자열의 끝 Index
        print("matchs.span() : ", matchs.span()) #-- 일치하는 문자열의 시작/끝 Index
    else:
        print("Not Match")  

#-- 비교하는 값이 처음부터 매치되는지 확인
matchs = pattern.match("caseless") 
print_matchs(matchs)

#-- 주어진 문자열 중에 일치하는게 있는지 확인
matchs = pattern.search("good care")
print_matchs(matchs)

#-- 일치하는 모든것을 리스트형태로 반환
matchsList = pattern.findall("good care case")
print(matchsList)