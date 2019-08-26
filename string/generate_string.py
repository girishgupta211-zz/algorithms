# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A, B, C):
    result = ""
    while A > 0 or B > 0 or C > 0:

        if A > B+C and result.endswith('a') is False:
            pass

        if A > 0 and result.endswith('a') is False:
            if A > 0:
                result = result + 'a'
                A -= 1
            if A > 0:
                result += 'a'
                A -= 1

        if B > 0 and result.endswith('b') is False:
            if B > 0:
                result = result + 'b'
                B -= 1
            if B > 0:
                result += 'b'
                B -= 1

        if A > 0 and result.endswith('a') is False:
            if A > 0:
                result = result + 'a'
                A -= 1
            if A > 0:
                result += 'a'
                A -= 1

        if C > 0 and result.endswith('c') is False:
            if C > 0:
                result = result + 'c'
                C -= 1
            if C > 0:
                result += 'c'
                C -= 1

        if result.endswith('a') is True and B == 0 and C == 0:
            break

        if result.endswith('b') is True and A == 0 and C == 0:
            break

        if result.endswith('c') is True and A == 0 and B == 0:
            result = 'cc' + result
            break

            # return result

    # print(result)
    return result


# Driver code
if __name__ == "__main__":
    # A = 6
    # B = 1
    # C = 1
    # print(solution(A, B, C))

    A = 0
    B = 1
    C = 8
    print(solution(A, B, C))
