from typing import Optional, Callable
from nicegui.dependencies import register_component
from nicegui.element import Element


register_component('leaderline', __file__, 'leaderline.js')


class LeaderLine(Element):
    def __init__(
        self,
        start_element: str = '',
        end_element: str = '',
        color: str = '',
        size: int = 8,
        hide: Optional[bool] = False,
        on_show: Optional[Callable] = None,
        on_hide: Optional[Callable] = None
    ) -> None:
        super().__init__('leaderline')
        self._props['startElement'] = start_element
        self._props['endElement'] = end_element
        self._props['color'] = color
        self._props['size'] = size
        self._props['hide'] = hide
        if on_show:
            self.on('show', on_show)
        if on_hide:
            self.on('hide', on_hide)

