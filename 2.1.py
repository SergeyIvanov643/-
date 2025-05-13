def char(J, S):
    count = 0

    for i in J:
        count += S.count(i)

    return count

J = "a, b"
print(f"J = {J}")

S = input("S = ")
result = char(J, S)

print(result)