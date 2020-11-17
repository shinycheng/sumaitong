import pandas as pd

product_weight = 0.7
product_cost = 90
product_cost_revernue_rate = 0.3
product_sale_price = 29
USD_to_RMB = 6.5
free_shipping_freight = product_sale_price * USD_to_RMB * 0.92 - product_cost - (product_cost * product_cost_revernue_rate)
freight_sum_address = r'F:\python\速卖通\运费模板\线上运费报价.xlsx'
writer = pd.ExcelWriter(r'F:\python\速卖通\运费模板\速卖通运费模板.xlsx')
#---------------------------------------------------------------------------------------------------------------------------------
#无忧标准
df_Wuyo = pd.read_excel(freight_sum_address, sheet_name = 'AliExpress无忧物流-标准')

if(product_weight < 0.1):
    df_Wuyo['应加运费'] = ((product_weight * df_Wuyo['费率(0-100g)'] + df_Wuyo[
        '挂号费(0-100g)'] - free_shipping_freight) / 0.92 / USD_to_RMB / 1.05).round(decimals=2)
    # df_Wuyo.to_excel(writer, 'AliExpress无忧物流-标准')

elif(product_weight < 0.15):
    df_Wuyo['应加运费'] = ((product_weight * df_Wuyo['费率(100-150g)'] + df_Wuyo[
        '挂号费(100-150g)'] - free_shipping_freight) / 0.92 / USD_to_RMB / 1.05).round(decimals=2)
    # df_Wuyo.to_excel(writer, 'AliExpress无忧物流-标准')

elif(product_weight < 0.175):
    df_Wuyo['应加运费'] = ((product_weight * df_Wuyo['费率(150-175g)'] + df_Wuyo[
        '挂号费(150-175g)'] - free_shipping_freight) / 0.92 / USD_to_RMB / 1.05).round(decimals=2)
    # df_Wuyo.to_excel(writer, 'AliExpress无忧物流-标准')

elif(product_weight < 0.2):
    df_Wuyo['应加运费'] = ((product_weight * df_Wuyo['费率(175-200g)'] + df_Wuyo[
        '挂号费(175-200g)'] - free_shipping_freight) / 0.92 / USD_to_RMB / 1.05).round(decimals=2)
    # df_Wuyo.to_excel(writer, 'AliExpress无忧物流-标准')

elif(product_weight < 0.3):
    df_Wuyo['应加运费'] = ((product_weight * df_Wuyo['费率(200-300g)'] + df_Wuyo[
        '挂号费(200-300g)'] - free_shipping_freight) / 0.92 / USD_to_RMB / 1.05).round(decimals=2)
    # df_Wuyo.to_excel(writer, 'AliExpress无忧物流-标准')

elif(product_weight < 0.45):
    df_Wuyo['应加运费'] = ((product_weight * df_Wuyo['费率(300-450g)'] + df_Wuyo[
        '挂号费(300-450g)'] - free_shipping_freight) / 0.92 / USD_to_RMB / 1.05).round(decimals=2)
    # df_Wuyo.to_excel(writer, 'AliExpress无忧物流-标准')

elif(product_weight < 0.605):
    df_Wuyo['应加运费'] = ((product_weight * df_Wuyo['费率(450-605g)'] + df_Wuyo[
        '挂号费(450-605g)'] - free_shipping_freight) / 0.92 / USD_to_RMB / 1.05).round(decimals=2)
    # df_Wuyo.to_excel(writer, 'AliExpress无忧物流-标准')

else:
    df_Wuyo['应加运费'] = ((product_weight * df_Wuyo['费率(606-2000g)'] + df_Wuyo[
        '挂号费(606-2000g)'] - free_shipping_freight) / 0.92 / USD_to_RMB / 1.05).round(decimals=2)
    # df_Wuyo.to_excel(writer, 'AliExpress无忧物流-标准')

#------------------------------------------------------------------------------------------------------------------------------
#燕文挂号
df_Yanwen = pd.read_excel(freight_sum_address, sheet_name = '燕文航空挂号小包')

df_Yanwen['应加运费'] = ((product_weight * df_Yanwen['费率'] + df_Yanwen[
    '挂号费'] - free_shipping_freight) / 0.92 / USD_to_RMB / 1.05).round(decimals=2)
# df_Yanwen.to_excel(writer, '燕文航空挂号小包')


#------------------------------------------------------------------------------------------------------------------------------
#中邮

df_Zhongyo = pd.read_excel(freight_sum_address, sheet_name = '中国邮政挂号小包')
if(product_weight < 0.15):
    df_Zhongyo['应加运费'] = ((product_weight * df_Zhongyo['费率(0-150g)'] + df_Zhongyo[
        '挂号费(0-150g)'] - free_shipping_freight) / 0.92 / USD_to_RMB / 1.05).round(decimals=2)
    # df_Zhongyo.to_excel(writer, '中国邮政挂号小包')

elif(product_weight < 0.3):
    df_Zhongyo['应加运费'] = ((product_weight * df_Zhongyo['费率(150-300g)'] + df_Zhongyo[
        '挂号费(150-300g)'] - free_shipping_freight) / 0.92 / USD_to_RMB / 1.05).round(decimals=2)
    # df_Zhongyo.to_excel(writer, '中国邮政挂号小包')

else:
    df_Zhongyo['应加运费'] = ((product_weight * df_Zhongyo['费率(300-2000g)'] + df_Zhongyo[
        '挂号费(300-2000g)'] - free_shipping_freight) / 0.92 / USD_to_RMB / 1.05).round(decimals=2)
    # df_Zhongyo.to_excel(writer, '中国邮政挂号小包')

#------------------------------------------------------------------------------------------------------------------------------
#包邮国家
free_shpping_country = ['俄罗斯','美国','加拿大','西班牙','法国','英国','荷兰',
                        '以色列','巴西','智利','澳大利亚','乌克兰','白俄罗斯','日本',
                        '泰国','新加坡', '韩国','印度尼西亚','马来西亚','越南','意大利',
                        '德国','沙特阿拉伯','阿拉伯联合酋长国','波兰','土耳其','葡萄牙']
free_shipping_country_list  = {'country':free_shpping_country}

df_freeshipping_country = pd.DataFrame(free_shipping_country_list).set_index(keys = ['country'])


df_Zhongyo = df_Zhongyo.set_index(keys = ['国家'])
df_Yanwen  = df_Yanwen.set_index(keys = ['国家'])
df_Wuyo    = df_Wuyo.set_index(keys = ['国家'])


s_Zhongyo = df_Zhongyo['应加运费']
s_Yanwen  = df_Yanwen['应加运费']
s_Wuyo    = df_Wuyo['应加运费']

df_freeshipping_country['中邮应加运费'] = s_Zhongyo
df_freeshipping_country['燕文应加运费'] = s_Yanwen
df_freeshipping_country['无忧应加运费'] = s_Wuyo

df_freeshipping_country = df_freeshipping_country.fillna(value = 1000)

for country in free_shpping_country:
    if (df_freeshipping_country.at[country, '中邮应加运费'] < df_freeshipping_country.at[country, '燕文应加运费'] ) & (df_freeshipping_country.at[country, '中邮应加运费'] < df_freeshipping_country.at[country, '无忧应加运费']):
        df_Zhongyo.at[country, '应加运费'] = 0
        df_Zhongyo.to_excel(writer, '中国邮政挂号小包')
    elif (df_freeshipping_country.at[country, '燕文应加运费'] < df_freeshipping_country.at[country, '无忧应加运费'] ):
        df_Yanwen.at[country, '应加运费'] = 0
        df_Yanwen.to_excel(writer, '燕文航空挂号小包')
    else:
        df_Wuyo.at[country, '应加运费'] = 0
        df_Wuyo.to_excel(writer, 'AliExpress无忧物流-标准')


df_freeshipping_country.to_excel(writer, '包邮国家')

print(df_freeshipping_country)


writer.save()
writer.close()