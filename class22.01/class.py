def read_table(file_name):
    with open (file_name, encoding = 'utf-8') as file:
        lines = file.readlines()[8:]
    return lines
def word_order(lines):
    orders = {}
    for line in lines:
        cells = line.split('\t')
        wo = cells[3]
        if wo in orders:
            orders[wo] += 1
        else:
            orders[wo] = 1
    return orders
def main():
    print('start')
    lines = read_table('81A.tab.txt')
    stats = word_order(lines)
    print(stats)
    for wo in stats:
        print(wo, stats[wo])

if __name__ == '__main__':
    main()
