# ExpressionTree.py
from binary_tree_Tues import BTNode, inorder, postorder, preorder

# 1. 모스코드 결정트리
# ===== 모스 코드 테이블 (A~Z) =====
MORSE_TABLE = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
]



# 2. 수식트리  

    







#===================================================
# 테스트 프로그램 : 결정 트리(이진 트리) 기반 모스 코드 트리
#===================================================   

# if __name__ == "__main__":
#     morseCodeTree = make_morse_tree()
#     s = input("입력 문장 : ").strip() # GAMEOVER, DATA

#     mlist = [ ]
#     for ch in s:
#       code = encode(ch) 
#       mlist.append(code)
#     print("Morse Code:", mlist)

#     print("Decoding: ", end='')
#     for code in mlist:
#         print(decode(morseCodeTree, code), end='')
#     print()
   
#==================================================
# 테스트 프로그램 코드 4.17: 수식 트리 생성 및 순회 및 평가
#=====================================================  
# if __name__ == "__main__":
#     # (1+3) * (4/2)
#     # expr = ['1', '3', '+', '4', '2', '/', '*']
#     str = input("입력(후위표기): ")
#     expr = str.split()
#     print("토큰분리(expr): ", expr)

#     root = buildTree(expr)
#     print("트리 루트:", root)

#     preorder(root)
#     print()
#     inorder(root)
#     print()
#     postorder(root)
#     print()
#     print("수식 트리 값 평가:", evaluate(root))             

#=============================
# 테스트 프로그램 QUIZ p.150 
#=============================
# if __name__ == "__main__":
#     # Construct the expression tree for expr = 2 1 3 + * 8 4 / -
#     # Tree structure:
#     # 트리 구조:
#     #        -
#     #      /   \
#     #     *      /
#     #    / \   /  \
#     #   2   +  8   4
#     #      / \
#     #     1  3
#     # 중위식: (2 * (1 + 3)) - (8 / 4)
#     postfix_expr = ['2', '1', '3', '+', '*', '8', '4', '/', '-']
#     root = buildTree(postfix_expr)  # 수식 트리 생성
#     print(root)
#     result = evaluate(root)         # 평가
#     print("평가 결과 =", result)    # 예상 결과: 6.0

