import xml.etree.ElementTree as ET
from xml.dom import minidom

from src.config import logger


def build_xml_tree(node):
    url_element = ET.Element("url")
    loc = ET.SubElement(url_element, "loc")
    loc.text = node["url"]

    if node.get("internal"):
        internal_elem = ET.SubElement(url_element, "internal")
        for child in node["internal"]:
            internal_elem.append(build_xml_tree(child))

    if node.get("external"):
        external_elem = ET.SubElement(url_element, "external")
        for ext_url in node["external"]:
            ext_url_elem = ET.SubElement(external_elem, "url")
            loc = ET.SubElement(ext_url_elem, "loc")
            loc.text = ext_url

    return url_element


def generate_sitemap(root_node, save_to_file=False, filename="sitemap.xml"):
    urlset = ET.Element("urlset")
    urlset.append(build_xml_tree(root_node))

    rough_string = ET.tostring(urlset, encoding="utf-8")
    parsed_xml = minidom.parseString(rough_string)
    pretty_xml = parsed_xml.toprettyxml(indent="  ")

    if save_to_file:
        save_to_xml(pretty_xml, filename)

    return pretty_xml


def save_to_xml(xml_string, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(xml_string)
    logger.info("XML збережено у sitemap.xml")
