import re, json, requests, validators
from bs4 import BeautifulSoup
import os, sys

CVE_urls = "https://github.com/TheMirkin/CVE-List-Public-Exploits";
#print(type(lhost));

data = {
    "rhost": None,
    "lhost": None,
    "exploit": None,
    "payload": None
}
class commands(object):
    def set(self, arguement):
        arguement = arguement.split();
        for sets in list(data):
            matches = [match for match in arguement if sets in match]
            comment = "".join(matches).split(":");  
           # if matches==[]: return
            try:comment = dict({comment[0]: comment[1]}); data.update(comment)#lhost=comment[1]);
            except Exception: pass
            print(data);
                
    def use(self, arguement):
        print(arguement);
        try:
            sys.path.insert(1, arguement);#"./tools/exploit/");
            import sample as db
            db.main("funny");
        except Exception: print("can't find module!");
            
funcs = commands();

def read_CVE(resp):
    data = json.loads(resp);
    print("[+]----------------------------------------");
    print("[  CVE_DATA_META:");
    for cve_data in data["CVE_data_meta"]:
        print("-----] "+cve_data+": "+data["CVE_data_meta"][cve_data]);

    print("     "+"[-]============Vendor==============");
    for cve_data in data["affects"]["vendor"]["vendor_data"]:
        for product in cve_data["product"]["product_data"]:
            print("     "+"-----] "+"Product-Name: "+product["product_name"]);
            print("     "+"     "+"[-]============VERSION=========");
            for version in product["version"]["version_data"]:
                for lists in version:
                    print("     "+"     "+"-----] "+lists+": "+version[lists]);
    print("[I]=======================================[I]");
    try:
        for impact in data["impact"]["cvss"]:
            print("-----] "+impact+": "+data["impact"]["cvss"][impact]);
    except Exception:
        print("IMPACT: None Taken.");
    for cve_data in data["description"]["description_data"]:
        print("[D]======================================[D]");
        print("-----] "+"lang: "+cve_data["lang"]);
        print("-----] "+"value: "+cve_data["value"]);
    print("[+]----------------------------------------");

while True:
    inputs = input()
    inputs = inputs.split()
    getattr(funcs, inputs[0])(inputs[1]);
   # try:
   # except Exception: print("invalid command");
#cve = "https://github.com/TheMirkin/CVE-List-Public-Exploits/blob/main/CVE%20List/2019/0xxx/CVE-2019-0001.json"
#try:
   # r = requests.get(CVE_urls);
    #bs = BeautifulSoup(r.text, features="lxml");
    #file = bs.find_all(title=re.compile("CVE List"))#"CVE-2019-7069.json"));
   # print(file);
#except Exception:
  #  print("nope");


