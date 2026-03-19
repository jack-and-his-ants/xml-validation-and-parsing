from lxml import etree


def is_valid_xml(xml_path,xsd_path):
    schema = etree.XMLSchema(etree.parse(xsd_path))
    xml_file = etree.parse(xml_path)
    return schema.validate(xml_file)

if __name__ == "__main__":
    xsd_path = 'schema.xsd'
    XML_file_paths = ["examples/valid.xml","examples/invalid.xml"]
    for path in XML_file_paths:
        if is_valid_xml(path,xsd_path):
            print(path + " is valid.")
        else:
            print(path + " is invalid.")


