name="传智播客"
stock_price=19.99
stock_code="003032"
stock_price_growth_factor=1.2
growth_days=7

print(f"公司：{name}，股票代码：{stock_code}，当前股票：{stock_price}") 
stock_price=stock_price*stock_price_growth_factor**growth_days
print('每日增长系数是：%d，经过%d的增长后，股价达到了：%5.2f'%(stock_price_growth_factor,growth_days,stock_price))