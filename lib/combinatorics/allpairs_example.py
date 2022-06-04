from lib.combinatorics import all_pairs2 as ap # https://forworktests.blogspot.com/2013/11/pairwise-testing.html

print(list(ap.all_pairs2([
        ['мужчина', 'женщина'],
        ['до 25', '25-70', 'после 70'],
        ['дети есть', 'детей нет']
        ])))

