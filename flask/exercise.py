######################바다코끼리 연산자######################
"""
:=
할당과 테스트를 한번에
"""
from asyncio import tasks


tweet_limit = 280
tweet_string = "blah"*50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))

tweet_limit2 = 100
tweet_string2 = "blah"*50
if diff:= tweet_limit2 - len(tweet_string2) >= 0: #할당과 테스트를 한단계로 줄임
    print('A fitting tweet2')
else:
    print("Went over by", abs(diff))


######################문자열 슬라이스######################
"""
[:] 처음부터 끝까지 전체 시퀀스 추출
[start :] start 오프셋부터 끝까지 시퀀스 추출
[: end] 처음부터 end-1 오프셋까지 시퀀스 추출
[start : end] start 오프셋부터 end-1 오프셋까지 시퀀스 추출
[start : end : step] step 만큼 문자를 건너뛰면서 start 오프셋부터 end-1 오프셋까지 시퀀스 추출

시작지점에서 오른쪽 -> 0, 1, 2 ...
끝에서 왼쪽 -> -1, -2, -3...
"""
#처음부터 e까지 추출해보기
letters = "abcdefg" 
sliced = letters[:-2] #-2면 실제로는 -3까지 추출된다
print(sliced) #abcde


######################문자열 split######################
"""
하나의 문자열을 작은 문자열들의 "리스트"로 나눈다.
split() 함수를 사용한다.
구분자(separator)지정하지 않으면 공백문자를 사용한다.
"""
tasks = 'get gloves, get mask, give cat vitamins, call ambluance'
print(tasks.split(',')) #['get gloves', ' get mask', ' give cat vitamins', ' call ambluance']


######################문자열 join######################
"""
문자열 리스트를 하나의 문자열로 결합
"""
crypto_list = ['yeti', 'bigfoot', 'loch ness monster']
crypto_string = ', '.join(crypto_list)
print(crypto_string)

