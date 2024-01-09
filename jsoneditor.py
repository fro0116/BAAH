if __name__ in {"__main__", "__mp_main__"}:
    try:
        import os
        import requests
        import sys
        from modules.configs.MyConfig import MyConfigger, config
        # 是否以网页形式运行
        isweb=False
        if len(sys.argv) > 1:
            isweb = sys.argv[1] == "web"
        # 获取到user config文件夹下以json为后缀的文件
        def get_json_list():
            return [i for i in os.listdir(MyConfigger.USER_CONFIG_FOLDER) if i.endswith(".json")]

        # 如果没有config.json文件，则创建一个
        if not os.path.exists(os.path.join(MyConfigger.USER_CONFIG_FOLDER, "config.json")):
            with open(os.path.join(MyConfigger.USER_CONFIG_FOLDER, "config.json"), "w") as f:
                f.write("{}")
        # 维护当前正在看的json文件名字
        now_json_name = {"name":"config.json"}

        from gui import show_GUI
        from nicegui import native, ui, run

        # 检查更新
        async def check_newest_version():
            try:
                r = await run.io_bound(requests.get, "https://api.github.com/repos/sanmusen214/BAAH/releases/latest", timeout=10)
                if r.status_code == 200:
                    data = r.json()
                    ui.notify(f'{config.get_text("notice_get_new_version")}: {data["tag_name"]}')
                else:
                    ui.notify(config.get_text("notice_fail"))
            except:
                ui.notify(config.get_text("notice_fail"))
        
        @ui.refreshable
        def draw_upper_right_selectlist(jsonfile_list):
            """
            更新右上角的选择列表，并自动保存当前config文件
            当选择列表发生变化时，会自动调用show_GUI.refresh()函数
            """
            with ui.column().style('width: 10vw; overflow: auto; position: fixed; top: 20px; right: 20px;min-width: 150px;'):
                # now_json_name主要是初始值有用
                # 不在select里设置value，只有后面的bind_value的话，渲染时会触发一次on_change事件
                ui.select(jsonfile_list, value=now_json_name["name"], on_change=lambda:show_GUI.refresh(now_json_name['name'], config)).bind_value(now_json_name, 'name')
                ui.button(config.get_text("button_check_version"), on_click=check_newest_version)
        
        show_GUI("config.json", config)
        alljson_list = get_json_list()
        draw_upper_right_selectlist(alljson_list)
        # 对每个get_json_list()里的文件，show_GUI一下
        for i in range(len(alljson_list)):
            show_GUI.refresh(alljson_list[i], config)
        # 回到config.json
        show_GUI.refresh("config.json", config)
        
        ui.timer(30.0, lambda: draw_upper_right_selectlist.refresh(get_json_list()))
        if not isweb:
            try:
                ui.run(native=True, window_size=(1280,720), title=f"Blue Archive Aris Helper{MyConfigger.NOWVERSION}", favicon="./assets/aris.ico", language="zh-cn", reload=False, port=native.find_open_port())
            except:
                # 如果GUI出错，自动使用网页端
                print("窗口端GUI出错，自动使用网页端/Window GUI error, automatically use web GUI")
                ui.run(title=f"Blue Archive Aris Helper{MyConfigger.NOWVERSION}", favicon="./assets/aris.ico", language="zh-cn", reload=False, port=native.find_open_port())
        else:
            ui.run(title=f"Blue Archive Aris Helper{MyConfigger.NOWVERSION}", favicon="./assets/aris.ico", language="zh-cn", reload=False, port=native.find_open_port())

    except Exception as e:
        import traceback
        traceback.print_exc()
        input("按任意键退出")