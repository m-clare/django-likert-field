# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from .likert_star_tools import render_geo
from django.utils.safestring import mark_safe


register = template.Library()

# Font-awesome circle ver 5
circle_set_6 = {
    'geo': "<i class='fas fa-circle likert-circle'></i>",
    'unlit': "<i class='fas fa-circle-o likert-circle'></i>",
    'noanswer': "<i class='fa fa-ban likert-circle'></i>"
}

def fa_circles5(num, max_geo=5):
    """
    Circles for Font Awesome 3

    If num is not None, the returned string will contain num solid circles
    followed by max_geo - num empty stars
    """
    return mark_safe(render_stars(num, max_geo, circle_set_6))

register.filter('fa_circles5', fa_circles5)

