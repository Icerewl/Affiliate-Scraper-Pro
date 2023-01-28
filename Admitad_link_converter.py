

def link_convert(admitad_before):
    admitad_before = admitad_before.replace("/","%2F").replace("?","%3F").replace("=","%3D").replace("&","%26").replace(":","%3A")
    admitad_after = "https://alitems.co/g/1e8d1144949e792578f516525dc3e8/?ulp=" + admitad_before

    return admitad_after

def file_opener(file_name):
    with open(file_name,encoding="utf-8") as f:
        lines = f.readlines()
        lines = ' '.join([str(elem) for elem in lines]).replace('"',"")
    return lines.split(",")
