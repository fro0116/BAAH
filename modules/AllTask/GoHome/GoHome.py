from DATA.assets.PageName import PageName
from DATA.assets.ButtonName import ButtonName
from DATA.assets.PopupName import PopupName

from modules.AllPage.Page import Page
from modules.AllTask.Task import Task

from modules.utils import go_home, click, swipe, match, page_pic, button_pic, popup_pic, sleep, config, ocr_area
# =====

class GoHome(Task):
    def __init__(self, name="GoHome" , pre_times = 1, post_times = 10) -> None:
        super().__init__(name, pre_times, post_times)
    
    def pre_condition(self) -> bool:
        return True
    
     
    def on_run(self) -> None:
        go_home(config.userconfigdict['ACTIVITY_PATH'])
        
    def post_condition(self) -> bool:
        return True