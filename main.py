from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.font_definitions import fonts
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.uix.tab import MDTabsBase
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.label import  MDLabel
from kivymd.uix.menu import MDDropdownMenu

KV = f'''
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts

# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "112dp", "112dp"
            source: "data/logo/icon_title.png"

    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list



Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: app.title
                        elevation: 2
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["star-outline", lambda x: app.on_star_click()]]
                        
                       

                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        height: "48dp"
                        tab_indicator_anim: False
                        
                        Tab:
                            id: tab1
                            name: "tab1"
                            icon: 'clock-plus-outline'
                            title: "Активности"
                            
                            BoxLayout:
                                orientation: "vertical"
                                padding: "10dp"
                                
                                MDRectangleFlatIconButton:
                                    icon: "android"
                                    text: "MDRectangleFlatIconButton"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    line_color: "red"
                                    theme_icon_color: "Custom"
                                    icon_color: "orange"
                        Tab:
                            id: tab2
                            name: "tab2"
                            icon: 'playlist-check'
                            title: "История"
                        Tab:
                            id: tab2
                            name: "tab3"
                            icon: "google-analytics"
                            title: "График отслеживания"






        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    pass

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Tab(MDFloatLayout, MDTabsBase):
    pass


class StlTimeTracker(MDApp):
    title = "STL Time Tracker"
    by_who = "by Vitaliy Shpak"

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def on_start(self):
        icons_item_menu_Lines = {
            "account-cowboy-hat": "About author",
            "youtube": "My YouTube",
            "coffee": "Donate author",
            "github": "Source code",
            "share-variant": "Share app",
            "shield-sun": "Dark/Light"
        }

        for icon_name in icons_item_menu_Lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_Lines[icon_name])
            )

 #       icon_tab_items = {
 #           'clock-plus-outline': 'Активности',
 #          'playlist-check': 'История',
  #          'google-analytics': 'График отслеживания'

  #      }
  #      for icon_name, name_tab in icon_tab_items.items():
  #          self.root.ids.tabs.add_widget(
   #             Tab(icon=icon_name, title=name_tab)
   #         )

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        print('tab cliked' + tab_text)

    def on_star_click(self):
        print('Star cliked')


StlTimeTracker().run()
