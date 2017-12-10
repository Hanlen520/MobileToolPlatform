#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: v1.0
@author: jayzhen
@license: Apache Licence 
@email: jayzhen_testing@163.com
@software: PyCharm
@file: permission.py
@time: 2017/11/8 22:41

数据不全有待添加
"""

import sys
reload(sys)
sys.setdefaultencoding('utf8')

android_permissions = [
        {
            "Key": "android.permission.ACCESS_CHECKIN_PROPERTIES",
            "Title": "访问检入属性",
            "Memo": "允许对检入服务上传的属性进行读/写访问。普通应用程序不能使用此权限。",
            "Level": 0
        },
        {
            "Key": "android.permission.ACCESS_COARSE_LOCATION",
            "Title": "大概位置",
            "Memo": "访问大概的位置源(例如蜂窝网络数据库)以确定手机的大概位置(如果可以)。恶意应用程序可借此确定您所处的大概位置。",
            "Level": 1
        },
        {
            "Key": "android.permission.ACCESS_FINE_LOCATION",
            "Title": "精准的(GPS)位置",
            "Memo": "访问精准的位置源，例如手机上的全球定位系统(如果有)。恶意应用程序可能会借此确定您所处的位置，并可能消耗额外的电池电量。",
            "Level": 1
        },
        {
            "Key": "android.permission.ACCESS_LOCATION_EXTRA_COMMANDS",
            "Title": "访问额外的位置信息提供程序命令",
            "Memo": "访问额外的位置信息提供程序命令。恶意应用程序可借此干扰 GPS 或其他位置源的正常工作。",
            "Level": 1
        },
        {
            "Key": "android.permission.ACCESS_MOCK_LOCATION",
            "Title": "使用模拟地点来源进行测试",
            "Memo": "创建模拟地点来源进行测试。恶意应用程序可能利用此选项覆盖由真实地点来源（如 GPS 或网络提供商）传回的地点和/或状态。",
            "Level": 1
        },
        {
            "Key": "android.permission.ACCESS_NETWORK_STATE",
            "Title": "查看网络状态",
            "Memo": "允许应用程序查看所有网络的状态。",
            "Level": 0
        },
        {
            "Key": "android.permission.ACCESS_SURFACE_FLINGER",
            "Title": "访问 SurfaceFlinger",
            "Memo": "允许应用程序使用 SurfaceFlinger 低级别功能。",
            "Level": 0
        },
        {
            "Key": "android.permission.ACCESS_WIFI_STATE",
            "Title": "查看 WLAN 状态",
            "Memo": "允许应用程序查看有关 WLAN 状态的信息。",
            "Level": 0
        },
        {
            "Key": "android.permission.ADD_SYSTEM_SERVICE",
            "Title": "系统级服务",
            "Memo": "允许程序发布系统级服务",
            "Level": 0
        },
        {
            "Key": "android.permission.BATTERY_STATS",
            "Title": "修改电池统计信息",
            "Memo": "允许修改收集的电池使用情况统计信息。普通应用程序不能使用此权限。",
            "Level": 0
        },
        {
            "Key": "android.permission.BLUETOOTH",
            "Title": "创建蓝牙连接",
            "Memo": "允许应用程序查看本地蓝牙手机的配置，以及建立或接受与配对设备的连接。",
            "Level": 1
        },
        {
            "Key": "android.permission.BLUETOOTH_ADMIN",
            "Title": "蓝牙管理",
            "Memo": "允许应用程序配置本地蓝牙手机，以及发现远程设备并与其配对。",
            "Level": 0
        },
        {
            "Key": "android.permission.BRICK",
            "Title": "永久停用手机",
            "Memo": "允许应用程序永久停用整个手机，这非常危险。",
            "Level": 2
        },
        {
            "Key": "android.permission.BROADCAST_PACKAGE_REMOVED",
            "Title": "发送包删除的广播",
            "Memo": "允许应用程序广播已删除某应用程序包的通知。恶意应用程序可借此终止任何正在运行的其他应用程序。",
            "Level": 1
        },
        {
            "Key": "android.permission.BROADCAST_STICKY",
            "Title": "发送置顶广播",
            "Memo": "允许应用程序发送顽固广播，这些广播在结束后仍会保留。恶意应用程序可能会借此使手机耗用太多内存，从而降低其速度或稳定性。",
            "Level": 1
        },
        {
            "Key": "android.permission.CALL_PHONE",
            "Title": "直接拨打电话号码",
            "Memo": "允许应用程序在您不介入的情况下拨打电话。恶意应用程序可借此在您的话费单上产生意外通话费。请注意，此权限不允许应用程序拨打紧急呼救电话。",
            "Level": 2
        },
        {
            "Key": "android.permission.CALL_PRIVILEGED",
            "Title": "直接呼叫任何电话号码",
            "Memo": "允许应用程序在您不介入的情况下拨打任何电话（包括紧急呼救）。恶意应用程序可借此向应急服务机构拨打骚扰电话甚至非法电话。",
            "Level": 2
        },
        {
            "Key": "android.permission.CAMERA",
            "Title": "拍照",
            "Memo": "允许应用程序使用相机拍照，这样应用程序可随时收集进入相机镜头的图像。",
            "Level": 0
        },
        {
            "Key": "android.permission.CHANGE_COMPONENT_ENABLED_STATE",
            "Title": "启用或停用应用程序组件",
            "Memo": "允许应用程序更改是否启用其他应用程序的组件。恶意应用程序可借此停用重要的手机功能。使用此权限时务必谨慎，因为这可能导致应用程序组件进入不可用、不一致或不稳定的状态。",
            "Level": 1
        },
        {
            "Key": "android.permission.CHANGE_CONFIGURATION",
            "Title": "更改用户界面设置",
            "Memo": "允许应用程序更改当前配置，例如语言设置或整体的字体大小。",
            "Level": 0
        },
        {
            "Key": "android.permission.CHANGE_NETWORK_STATE",
            "Title": "更改网络连接性",
            "Memo": "允许应用程序更改网络连接的状态。",
            "Level": 0
        },
        {
            "Key": "android.permission.CHANGE_WIFI_STATE",
            "Title": "更改 WLAN 状态",
            "Memo": "允许应用程序连接到 WLAN 接入点以及与 WLAN 接入点断开连接，并对配置的 WLAN 网络进行更改。",
            "Level": 0
        },
        {
            "Key": "android.permission.CLEAR_APP_CACHE",
            "Title": "删除所有应用程序缓存数据",
            "Memo": "允许应用程序通过删除应用程序缓存目录中的文件释放手机存储空间。通常此权限只适用于系统进程。",
            "Level": 0
        },
        {
            "Key": "android.permission.CLEAR_APP_USER_DATA",
            "Title": "删除其他应用程序的数据",
            "Memo": "允许应用程序清除用户数据。",
            "Level": 1
        },
        {
            "Key": "android.permission.CONTROL_LOCATION_UPDATES",
            "Title": "控制位置更新通知",
            "Memo": "允许启用/停用来自收音机的位置更新通知。普通应用程序不能使用此权限。",
            "Level": 0
        },
        {
            "Key": "android.permission.DELETE_CACHE_FILES",
            "Title": "删除其他应用程序的缓存",
            "Memo": "允许应用程序删除缓存文件。",
            "Level": 0
        },
        {
            "Key": "android.permission.DELETE_PACKAGES",
            "Title": "删除应用程序",
            "Memo": "允许应用程序删除 Android 包。恶意应用程序可借此删除重要的应用程序。",
            "Level": 0
        },
        {
            "Key": "android.permission.DEVICE_POWER",
            "Title": "开机或关机",
            "Memo": "允许应用程序打开或关闭手机。",
            "Level": 0
        },
        {
            "Key": "android.permission.DIAGNOSTIC",
            "Title": "读取/写入诊断所拥有的资源",
            "Memo": "允许应用程序读取/写入诊断组所拥有的任何资源（例如，/dev 中的文件）。这可能会影响系统稳定性和安全性。此权限仅供制造商或运营商诊断硬件问题。",
            "Level": 2
        },
        {
            "Key": "android.permission.DISABLE_KEYGUARD",
            "Title": "停用键锁",
            "Memo": "允许应用程序停用键锁和任何关联的密码安全设置。例如，在手机上接听电话时停用键锁，在通话结束后重新启用键锁。",
            "Level": 0
        },
        {
            "Key": "android.permission.DUMP",
            "Title": "检索系统内部状态",
            "Memo": "允许应用程序检索系统的内部状态。恶意应用程序可借此检索它们本不需要的各种保密信息和安全信息。",
            "Level": 0
        },
        {
            "Key": "android.permission.EXPAND_STATUS_BAR",
            "Title": "展开/收拢状态栏",
            "Memo": "允许应用程序展开或收拢状态栏。",
            "Level": 0
        },
        {
            "Key": "android.permission.FACTORY_TEST",
            "Title": "在出厂测试模式下运行",
            "Memo": "作为一项低级制造商测试来运行，从而允许对手机硬件进行完全访问。此权限仅当手机在制造商测试模式下运行时才可用。",
            "Level": 0
        },
        {
            "Key": "android.permission.FLASHLIGHT",
            "Title": "控制闪光灯",
            "Memo": "允许应用程序控制闪光灯。",
            "Level": 0
        },
        {
            "Key": "android.permission.FORCE_BACK",
            "Title": "强制应用程序关闭",
            "Memo": "允许应用程序强制前端的任何活动关闭并重新开始。普通应用程序从不需要使用此权限。",
            "Level": 0
        },
        {
            "Key": "android.permission.FOTA_UPDATE",
            "Title": "系统升级",
            "Memo": "运行应用程序使用空中升级系统",
            "Level": 0
        },
        {
            "Key": "android.permission.GET_ACCOUNTS",
            "Title": "发现已知帐户",
            "Memo": "允许应用程序获取手机已知的帐户列表。",
            "Level": 0
        },
        {
            "Key": "android.permission.GET_PACKAGE_SIZE",
            "Title": "计算应用程序存储空间",
            "Memo": "允许应用程序检索其代码、数据和缓存大小",
            "Level": 0
        },
        {
            "Key": "android.permission.GET_TASKS",
            "Title": "检索当前运行的应用程序",
            "Memo": "允许应用程序检索有关当前和最近运行的任务的信息。恶意应用程序可借此发现有关其他应用程序的保密信息。",
            "Level": 1
        },
        {
            "Key": "android.permission.HARDWARE_TEST",
            "Title": "测试硬件",
            "Memo": "允许应用程序控制各外围设备以进行硬件测试。",
            "Level": 0
        },
        {
            "Key": "android.permission.INJECT_EVENTS",
            "Title": "按键和控制按钮",
            "Memo": "允许应用程序将其自己的输入活动（按键等）提供给其他应用程序。恶意应用程序可借此掌控手机。",
            "Level": 2
        },
        {
            "Key": "android.permission.INSTALL_PACKAGES",
            "Title": "直接安装应用程序",
            "Memo": "允许应用程序安装全新的或更新的 Android 包。恶意应用程序可能会借此添加其具有任意权限的新应用程序。",
            "Level": 1
        },
        {
            "Key": "android.permission.INTERNAL_SYSTEM_WINDOW",
            "Title": "显示未授权的窗口",
            "Memo": "允许创建专用于内部系统用户界面的窗口。普通应用程序不能使用此权限。",
            "Level": 0
        },
        {
            "Key": "android.permission.INTERNET",
            "Title": "访问网络",
            "Memo": "允许程序访问网络.",
            "Level": 0
        },
        {
            "Key": "android.permission.MANAGE_APP_TOKENS",
            "Title": "管理应用程序令牌",
            "Memo": "允许应用程序创建和管理自己的令牌，从而绕开其常规的 Z 方向。普通应用程序从不需要使用此权限。",
            "Level": 0
        },
        {
            "Key": "android.permission.MASTER_CLEAR",
            "Title": "恢复出厂设置",
            "Memo": "允许应用程序将系统恢复为出厂设置，即清除所有数据、配置以及所安装的应用程序。",
            "Level": 2
        },
        {
            "Key": "android.permission.MODIFY_AUDIO_SETTINGS",
            "Title": "更改您的音频设置",
            "Memo": "允许应用程序修改整个系统的音频设置，如音量和路由。",
            "Level": 0
        },
        {
            "Key": "android.permission.MODIFY_PHONE_STATE",
            "Title": "修改手机状态",
            "Memo": "允许应用程序控制设备的电话功能。拥有此权限的应用程序可自行切换网络、打开和关闭无线通信等，而不会通知您。",
            "Level": 1
        },
        {
            "Key": "android.permission.MOUNT_UNMOUNT_FILESYSTEMS",
            "Title": "装载和卸载文件系统",
            "Memo": "允许应用程序装载和卸载可移动存储器的文件系统。",
            "Level": 0
        },
        {
            "Key": "android.permission.PERSISTENT_ACTIVITY",
            "Title": "让应用程序始终运行",
            "Memo": "允许应用程序部分持续运行，这样系统便不能将其用于其他应用程序。",
            "Level": 0
        },
        {
            "Key": "android.permission.PROCESS_OUTGOING_CALLS",
            "Title": "拦截外拨电话",
            "Memo": "允许应用程序处理外拨电话或更改要拨打的号码。恶意应用程序可能会借此监视、另行转接甚至阻止外拨电话。",
            "Level": 2
        },
        {
            "Key": "android.permission.READ_CALENDAR",
            "Title": "读取日历活动",
            "Memo": "允许应用程序读取您手机上存储的所有日历活动。恶意应用程序可借此将您的日历活动发送给其他人。",
            "Level": 1
        },
        {
            "Key": "android.permission.READ_CONTACTS",
            "Title": "读取联系人数据",
            "Memo": "允许应用程序读取您手机上存储的所有联系人（地址）数据。恶意应用程序可借此将您的数据发送给其他人。",
            "Level": 1
        },
        {
            "Key": "android.permission.READ_FRAME_BUFFER",
            "Title": "读取帧缓冲区",
            "Memo": "允许应用程序读取帧缓冲区中的内容,比如抓屏程序.",
            "Level": 0
        },
        {
            "Key": "android.permission.READ_INPUT_STATE",
            "Title": "记录您键入的内容和执行的操作",
            "Memo": "允许应用程序查看您按的键，即使在与其他应用程序交互（例如输入密码）时也不例外。普通应用程序从不需要使用此权限。",
            "Level": 2
        },
        {
            "Key": "android.permission.READ_LOGS",
            "Title": "读取系统日志文件",
            "Memo": "允许应用程序从系统的各日志文件中读取信息。这样应用程序可以发现您的手机使用情况，但这些信息不应包含任何个人信息或保密信息。",
            "Level": 0
        },
        {
            "Key": "android.permission.READ_OWNER_DATA",
            "Title": "读取所有者数据",
            "Memo": "允许应用程序读取您手机上存储的手机所有者数据。恶意应用程序可借此读取手机所有者数据。",
            "Level": 1
        },
        {
            "Key": "android.permission.READ_SMS",
            "Title": "读取短信或彩信",
            "Memo": "允许应用程序读取您的手机或 SIM 卡中存储的短信。恶意应用程序可借此读取您的机密信息。",
            "Level": 2
        },
        {
            "Key": "android.permission.READ_SYNC_SETTINGS",
            "Title": "读取同步设置",
            "Memo": "允许应用程序读取同步设置，例如是否为（联系人）启用同步。",
            "Level": 0
        },
        {
            "Key": "android.permission.READ_SYNC_STATS",
            "Title": "读取同步统计信息",
            "Memo": "允许应用程序读取同步统计信息；例如已发生的同步历史记录。",
            "Level": 0
        },
        {
            "Key": "android.permission.REBOOT",
            "Title": "强行重新启动手机",
            "Memo": "允许应用程序强行重新启动手机。",
            "Level": 1
        },
        {
            "Key": "android.permission.RECEIVE_BOOT_COMPLETED",
            "Title": "开机时自动启动",
            "Memo": "允许应用程序在系统完成启动后即自行启动。这样会延长手机的启动时间，而且如果应用程序一直运行，会降低手机的整体速度。",
            "Level": 1
        },
        {
            "Key": "android.permission.RECEIVE_MMS",
            "Title": "接收彩信",
            "Memo": "允许应用程序接收和处理彩信。恶意应用程序可借此监视您的信息，或者将信息删除而不向您显示。",
            "Level": 1
        },
        {
            "Key": "android.permission.RECEIVE_SMS",
            "Title": "接收短信",
            "Memo": "允许应用程序接收和处理短信。恶意应用程序可借此监视您的信息，或者将信息删除而不向您显示。",
            "Level": 1
        },
        {
            "Key": "android.permission.RECEIVE_WAP_PUSH",
            "Title": "接收 WAP",
            "Memo": "允许应用程序接收和处理 WAP 信息。恶意应用程序可借此监视您的信息，或者将信息删除而不向您显示。",
            "Level": 1
        },
        {
            "Key": "android.permission.RECORD_AUDIO",
            "Title": "录音",
            "Memo": "允许应用程序访问录音路径。",
            "Level": 1
        },
        {
            "Key": "android.permission.REORDER_TASKS",
            "Title": "对正在运行的应用程序重新排序",
            "Memo": "允许应用程序将任务移至前端和后台。恶意应用程序可借此强行进入前端，而不受您的控制。",
            "Level": 1
        },
        {
            "Key": "android.permission.RESTART_PACKAGES",
            "Title": "重启程序",
            "Memo": "允许程序自己重启或重启其他程序",
            "Level": 0
        },
        {
            "Key": "android.permission.SEND_SMS",
            "Title": "发送短信",
            "Memo": "允许应用程序发送短信。恶意应用程序可能会不经您的确认就发送信息，给您带来费用。",
            "Level": 2
        },
        {
            "Key": "android.permission.SET_ACTIVITY_WATCHER",
            "Title": "监控所有应用程序的启动",
            "Memo": "允许应用程序监控系统启动活动的方式。恶意应用程序可借此彻底损坏系统。此权限仅在开发时才需要，普通的手机应用不需要。",
            "Level": 1
        },
        {
            "Key": "android.permission.SET_ALWAYS_FINISH",
            "Title": "关闭所有后台应用程序",
            "Memo": "允许应用程序控制活动是否始终是一转至后台就完成。普通应用程序从不需要使用此权限。",
            "Level": 0
        },
        {
            "Key": "android.permission.SET_ANIMATION_SCALE",
            "Title": "修改全局动画速度",
            "Memo": "允许应用程序随时更改全局动画速度（加快或放慢动画）。",
            "Level": 0
        },
        {
            "Key": "android.permission.SET_DEBUG_APP",
            "Title": "启用应用程序调试",
            "Memo": "允许应用程序启动对其他应用程序的调试。恶意应用程序可借此终止其他应用程序。",
            "Level": 1
        },
        {
            "Key": "android.permission.SET_ORIENTATION",
            "Title": "更改屏幕显示方向",
            "Memo": "允许应用程序随时更改屏幕的旋转方向。普通应用程序从不需要使用此权限。",
            "Level": 0
        },
        {
            "Key": "android.permission.SET_PREFERRED_APPLICATIONS",
            "Title": "设置首选应用程序",
            "Memo": "允许应用程序修改首选的应用程序。这样恶意应用程序可能会暗中更改运行的应用程序，从而骗过您的现有应用程序来收集您的保密数据。",
            "Level": 1
        },
        {
            "Key": "android.permission.SET_PROCESS_FOREGROUND",
            "Title": "强制前台运行",
            "Memo": "允许程序强制前台运行",
            "Level": 0
        },
        {
            "Key": "android.permission.SET_PROCESS_LIMIT",
            "Title": "限制运行的进程个数",
            "Memo": "允许应用程序控制将运行的进程数上限。普通应用程序从不需要使用此权限。",
            "Level": 0
        },
        {
            "Key": "android.permission.SET_TIME_ZONE",
            "Title": "设置时区",
            "Memo": "允许应用程序更改手机的时区。",
            "Level": 0
        },
        {
            "Key": "android.permission.SET_WALLPAPER",
            "Title": "设置壁纸",
            "Memo": "允许应用程序设置系统壁纸。",
            "Level": 0
        },
        {
            "Key": "android.permission.SET_WALLPAPER_HINTS",
            "Title": "设置壁纸大小提示",
            "Memo": "允许应用程序设置有关壁纸大小的提示。",
            "Level": 0
        },
        {
            "Key": "android.permission.SIGNAL_PERSISTENT_PROCESSES",
            "Title": "向应用程序发送 Linux 信号",
            "Memo": "允许应用程序请求将所提供的信号发送给所有持久进程。",
            "Level": 0
        },
        {
            "Key": "android.permission.STATUS_BAR",
            "Title": "停用或修改状态栏",
            "Memo": "允许应用程序停用状态栏或者增删系统图标。",
            "Level": 0
        },
        {
            "Key": "android.permission.SUBSCRIBED_FEEDS_READ",
            "Title": "读取订阅的供稿",
            "Memo": "允许应用程序获取有关当前同步的供稿的详细信息。",
            "Level": 0
        },
        {
            "Key": "android.permission.SUBSCRIBED_FEEDS_WRITE",
            "Title": "写入订阅的供稿",
            "Memo": "允许应用程序修改您当前同步的供稿。恶意应用程序可借此更改您同步的供稿。",
            "Level": 1
        },
        {
            "Key": "android.permission.SYSTEM_ALERT_WINDOW",
            "Title": "显示系统级警报",
            "Memo": "允许应用程序显示系统警报窗口。恶意应用程序可借此掌控整个手机屏幕。",
            "Level": 1
        },
        {
            "Key": "android.permission.VIBRATE",
            "Title": "控制振动器",
            "Memo": "允许应用程序控制振动器。",
            "Level": 0
        },
        {
            "Key": "android.permission.WAKE_LOCK",
            "Title": "防止手机休眠",
            "Memo": "允许应用程序防止手机进入休眠状态。",
            "Level": 0
        },
        {
            "Key": "android.permission.WRITE_APN_SETTINGS",
            "Title": "写入（接入点名称）设置",
            "Memo": "允许应用程序修改 APN 设置，例如任何 APN 的代理和端口。",
            "Level": 0
        },
        {
            "Key": "android.permission.WRITE_CALENDAR",
            "Title": "添加或修改日历活动以及向邀请对象发送电子邮件",
            "Memo": "允许应用程序添加或更改日历中的活动，这可能会向邀请对象发送电子邮件。恶意应用程序可能会借此清除或修改您的日历活动，或者向邀请对象发送电子邮件。",
            "Level": 1
        },
        {
            "Key": "android.permission.WRITE_CONTACTS",
            "Title": "写入联系数据",
            "Memo": "允许应用程序修改您手机上存储的联系人（地址）数据。恶意应用程序可借此清除或修改您的联系人数据。",
            "Level": 1
        },
        {
            "Key": "android.permission.WRITE_GSERVICES",
            "Title": "修改 Google 地图",
            "Memo": "允许应用程序修改 Google 服务地图。普通应用程序不能使用此权限。",
            "Level": 0
        },
        {
            "Key": "android.permission.WRITE_OWNER_DATA",
            "Title": "写入所有者数据",
            "Memo": "允许应用程序修改您手机上存储的手机所有者数据。恶意应用程序可借此清除或修改所有者数据。",
            "Level": 1
        },
        {
            "Key": "android.permission.WRITE_SETTINGS",
            "Title": "修改全局系统设置",
            "Memo": "允许应用程序修改系统设置方面的数据。恶意应用程序可借此破坏您的系统配置。",
            "Level": 1
        },
        {
            "Key": "android.permission.WRITE_SMS",
            "Title": "编辑短信或彩信",
            "Memo": "允许应用程序写入手机或 SIM 卡中存储的短信。恶意应用程序可借此删除您的信息。",
            "Level": 1
        },
        {
            "Key": "android.permission.WRITE_SYNC_SETTINGS",
            "Title": "写入同步设置",
            "Memo": "允许应用程序修改同步设置，例如是否为（联系人）启用同步。",
            "Level": 1
        },
        {
            "Key": "android.permission.ACCESS_CACHE_FILESYSTEM",
            "Title": "访问缓存文件系统",
            "Memo": "允许应用程序读取和写入缓存文件系统。",
            "Level": 0
        },
        {
            "Key": "android.permission.ACCOUNT_MANAGER",
            "Title": "作为帐户身份验证程序",
            "Memo": "允许应用程序使用 AccountManager 的帐户身份验证程序功能，包括创建帐户以及获取和设置其密码。",
            "Level": 0
        },
        {
            "Key": "android.permission.ASEC_ACCESS",
            "Title": "获取有关安全存储的信息",
            "Memo": "允许应用程序获取有关安全存储的信息。",
            "Level": 0
        },
        {
            "Key": "android.permission.ASEC_CREATE",
            "Title": "创建安全存储",
            "Memo": "允许应用程序创建安全存储。",
            "Level": 0
        },
        {
            "Key": "android.permission.ASEC_DESTROY",
            "Title": "清除安全存储",
            "Memo": "允许应用程序清除安全存储。",
            "Level": 0
        },
        {
            "Key": "android.permission.ASEC_MOUNT_UNMOUNT",
            "Title": "安装/卸载安全存储",
            "Memo": "允许应用程序安装/卸载安全存储。",
            "Level": 0
        },
        {
            "Key": "android.permission.ASEC_RENAME",
            "Title": "重命名安全存储",
            "Memo": "允许应用程序重命名安全存储。",
            "Level": 0
        },
        {
            "Key": "android.permission.AUTHENTICATE_ACCOUNTS",
            "Title": "作为帐户身份验证程序",
            "Memo": "允许应用程序使用 AccountManager 的帐户身份验证程序功能，包括创建帐户以及获取和设置其密码。",
            "Level": 0
        },
        {
            "Key": "android.permission.BACKUP",
            "Title": "控制系统备份和还原",
            "Memo": "允许应用程序控制系统的备份和还原机制。普通应用程序不能使用此权限。",
            "Level": 0
        },
        {
            "Key": "android.permission.BIND_APPWIDGET",
            "Title": "选择窗口小部件",
            "Memo": "允许应用程序告诉系统哪个应用程序可以使用哪些窗口小部件。具有该权限的应用程序可以允许其他应用程序访问个人数据。普通应用程序不能使用此权限。",
            "Level": 0
        },
        {
            "Key": "android.permission.BIND_DEVICE_ADMIN",
            "Title": "与设备管理器交互",
            "Memo": "允许持有对象将意向发送到设备管理器。普通的应用程序一律无需此权限。",
            "Level": 0
        },
        {
            "Key": "android.permission.BIND_INPUT_METHOD",
            "Title": "绑定至输入法",
            "Memo": "允许手机用户绑定至输入法的顶级界面。普通应用程序从不需要使用此权限。",
            "Level": 0
        },
        {
            "Key": "android.permission.BIND_WALLPAPER",
            "Title": "绑定到壁纸",
            "Memo": "允许手机用户绑定到壁纸的顶级界面。应该从不需要将此权限授予普通应用程序。",
            "Level": 0
        },
        {
            "Key": "android.permission.BROADCAST_SMS",
            "Title": "发送短信收到的广播",
            "Memo": "允许应用程序广播已收到短信的通知。恶意应用程序可借此伪造收到的短信。",
            "Level": 1
        },
        {
            "Key": "android.intent.category.MASTER_CLEAR.permission.C2D_MESSAGE",
            "Title": "C2DM权限(云端)",
            "Memo": "C2DM允许第三方开发者开发相关的应用来推送少量数据消息到用户的手机上。",
            "Level": 1
        },
        {
            "Key": "android.permission.CHANGE_BACKGROUND_DATA_SETTING",
            "Title": "更改背景数据使用设置",
            "Memo": "允许应用程序更改背景数据使用设置。",
            "Level": 0
        },
        {
            "Key": "android.permission.CHANGE_WIFI_MULTICAST_STATE",
            "Title": "允许接收WLAN多播",
            "Memo": "允许应用程序接收并非直接向您的设备发送的数据包。这样在查找附近提供的服务时很有用。这种操作所耗电量大于非多播模式。",
            "Level": 1
        },
        {
            "Key": "android.permission.COPY_PROTECTED_DATA",
            "Title": "复制保护数据",
            "Memo": "允许调用默认的容器服务复制内容。不适用于普通应用程序使用。",
            "Level": 1
        },
        {
            "Key": "android.permission.FORCE_STOP_PACKAGES",
            "Title": "强行停止其他应用程序",
            "Memo": "允许应用程序强行停止其他应用程序。",
            "Level": 0
        },
        {
            "Key": "android.permission.GLOBAL_SEARCH",
            "Title": "全局搜索",
            "Memo": "允许应用程序使用全局搜索。",
            "Level": 0
        },
        {
            "Key": "android.permission.GLOBAL_SEARCH_CONTROL",
            "Title": "全局搜索控制",
            "Memo": "允许应用程序控制全局搜索。",
            "Level": 0
        },
        {
            "Key": "android.permission.INSTALL_LOCATION_PROVIDER",
            "Title": "允许安装位置信息提供程序",
            "Memo": "创建模拟地点来源进行测试。恶意应用程序可能利用此选项覆盖由真实地点来源（如 GPS 或网络提供商）所传回的地点和/或状态，或者监视您的位置并将其提供给外部来源。",
            "Level": 1
        },
        {
            "Key": "android.permission.KILL_BACKGROUND_PROCESSES",
            "Title": "结束后台进程",
            "Memo": "无论内存资源是否紧张，都允许应用程序结束其他应用程序的后台进程。",
            "Level": 0
        },
        {
            "Key": "android.permission.LEDS",
            "Title": "控制键盘灯",
            "Memo": "允许应用程序控制键盘灯。",
            "Level": 0
        },
        {
            "Key": "android.permission.MANAGE_ACCOUNTS",
            "Title": "管理帐户列表",
            "Memo": "允许应用程序执行添加、删除帐户及删除其密码之类的操作。",
            "Level": 0
        },
        {
            "Key": "android.permission.MEIZU_SYS_PHONE_FUNC",
            "Title": "魅族手机系统程序",
            "Memo": "魅族手机系统程序。不做解释.",
            "Level": 0
        },
        {
            "Key": "android.permission.MOUNT_FORMAT_FILESYSTEMS",
            "Title": "格式化外部存储设备",
            "Memo": "允许应用程序格式化可移除的存储设备。",
            "Level": 2
        },
        {
            "Key": "android.permission.MOVE_PACKAGE",
            "Title": "移动应用程序资源",
            "Memo": "允许应用程序在内部介质和外部介质之间移动应用程序资源。",
            "Level": 0
        },
        {
            "Key": "android.permission.PACKAGE_USAGE_STATS",
            "Title": "更新组件使用统计",
            "Memo": "允许使用统计资料的收集组件修改。普通应用程序不适合使用。",
            "Level": 0
        },
        {
            "Key": "android.permission.PERFORM_CDMA_PROVISIONING",
            "Title": "直接启动CDMA电话设置",
            "Memo": "允许应用程序启动 CDMA 服务。恶意应用程序可能会无端启动 CDMA 服务",
            "Level": 1
        },
        {
            "Key": "android.permission.READ_CONTACTS_SUPER",
            "Title": "读取联系人",
            "Memo": "允许应用程序读取联系人数据(超级权限).",
            "Level": 2
        },
        {
            "Key": "android.permission.READ_HISTORY_BOOKMARKS",
            "Title": "读取历史记录",
            "Memo": "允许应用程序读取浏览器历史记录.",
            "Level": 1
        },
        {
            "Key": "android.permission.READ_PHONE_STATE",
            "Title": "读取手机状态和身份",
            "Memo": "允许应用程序访问设备的手机功能。有此权限的应用程序可确定此手机的号码和序列号，是否正在通话，以及对方的号码等。",
            "Level": 1
        },
        {
            "Key": "android.permission.READ_USER_DICTIONARY",
            "Title": "读取用户定义的词典",
            "Memo": "允许应用程序读取用户在用户词典中存储的任意私有字词、名称和短语。",
            "Level": 0
        },
        {
            "Key": "android.permission.SET_TIME",
            "Title": "设置时间",
            "Memo": "允许应用程序更改手机的时间。",
            "Level": 0
        },
        {
            "Key": "android.permission.SET_WALLPAPER_COMPONENT",
            "Title": "设置壁纸组件",
            "Memo": "允许应用程序设置壁纸组件。",
            "Level": 0
        },
        {
            "Key": "android.permission.SHUTDOWN",
            "Title": "部分关机",
            "Memo": "使活动管理器进入关闭状态。不执行彻底关机。",
            "Level": 0
        },
        {
            "Key": "android.permission.STOP_APP_SWITCHES",
            "Title": "禁止切换应用程序",
            "Memo": "禁止用户切换到另一应用程序。",
            "Level": 0
        },
        {
            "Key": "android.permission.UPDATE_DEVICE_STATS",
            "Title": "更新设备状态",
            "Memo": "允许应用程序更新设备状态。",
            "Level": 0
        },
        {
            "Key": "android.permission.USE_CREDENTIALS",
            "Title": "使用帐户的身份验证凭据",
            "Memo": "允许应用程序请求身份验证标记。",
            "Level": 0
        },
        {
            "Key": "android.permission.WRITE_CONTACTS_SUPER",
            "Title": "写入联系人数据",
            "Memo": "允许应用程序写入联系人数据(超级权限)。",
            "Level": 0
        },
        {
            "Key": "android.permission.WRITE_EXTERNAL_STORAGE",
            "Title": "修改/删除SD卡中的内容",
            "Memo": "允许应用程序写入SD卡。",
            "Level": 0
        },
        {
            "Key": "com.android.browser.permission.WRITE_HISTORY_BOOKMARKS",
            "Title": "写入浏览器历史和书签记录",
            "Memo": "允许应用程序写入浏览器历史和书签记录。",
            "Level": 0
        },
        {
            "Key": "android.permission.WRITE_SECURE_SETTINGS",
            "Title": "修改安全系统设置",
            "Memo": "允许应用程序修改系统的安全设置数据。普通应用程序不能使用此权限。",
            "Level": 1
        },
        {
            "Key": "android.permission.WRITE_USER_DICTIONARY",
            "Title": "写入用户定义的词典",
            "Memo": "允许应用程序向用户词典中写入新词。",
            "Level": 1
        }
    ]