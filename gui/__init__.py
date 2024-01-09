from nicegui import ui
import os
from gui.pages.Setting_cafe import set_cafe
from gui.pages.Setting_emulator import set_emulator
from gui.pages.Setting_event import set_event
from gui.pages.Setting_exchange import set_exchange
from gui.pages.Setting_hard import set_hard
from gui.pages.Setting_normal import set_normal
from gui.pages.Setting_other import set_other
from gui.pages.Setting_server import set_server
from gui.pages.Setting_shop import set_shop
from gui.pages.Setting_special import set_special
from gui.pages.Setting_task_order import set_task_order
from gui.pages.Setting_timetable import set_timetable
from gui.pages.Setting_wanted import set_wanted

@ui.refreshable
def show_GUI(load_jsonname, config):
        
    config.parse_user_config(load_jsonname)
    
    with ui.row():
        ui.label("Blue Archive Aris Helper").style('font-size: xx-large')
    
    ui.label(config.get_text("BAAH_desc"))

    ui.label(config.get_text("BAAH_get_version"))
    
    ui.label(config.get_text("BAAH_attention")).style('color: red; font-size: x-large')

    # myAllTask里面的key与GUI显示的key的映射
    real_taskname_to_show_taskname = {
        "登录游戏":config.get_text("task_login_game"),
        "清momotalk":config.get_text("task_clear_momotalk"),
        "咖啡馆":config.get_text("task_cafe"),
        "咖啡馆只摸头":config.get_text("task_cafe_only_touch"),
        "课程表":config.get_text("task_timetable"),
        "社团":config.get_text("task_club"),
        "商店":config.get_text("task_shop"),
        "悬赏通缉":config.get_text("task_wanted"),
        "特殊任务":config.get_text("task_special"),
        "学园交流会":config.get_text("task_exchange"),
        "战术大赛":config.get_text("task_contest"),
        "困难关卡":config.get_text("task_hard"),
        "活动关卡":config.get_text("task_event"),
        "每日任务":config.get_text("task_daily"),
        "邮件":config.get_text("task_mail"),
        "普通关卡":config.get_text("task_normal"),
    }

    # =============================================

    # =============================================

    with ui.row().style('min-width: 800px; display: flex; flex-direction: row;flex-wrap: nowrap;'):
        with ui.column().style('width: 200px; overflow: auto;flex-grow: 1;position: sticky; top: 20px;'):
            with ui.card():
                ui.link(config.get_text("setting_emulator"), '#EMULATOR')
                ui.link(config.get_text("setting_server"), '#SERVER')
                ui.link(config.get_text("setting_task_order"), '#TASK_ORDER')
                ui.link(config.get_text("setting_next_config"), '#NEXT_CONFIG')
                ui.link(config.get_text("task_cafe"), '#CAFE')
                ui.link(config.get_text("task_timetable"), '#TIME_TABLE')
                ui.link(config.get_text("task_shop"), '#SHOP_NORMAL')
                ui.link(config.get_text("task_wanted"), '#WANTED')
                ui.link(config.get_text("task_special"), '#SPECIAL_TASK')
                ui.link(config.get_text("task_exchange"), '#EXCHANGE')
                ui.link(config.get_text("task_event"), '#ACTIVITY')
                ui.link(config.get_text("task_hard"), '#HARD')
                ui.link(config.get_text("task_normal"), '#NORMAL')
                ui.link(config.get_text("setting_other"), '#TOOL_PATH')


        with ui.column().style('flex-grow: 4;'):
            # 模拟器配置
            set_emulator(config)
            
            # 服务器配置
            set_server(config)
            
            # 任务执行顺序，后续配置文件
            set_task_order(config, real_taskname_to_show_taskname)
            
            # 咖啡馆
            set_cafe(config)
            
            # 课程表
            set_timetable(config)
                
            # 商店
            set_shop(config)
            
            # 悬赏通缉
            set_wanted(config)
            
            # 特殊任务
            set_special(config)
            
            # 学园交流会
            set_exchange(config)

            # 活动关卡
            set_event(config)
                
            # 困难关卡
            set_hard(config)
            
            # 普通关卡
            set_normal(config)
            
            # 其他设置
            set_other(config)
            
        with ui.column().style('width: 10vw; overflow: auto; position: fixed; bottom: 40px; right: 20px;min-width: 150px;'):
            def save_and_alert():
                config.save_user_config(load_jsonname)
                ui.notify(config.get_text("notice_save_success"))
            ui.button(config.get_text("button_save"), on_click=save_and_alert)

            def save_and_alert_and_run():
                config.save_user_config(load_jsonname)
                ui.notify(config.get_text("notice_save_success"))
                ui.notify(config.get_text("notice_start_run"))
                # 打开同目录中的BAAH.exe，传入当前config的json文件名
                os.system(f"start BAAH{config.NOWVERSION}.exe {load_jsonname}")
            ui.button(config.get_text("button_save_and_run"), on_click=save_and_alert_and_run)
        
    # 加载完毕保存一下config，让新建的config文件有默认值
    config.save_user_config(load_jsonname)