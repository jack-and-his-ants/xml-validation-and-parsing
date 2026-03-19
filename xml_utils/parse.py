import xmltodict
import json

def parse_xml_to_json(xml_path,dest):
    with open(xml_path,mode='r',encoding="utf-8") as f:
        data = xmltodict.parse(f.read())
    with open(dest,mode='w',encoding='utf-8') as f:
        f.write(json.dumps(data, indent=2,ensure_ascii=False))

if __name__ == "__main__":
    parse_xml_to_json("examples/valid.xml")