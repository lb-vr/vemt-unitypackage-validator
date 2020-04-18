import os
import dataclasses
import generator

from PySide2.QtWidgets import (
    QCheckBox,
    QRadioButton
)
from qt.widgets import EditableListView, EditableListModel


name = "ルートフォルダ名"


def run(assets: dict, rule: dict):
    pass


@dataclasses.dataclass(eq=False)
class Generator(generator.GeneratorBase):
    cbEnable: QCheckBox
    rbWhitelist: QRadioButton
    rbBlacklist: QRadioButton
    ruleListView: EditableListView

    def __post_init__(self):
        model = EditableListModel(addable=True,
                                  removable=True,
                                  swappable=False,
                                  editable=True)
        self.ruleListView.setModel(model)
        self.ruleListView.setAddArgs("--入力--")

    @classmethod
    def getTitle(cls):
        return "ルートフォルダ名"

    @classmethod
    def getUiPath(cls) -> str:
        return os.path.join(os.path.dirname(__file__), "root_directory_filter.ui")

    def toDict(self) -> dict:
        return {
            "root_directory_filter": {
                "enabled": self.cbEnable.isChecked(),
                "type": "whitelist" if self.rbWhitelist.isChecked() else "blacklist",
                "values": self.ruleListView.getListData()
            }
        }