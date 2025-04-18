
from DATA.assets.PageName import PageName
from DATA.assets.ButtonName import ButtonName
from DATA.assets.PopupName import PopupName

from modules.AllPage.Page import Page
from modules.AllTask.Task import Task

from modules.utils.log_utils import logging

from modules.utils import click, swipe, match, page_pic, button_pic, popup_pic, sleep

class CollectPower(Task):
    def __init__(self, name="CollectPower", pre_times = 3, post_times = 3) -> None:
        super().__init__(name, pre_times, post_times)


    def pre_condition(self) -> bool:
        return Page.is_page(PageName.PAGE_CAFE)


    def on_run(self) -> None:
        self.clear_popup()
        if match(button_pic(ButtonName.BUTTON_CAFE_CANNOT_COLLECT)):
            logging.info({"zh_CN": "咖啡馆没有可领取的物品", "en_US": "there's nothing in cafe"})
            return

        # 重复点收集直到出现弹窗
        openinfo = self.run_until(
            lambda: click((1156, 648)),
            lambda: self.has_popup(),
            times=3
        )
        if openinfo:
            logging.info({"zh_CN": "成功点击右下角收集",
                          "en_US": "Successfully click the Collect button in the lower right corner"})
        else:
            logging.info({"zh_CN": "没有可收集的物品", "en_US": "No items to collect"})
            return
        # 重复点领取直到领取按钮变灰，这之间其实也关闭了领取成功的弹窗
        button_collect_match_res = match(button_pic(ButtonName.BUTTON_COLLECT), returnpos=True)
        button_collect_position = button_collect_match_res[1]
        collect_res = self.run_until(
            lambda: click(button_collect_position),
            # 亮度变换可信度不会下降太多，这里靠比可信度大小
            # 点击直到看到灰色按钮并确认是灰色不是亮色
            lambda: match(button_pic(ButtonName.BUTTON_COLLECT_GRAY)) and (
                        match(button_pic(ButtonName.BUTTON_COLLECT_GRAY), returnpos=True)[2] >
                        match(button_pic(ButtonName.BUTTON_COLLECT), returnpos=True)[2]),
            times=4)
        if collect_res:
            logging.info({"zh_CN": "成功点击领取", "en_US": "Successfully clicked to claim"})
        else:
            logging.warn({"zh_CN": "领取失败", "en_US": "Failed to collect"})
        # 不管成功失败，关闭弹窗
        self.clear_popup()

    def post_condition(self) -> bool:
        return Page.is_page(PageName.PAGE_CAFE)