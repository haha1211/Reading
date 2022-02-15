# Sliding Window

## Sliding Window란?
- 고정 사이즈의 윈도우가 이동하면서 윈도우 내에 있는 데이터를 이용해 문제를 풀이하는 알고리즘
- 네트워크에서 사용되던 알고리즘을 문제 풀이에 응용한 경우

## Sliding Window vs Two Pointer
- 정렬 여부
    + Sliding Window : 정렬 X
    + Two Pointer : 대부분 O
- 윈도우 사이즈
    + Sliding Window : 고정
    + Two Pointer : 가변
- 이동
    + Sliding Window : 좌 또는 우 단방향
    + Two Pointer : 좌우 포인터 양방향
- 실무에서 주로 이런 형태로 쓰일 뿐, 서로 혼용되어 쓰이기도 함
- 둘 사이를 명확하게 구분하는 큰 의미 X