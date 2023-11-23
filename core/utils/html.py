from requests import get
from bs4 import BeautifulSoup


class HtmlUtils:
    def get_page(self, url):
        response = get(url)
        response.encoding = 'utf-8'
        response_html = BeautifulSoup(response.text, 'html.parser')
        return response_html

    def find_by_tag(self, parent, tag_name, err_if_not_found=False):
        element = parent.find(tag_name)
        if not element:
            if err_if_not_found:
                raise Exception(f"can't find the element with the tag: {tag_name}")
            else:
                # log it
                pass
        return element


    def find_by_id(self, parent, id, err_if_not_found=False):
        element = parent.find(id=id)
        if not element:
            if err_if_not_found:
                raise Exception(f"can't find the element with the id: {id}")
            else:
                # log that it is not found
                pass

        return element

    def find_by_class(self, parent, class_, err_if_not_found=False):
        element = parent.find(class_=class_)
        if not element:
            if not err_if_not_found:
                raise Exception(f"can't find the element with the class: {class_}")
            else:
                # log it
                pass

        return element

    def find_all_by_class(self, parent, class_, err_if_not_found=False):
        elements = parent.find_all(class_=class_)
        if not element:
            if not err_if_not_found:
                raise Exception(f"can't find any element with the class: {class_}")
            else:
                # log it
                pass

        return elements

    def find_all(self, parent, recursive=False):
        elements = parent.find_all(recursive=recursive)
        if not elements:
            # log that no elmeent was found
            pass
        return elements

