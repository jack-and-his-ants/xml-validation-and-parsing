from lxml import etree

valid_XML_path = "examples/valid.xml"
invalid_XML_path = "examples/invalid.xml"
XML_files = [valid_XML_path,invalid_XML_path]
# loading xml schema
schema = etree.XMLSchema(etree.parse("schema.xsd"))

for XML_file_path in XML_files:
    xml_file = etree.parse(XML_file_path)
    if schema.validate(xml_file):
        print(f"{XML_file_path} is valid")
    else:
        print(f"{XML_file_path} is invalid")