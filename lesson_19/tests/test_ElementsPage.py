import pytest
from lesson_19.ElementsPage import ElementsPage


class TestElementsPage:
    @pytest.mark.parametrize("element_name", ['Text Box', 'Check Box', 'Radio Button', 'Web Tables', 'Buttons',
                                              'Links', 'Broken Links - Images', 'Upload and Download',
                                              'Dynamic Properties', '', '', '', '', '', '', '', '', '', '',
                                              '', '', '', '', '', '', '', '', '', '', '', '', '', ''])
    def test_each_elem_name(self, chrome, element_name):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert element_name in elements
