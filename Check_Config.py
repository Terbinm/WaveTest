import datetime
import logging
import os
import platform

from function.ConfigLoader import ConfigLoader


###############################################################
# 設定路徑(程式執行的路徑)
os.chdir("C:/Users/user/TestPycharm/WaveTest")
config_dir = 'config'  # 設定config目錄，會自動讀取全部檔案
edgeID = 'Soundtest_ModelA'  # 裝置編號 #不需設定，已廢棄
logging_name = 'CheckConfig.log'  # 裝置編號 #不需設定，已廢棄
###############################################################

# 紀錄執行的時間
with open(os.path.join('out', logging_name), 'w') as log_file:
    log_file.truncate()
logging.basicConfig(filename=os.path.join('out', logging_name), level=logging.DEBUG)  # log設定
logging.info('檢查開始時間: ' + str(datetime.datetime.now()))

# 讀取config
system_config_data = ConfigLoader(config_dir).config_dict

ERROR_COUNT = 0  # 錯誤次數


def check_out(check_value, identification, info_msg):
    global ERROR_COUNT
    if check_value == identification:
        print(info_msg + '-成功')
        logging.info(info_msg + '-成功')  # 系統與配置匹配時，記錄在log當中
    else:
        ERROR_COUNT += 1
        print(info_msg + '-失敗')
        logging.error(info_msg + '-失敗: ' + check_value + '與' + identification + '不匹配')  # 系統與配置匹配時，記錄在log當中


# System
print('-----檢察系統-----')
print('當前系統為：' + platform.system())
check_out(platform.system(), system_config_data['System']['os'], '系統與配置匹配')
print('-----檢察系統完畢-----\n')

print('-----檢察On Board參數-----')
if platform.system() == 'Windows':
    print('當前系統為：' + platform.system() + '，跳過該部分')
    logging.info('On Board 檢查跳過')  # 跳過檢查
elif platform.system() == 'Linux':
    # TODO: 檢查腳位功能
    print('當前系統為：' + platform.system() + '，檢查功能未開發')
    logging.info('On Board 檢查功能未開發')  # 跳過檢查
print('-----檢察On Board參數完畢-----\n')

print('-----檢察硬體是否匹配-----')
check_out(system_config_data['edge']['edge_type'], 'A', '裝置類別匹配')
check_out(system_config_data['edge']['code_name'], 'Tester', '硬體代號匹配')
# check_out(system_config_data['edge']['generation'],'gen1','硬體大版本匹配')

print('-----檢察執行程式是否匹配完畢-----\n')

print('-----檢察完畢-----')
if ERROR_COUNT == 0:
    print('通過檢查')
else:
    print('檢查失敗')
    print('共有: ' + str(ERROR_COUNT) + ' 筆錯誤')
print('更多細節請前往 '+os.path.join('out', logging_name)+' 檢查')

print('-----檢察完畢-----\n')
