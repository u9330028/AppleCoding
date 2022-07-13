# MultiDict 데이터 타입 : GET과 POST 메서드로 넘어온 데이터를  (키, 값) 튜플 형태의 리스트 타입이다.
# MultiDict 타입에서 제공하는 메서드
# get, getlist, add, setlist, setdefault, setlistdefault, clear, copy, deepcopy, pop. poplist, update

# add : MultiDict에 키와 값을 추가하는 메소드
# setdefault : add 메소드와 거의 비슷하게 동작하지만, 변수가 있을 때는 그변수의 값을 리터을 하고
#                    설정하고자 하는 변수가 없을 때 default값으로 데이터를 추가한다.

# copy(얕은복사): MultiDict 데이터의 변수값이 리스트 타입으로 있는 경우 그 리스트 타입의 메모리 주소를
#                           복사

# deepcopy(깊은복사) : 리스트 타입의 메모리 주소가 아니라, 그 데이터를 복사

# pop : get메소드와 유사한 동작을 하지만 기능적인 차이가 있다. get메소드는 MultiDict 데이터 변수에서
#           특정 변수 키의 키값을 메모리에서 복사해서 프로그램에 리턴을 하는 반면에,
#           pop은 변수 키의 키값을 복사하는 것이 아니라 MultiDict 데이터 변수에서 변수 키를 제거하고 그값을
#           리턴한다.

#poplist: pop 메소드와 같은 동작을 하지만 같은 이름의 변수 키로 여러 값이 들어올 때 이 값들을 꺼내올 때
#             사용한다. getlist와의 차이점은 꺼내온 뒤에 기존의 MultiDict 변수의 키를 제거한다.

# update : 기존의 MultiDict 타입 변수에 다른 MultiDict 타입 변수의 내용을 삽입할 때 사용
