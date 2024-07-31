from DATA.assets.PageName import PageName
from DATA.assets.ButtonName import ButtonName
from DATA.assets.PopupName import PopupName

from modules.AllPage.Page import Page
from modules.AllTask.Task import Task
from modules.AllTask.EnterGame.Loginin import Loginin
from modules.AllTask.EnterGame.CloseInform import CloseInform

from modules.utils import close_app, click, swipe, match, page_pic, button_pic, popup_pic, sleep, config, ocr_area

class RestartGame(Task):
    def __init__(self, name="RestartGame" , pre_times = 1, post_times = 10) -> None:
        super().__init__(name, pre_times, post_times)
    
    def pre_condition(self) -> bool:
        return True
    
     
    def on_run(self) -> None:
        close_app(config.userconfigdict['ACTIVITY_PATH'])
        Loginin().run()
        CloseInform().run()
        
    
    def post_condition(self) -> bool:
        return Page.is_page(PageName.PAGE_HOME)