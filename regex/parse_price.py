import re
import sys

def get_price_value(item):
    '''
    key function to sort by price for a list as below.
    [
        ["item name 1", "1,100"]
        ["item name 2", "1,200"]
        ....
    ]
    '''
    return int(item[1].replace(',', ''))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <input daraz.html file>')
        exit(1)

html_file = sys.argv[1]

'''
<a age="0" href="https://www.daraz.lk/products/havit-optical-wired-mouse-ms871-i121192924-s1042965829.html?search=1" title="Havit Optical Wired Mouse MS871">Havit Optical Wired Mouse MS871</a></div><div class="c3gUW0"><span class="c13VH6">Rs. 480</span></div>
'''

price_line_pattern = re.compile('search=1"\s+title=.*?Rs\.\s+[\d,]+')
item_price_pattern = re.compile('>([^<]+)<.*Rs\.\s+([\d,]+)')

with open(html_file) as f:
    data = f.read()

item_prices = price_line_pattern.findall(data)

items_list = []
for i in item_prices:
    items = item_price_pattern.search(i).groups()
    items_list.append([items[0], items[1]])

sort_items = sorted(items_list, key=get_price_value) 

print(f'{"ITEM":60} PRICE(Rs)')
for i in sort_items:
    print(f'{i[0][:78]:80} {i[1]}')



