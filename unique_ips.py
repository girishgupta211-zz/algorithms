# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

ip_set = set()
for entry in sys.stdin:
    line = entry.strip()
    # print(line)
    ip_contains = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
    if ip_contains is not None:
        ip = ip_contains.group()
        ip_set.add(ip)
        # print(ip)
print(len(ip_set))

# 2017/04/25 06:27:40.004692 INFO [Thread-23312] [Cache::getEntry] Probing cache for key=CME,180004846
# 2017/04/25 06:27:40.004693 INFO [Thread-23312] [Cache::getEntry] Cache now has num_entries=166, memory=5986 MBs
# 2017/04/25 06:27:40.005044 INFO [Thread-23312] [WebSocketHandler::operator()] RECORD username=hbatwani ip=10.26.130.119:0 view=Live min=1493116058159894 max=1493116059867766 key=CME,180004846 num_rows=285275 method=CACHE reply_size=40 cache_dt=0.000003 view_dt=0.000351
# 2017/04/25 06:27:40.008708 INFO [Thread-23316] [Cache::getEntry] Probing cache for key=CME,180004273
# 2017/04/25 06:27:40.008709 INFO [Thread-23316] [Cache::getEntry] Cache now has num_entries=166, memory=5986 MBs
# 2017/04/25 06:27:40.008781 INFO [Thread-23316] [WebSocketHandler::operator()] RECORD username=hbatwani ip=10.26.130.119:0 view=Live min=1493116059566625 max=1493116059869002 key=CME,180004273 num_rows=473734 method=CACHE reply_size=5 cache_dt=0.000003 view_dt=0.000071
# 2017/04/25 06:27:40.023492 INFO [Thread-23309] [Cache::getEntry] Probing cache for key=CME,135446600
# 2017/04/25 06:27:40.023493 INFO [Thread-23309] [Cache::getEntry] Cache now has num_entries=166, memory=5986 MBs
# 2017/04/25 06:27:40.023575 INFO [Thread-23309] [WebSocketHandler::operator()] RECORD username=sbrightman ip=10.26.130.39:0 view=Live min=1493116059009057 max=1493116059009057 key=CME,135446600 num_rows=223215 method=CACHE reply_size=5 cache_dt=0.000003 view_dt=0.000081
# 2017/04/25 06:27:40.042861 INFO [Thread-23303] [Cache::getEntry] Probing cache for key=CME,135215458
# 2017/04/25 06:27:40.042862 INFO [Thread-23303] [Cache::getEntry] Cache now has num_entries=166, memory=5986 MBs
# 2017/04/25 06:27:40.042941 INFO [Thread-23303] [WebSocketHandler::operator()] RECORD username=lyun ip=10.3.7.139:0 view=Live min=1493116059129166 max=1493116059129166 key=CME,135215458 num_rows=56902 method=CACHE reply_size=5 cache_dt=0.000003 view_dt=0.000079
# 2017/04/25 06:27:40.055705 INFO [Thread-23304] [Cache::getEntry] Probing cache for key=CME,135215458
# 2017/04/25 06:27:40.055706 INFO [Thread-23304] [Cache::getEntry] Cache now has num_entries=166, memory=5986 MBs
# 2017/04/25 06:27:40.055765 INFO [Thread-23304] [WebSocketHandler::operator()] RECORD username=lyun ip=10.3.7.139:0 view=Live min=1493116059129166 max=1493116059129166 key=CME,135215458 num_rows=56902 method=CACHE reply_size=5 cache_dt=0.000003 view_dt=0.000059
# 2017/04/25 06:27:40.083701 INFO [Thread-23305] [Cache::getEntry] Probing cache for key=CME,180004280
# 2017/04/25 06:27:40.083702 INFO [Thread-23305] [Cache::getEntry] Cache now has num_entries=166, memory=5986 MBs
# 2017/04/25 06:27:40.083753 INFO [Thread-23305] [WebSocketHandler::operator()] RECORD username=hbatwani ip=10.26.130.119:0 view=Live min=1493116059585601 max=1493116059836564 key=CME,180004280 num_rows=217640 method=CACHE reply_size=5 cache_dt=0.000004 view_dt=0.000050
