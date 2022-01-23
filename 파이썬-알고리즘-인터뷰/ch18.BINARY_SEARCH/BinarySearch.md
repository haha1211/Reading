# Binary Search

## Binary Search란?
- 이진검색
- 정렬된 배열에서 타겟을 찾는 검색 알고리즘
- 시간복잡도 : O(log n)

## Binary Search의 동작 과정
1. 찾고자 하는 값 X를 찾을 때까지 아래 과정 반복
    1. 배열의 중간에 있는 값을 선택하여 X와 비교
    2. X가 중간값보다 작으면 중간값 기준 좌측 데이터들을 대상으로 다시 탐색
    3. X가 중간값보다 크면 중간값 기준 우측 데이터들을 대상으로 다시 탐색
2. 탐색하고자 하는 배열이 더 이상 없을 경우 => 찾고자 하는 값이 배열에 존재X

## python 내 binary search 라이브러리
- bisect_left(a,x) => 배열 a내에서 x를 삽입할 가장 왼쪽 위치(index)를 찾는 method
- bisect_right(a,x) => 배열 a내에서 x를 삽입할 가장 오른쪽 위치(index)를 찾는 method
