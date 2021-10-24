# TREE

## TREE란?
+ 1개의 root 노드를 갖는다
+ 부모-자식 관계의 서브트리로 구성되며 서로 연결된 노드의 집합
+ 부모에서 자식으로 간선이 이어져 있는 유향 그래프
  - 항상 단방향이므로 화살표 생략 가능

## TREE의 특징
+ Recursively Defined(재귀로 정의된)
  - 트리의 순회에서 재귀 순회가 자연스러움
+ Self-Referential(자기 참조 자료구조)
  - 트리의 자식도 트리이며 그 자식도 트리 => 서브트리 구성됨

## TREE의 용어
<img src="https://gmlwjd9405.github.io/images/data-structure-tree/tree-terms.png">
출처 : (https://gmlwjd9405.github.io/2018/08/12/data-structure-tree.html)  

##
+ root : 부모가 없는 노드, 트리는 하나의 root를 갖는다
+ leaf : 자식이 없는 노드
+ edge : 노드와 노드를 연결하는 선(부모-자식 노드 간 edge로 연결)
+ Degree : 자식 노드의 개수
  - E의 Degree : 1
+ size : 자신을 포함한 모든 자식 노드의 개수
  - D의 Size : 3
+ Height : 현재 위치에서부터 leaf까지의 거리 
  - A의 Height : 3
+ Depth : root에서부터 현재 노드까지의 거리
  - F의 Depth : 2
+ level : 트리의 특정 깊이를 가지는 노드의 집합
  - 보통 0부터 시작

## GRAPH vs TREE
+ TREE는 순환 구조를 갖지 않는 그래프
  - 특수한 형태의 그래프의 일종
+ TREE는 어떠한 경우에도 한번 연결된 노드가 다시 연결 되지 X
+ TREE는 부모->자식 단방향만 가능

## BINARY TREE
+ 모든 노드의 degree가 2 이하인 TREE
  - left, right 최대 2개의 자식을 갖는 단순한 형태
 <img src="https://media.vlpt.us/images/bining/post/ce56d9b1-bf9f-4480-be0b-74818c877e98/image.png">
출처 : (https://velog.io/@bining/data-structure-tree)  

##
+ Full Binary Tree(정 이진 트리)
  - 모든 노드가 0개 또는 2개의 자식노드를 갖는다
+ Complete Binary Tree(완전 이진 트리)
  - 마지막 level을 제외하고 모든 level이 완전히 채워져 있다
  - 마지막 level의 모든 node는 가장 왼쪽부터 채워져 있다
+ Perfect Binary Tree(포화 이진 트리)
  - 모든 노드가 2개의 자식 노드를 갖고 있다
  - 모든 leaf 노드는 동일한 depth 또는 level을 갖는다

## 이진 탐색 트리(BST)
<img src="https://i.imgur.com/po0R4GB.png">
출처 : (https://ratsgo.github.io/data%20structure&algorithm/2017/10/22/bst/)

##
+ 왼쪽, 오른쪽 값들이 각각 크기에 따라 정렬되어 있는 트리
+ 노드.left.value < 노드.value
+ 노드.value > 노드.right.value
+ 탐색 시간 복잡도 : O(log n)
  - but, 균형 깨진 경우 시간 복잡도 : O(n)에 근접 => 비효율적(BST 장점X)

## 자기 균형 이진 탐색 트리
+ 삽입, 삭제 시 자동으로 높이를 작게 유지하는 노드 기반의 이진 탐색 트리
+ Height를 가능한 한 작게 유지한 트리
+ AVL 트리
+ 레드-블랙 트리
  - 자바의 Haspmap : 해시 테이블의 개별 체이닝 시 연결 리스트와 함께 레드-블랙 트리 병행해 저장 => 효율적