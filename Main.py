import datetime
import logging
import os

from function.ConfigLoader import ConfigLoader  # config載入器

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

