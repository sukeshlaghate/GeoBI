from django.shortcuts import render
from django.http import HttpRequest
from GeoBI.common import MenuSection, Menu,  SubMenu

# Create your views here.
# TODO: this menu section generation should happen dynamically by reading configuration files
map_section = MenuSection()
map_section.section_title = "General"

general_maps_menu = Menu()
general_maps_menu.name = "Maps"
general_maps_menu.style_class = "fa fa-map-marker fa-lg"

submenu1 = SubMenu()
submenu1.name = "Map1"
submenu1.href = "map1.html"

submenu2 = SubMenu()
submenu2.name = "Map2"
submenu2.href = "map2.html"

general_maps_menu.children = list()
general_maps_menu.children.append(submenu1)
general_maps_menu.children.append(submenu2)
general_maps_menu.has_children = True

map_section.children = [general_maps_menu]
map_section.has_children = True

search_section = MenuSection()
search_section.section_title = "Searches"

menu_sections = [map_section, search_section]


def indexview(request):
    """Renders the GIS admin configuration page."""
    assert isinstance(request, HttpRequest)
    print(menu_sections)
    for section in menu_sections:
        print(section.section_title)
        if section.has_children:
            for menu in section.children:
                print(menu.name)
                print(menu.has_children)

    return render(
        request,
        'website/index.html',
        {
            'site_title': 'Config Console',
            'username': 'Guest',
            'website_sidebar': True,
            'menu_sections': menu_sections,

        }
    )


