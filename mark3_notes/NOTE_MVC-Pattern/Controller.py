import Model
import View
from kivymd.app import MDApp
from kivy.lang import Builder


class Controller(MDApp):
    """
    Class Controller for pattern MVC, contain classes Model (interaction with SQL Lite)
    and View (HMI)

    """
    title = "Notes MVC v2.0"
    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        self.Model = Model.Model(self)
        self.View = View.View(self)


    def build(self):
        """
        built-in function of kivy.MDApp, callback from function Controller().run()
        """
        return self.View.Manager

    def update_DB(self, note):
        """
        Callback function from View fkr interaction with Model
        """
        self.Model.Update_note_DB(note)

    def get_from_DB(self):
        """
        Callback function from View fkr interaction with Model
        """
        data = self.Model.Get_data_DB()
        return data

    def save_to_DB(self, note):
        """
        Callback function from View fkr interaction with Model
        """
        self.Model.Save_note_DB(note)

    def del_note_DB(self, note_id):
        """
        Callback function from View fkr interaction with Model
        """
        self.Model.Delete_note_DB(note_id)

#Started programm
if __name__ == "__main__":
    My_programm = Controller()
    My_programm.run()
