#!/usr/bin/python3

import fnmatch
import os
import os.path
import codecs
import re

repo_dir = "../../../"
modules_col = "modules"
default_doc = "readme.md"

doc_build_dir = "../../build/"
modules_index = doc_build_dir + "modules_index.md"

#-------------------------------------------------------------------------------
def sanitize(txt):
  txt = re.sub(r"\s+", " ", txt).strip()
  return txt

#-------------------------------------------------------------------------------
def search_node_name(txt):
  txt = sanitize(txt).lower()
  txt = re.sub(r"\W+", "_", txt)
  return txt

#-------------------------------------------------------------------------------
def search_ref(txt):
  if re.search(r"([A-Z][A-Z][A-Z]-[\w_]+)", txt) is None:
    return None
  return re.search(r"([A-Z][A-Z][A-Z]-[\w_]+)", txt).group(1)

#-------------------------------------------------------------------------------
def collection(name):
  rootPath = repo_dir + name
  pattern = default_doc
  ret=[]
  for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
      full_path = os.path.join(root, filename)
      ret += [full_path]
  return ret

#-------------------------------------------------------------------------------
def md_parse(text):
  lines = text.splitlines()
  dom = {"":"", "###":""}
  context = dom
  cur_level = 0
  for i in range(0, len(lines)-1):
    li = lines[i]
    re_obj = re.match(r" *(#+)(.+)", li)
    if re_obj:
      new_level = len(re_obj.group(1))
      node_name = search_node_name(re_obj.group(2))
      if new_level > cur_level + 1:
        dom["###"] += "#Error : level mismatch on line " + str(i) + " :\n    " + li + "\n"
      else:
        for lev in range(new_level, cur_level+1): context=context[".."]
        context[node_name]={"..":context, "":""}
        context=context[node_name]
        cur_level=new_level
    else:
      context[""] += li + "\n"
  return dom

#-------------------------------------------------------------------------------
def doc(name):
  input_file = codecs.open(name, mode="r", encoding="utf-8")
  text = input_file.read()
  dom = md_parse(text)
  return dom

#-------------------------------------------------------------------------------
def store(name, text):
  output_file = codecs.open(modules_index, "w", encoding="utf-8",  errors="xmlcharrefreplace" )
  output_file.write(text)
  return name

#-------------------------------------------------------------------------------
def get(dic, key):
  
    try:
      val = dic[key]
    except KeyError:
      print "#Error : missing header " + key
      val = "###"
    except :
      val = "###"
    return val

#-------------------------------------------------------------------------------
if __name__ == "__main__":
  print("Documentation builder start :")

  md = """\
# Modules table
| Name | Title | Amplitude |
|------|-------|-----------|
"""
  for doc_name in collection(modules_col):
    print("<<< " + doc_name)
    dom = doc(doc_name)
    print(dom["###"])
    root = get(dom, "modules")
    r = search_ref(get(get(root, "name"), ""))
    t = sanitize(  get(get(root, "title"), ""))
    a = sanitize(  get(get(root, "technology"), ""))
    
    md += '|[`{ref}`](../../modules/{ref} "{title}")|_{title}_|{technology}|\n'.format(
          ref=r, title=t, technology=a)

  store(modules_index, md)
  print(">>>\n" + md)
