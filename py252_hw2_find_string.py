# -*- coding: utf8 -*-

# 在特定的文章字串中，搜尋輸入的字串
# 條件1: 若有符合的字串，將其索引值印出 (全部印出，
# 並非印出第一個符合的索引值)
#  條件2: 最後印出 總共有9個"的", (若輸入的字為"的")

text='在 Google I/O 2013 開發者大會上，除了 Samsung GALAXY S 4 的 Google 版本外，並未發表任何新產品；但許多消費者一定很期待，包括 Nexus 4、Nexus 7、Nexus 10 的後繼機種的消息。眼尖的網友或許會發現，在 Google I/O 2013 的介紹影片中，與 Nexus 4、Nexus 10 並列的官方圖片，中間那款並不是 Nexus 7，機身頂部與底部都是彎曲設計，極有可能是 Nexus 7 的後繼機種。不過，根據 VR-Zone 獲得的資訊顯示，次世代 Nexus 7 還是由 ASUS 代工，除了螢幕為 1920 x 1080 解析度 IPS 面板外，可能還會選擇 Qualcomm Snapdragon 800 四核心處理器，至於 NVIDIA Tegra 4 則因成本考量而被摒棄，這或許是二代 Nexus 7 至今還無法釋出的原因之一。'

findstr = input("請輸入要搜尋的字:")

index = 0
sum = 0
while True:
		index = text.find(findstr, index+1)
		if index == -1:
			break
		sum = sum + 1
		print (index)

print ('總共有 %d 個 %s' %(sum, findstr))
