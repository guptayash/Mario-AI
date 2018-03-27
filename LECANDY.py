if __name__ == '__main__':
    testCase=int(input())
     
    for i in range(testCase):
            N,C=map(int,input().split())
            AK= list(int(n) for n in input().split())
            if sum(AK)>C:
                    print("No")
            else:
                    print("Yes")
