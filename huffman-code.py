# 허프만 트리의 노드를 표현하기 위한 클래스
import heapq
from collections import Counter


# 허프만 트리의 노드 클래스
class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq  # 노드의 빈도
        self.char = char  # 리프 노드일 경우 문자 값
        self.left = left  # 왼쪽 자식
        self.right = right  # 오른쪽 자식

    # heapq에서 비교를 위해 __lt__ 정의 (빈도가 낮은 순)
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    """문자열의 빈도를 이용하여 허프만 트리를 구성합니다."""
    freq_counter = Counter(text)
    heap = []
    # 각 문자를 리프 노드로 초기화하여 최소 힙에 넣기
    for char, freq in freq_counter.items():
        heapq.heappush(heap, Node(freq, char))

    # 두 개의 최소 빈도 노드를 꺼내서 하나의 부모 노드로 합치기
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(node1.freq + node2.freq, left=node1, right=node2)
        heapq.heappush(heap, merged)

    # 최종 남은 노드가 트리의 루트
    return heap[0]


def build_codes(root, prefix="", codebook=None):
    """재귀적으로 트리를 순회하며 각 문자에 대한 허프만 코드를 생성합니다."""
    if codebook is None:
        codebook = {}
    # 리프 노드인 경우, 코드북에 추가
    if root.char is not None:
        codebook[root.char] = prefix or "0"  # 예외: 트리에 하나의 문자만 있는 경우
    else:
        build_codes(root.left, prefix + "0", codebook)
        build_codes(root.right, prefix + "1", codebook)
    return codebook


def encode_text(text, codebook):
    """코드북을 사용해 문자열을 인코딩합니다."""
    encoded = "".join(codebook[char] for char in text)
    return encoded


def decode_text(encoded_text, root):
    """
    인코딩된 비트열과 허프만 트리의 루트를 이용해
    원본 문자열로 디코딩합니다.
    """
    decoded = []
    current = root
    for bit in encoded_text:
        # '0'이면 왼쪽, '1'이면 오른쪽으로 이동
        if bit == "0":
            current = current.left
        else:
            current = current.right

        # 리프 노드(문자)인 경우, decoded에 추가하고 루트로 재설정
        if current.char is not None:
            decoded.append(current.char)
            current = root
    return "".join(decoded)


if __name__ == "__main__":
    text = "BETTER_LATE_THAN_NEVER"
    print("원본 문자열:", text)

    # 1. 허프만 트리 구성
    root = build_huffman_tree(text)

    # 2. 각 문자에 대한 허프만 코드 생성
    codes = build_codes(root)
    print("허프만 코드:")
    for char in sorted(codes):
        print(f"  '{char}': {codes[char]}")

    # 3. 문자열 인코딩
    encoded_text = encode_text(text, codes)
    print("\n인코딩된 비트열:", encoded_text)
    print("총 인코딩 비트 수:", len(encoded_text))

    # 4. 인코딩된 비트열 디코딩
    decoded_text = decode_text(encoded_text, root)
    print("\n디코딩된 문자열:", decoded_text)

    # 인코딩 전/후 비교
    print("\n디코딩이 올바른지 확인:", text == decoded_text)
