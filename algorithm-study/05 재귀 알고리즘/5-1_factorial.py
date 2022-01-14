# 양의 정수 n의 팩토리얼 구하기

# 양의 정수 n의 팩토리얼값을 재귀적으로 구하기
def factorial(n: int) -> int:
    # 2번 조건 : n > 0 이면 n! = n * (n - 1)!
    if n > 0:
        return n * factorial(n - 1)
    # 1번 조건 : 0! = 1
    else:  
        return 1

if __name__ == '__main__':
    n = int(input('출력할 팩토리얼값을 입력하세요.: '))
    if n < 0:
        print("잘못된 입력입니다. 음이 아닌 정수를 입력하세요.")
        n = int(input('출력할 팩토리얼값을 입력하세요.: '))
    print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')
