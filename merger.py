import xml.etree.ElementTree as etree
import shutil, os, sys, getopt

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:v", ["help", "dir="])
    except getopt.GetoptError as err:
        print(str(err))
        print('nessus_merger.py -d <target_directory>')
        sys.exit(2)

    dir = None
    verbose = False
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('nessus_merger.py -d <target_directory>')
            sys.exit()
        elif opt in ("-d", "--dir"):
            dir = arg
        else:
            assert False, "unhandled option"

    print('Searching for .nessus files to merge in directory:', dir)

    ### Starting important stuff

    firstFileParsed = True
    for fileName in os.listdir(dir):
        if fileName.endswith(".nessus"):
            full_path = os.path.join(dir, fileName)
            print("Parsing - " + full_path)
            if firstFileParsed:
                mainTree = etree.parse(full_path)
                report = mainTree.find('Report')
                report.attrib['name'] = 'Merged Report'
                firstFileParsed = False
            else:
                tree = etree.parse(full_path)
                for host in tree.findall('.//ReportHost'):
                    existing_host = report.find(".//ReportHost[@name='" + host.attrib['name'] + "']")
                    if not existing_host:
                        print("Adding host: " + host.attrib['name'])
                        report.append(host)
                    else:
                        for item in host.findall('ReportItem'):
                            if not existing_host.find("ReportItem[@port='" + item.attrib['port'] +
                                                      "'][@pluginID='" + item.attrib['pluginID'] + "']"):
                                print("Adding finding: " + item.attrib['port'] + ":" + item.attrib['pluginID'])
                                existing_host.append(item)
            print(" => done.")

    if os.path.exists("nss_report"):
        shutil.rmtree("nss_report")

    os.mkdir("nss_report")
    mainTree.write("nss_report/report.nessus", encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    main()
