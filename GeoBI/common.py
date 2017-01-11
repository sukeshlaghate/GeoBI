# structure that is common for admin site and websites


# class defining the submenus in side bar or in nav bar
class SubMenu(object):
    name = ''
    style_class = ''
    href = ''


# class defining main menu in side bar or in nav bar
class Menu(object):
    name = ''
    style_class = ''
    href = ''
    has_children = False
    children = None  # List of sub menu for a given menu, not to be initialized here


# class defining the menu sections each containing the
class MenuSection(object):
    section_title = ''
    style_class = ''
    href = ''
    has_children = False
    children = None  # List of menu for a given section, not to be initialized here


