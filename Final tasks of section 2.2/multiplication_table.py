def multiplication_table():

    for i in range(1, 11):
        #
        row = []

        for j in range(1, 11):

            row.append(i * j)

        print(' '.join(f'{num:2}' for num in row))

if __name__ == "__main__":
    multiplication_table()
