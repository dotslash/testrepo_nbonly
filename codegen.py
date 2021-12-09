import sys
from pathlib import Path
import uuid

def make_file_content(fname, is_notebook):
  ret = [fname]
  rand_str = lambda: uuid.uuid4().hex
  len_rand_str = len(rand_str())
  for i in range(1000//len_rand_str):
      ret.append(rand_str())
  all_lines = '\n'.join(ret)
  content = f'"""\n{all_lines}\n"""\n'
  if is_notebook:
    content = "# Databricks notebook source\n" + content
  return content

if __name__ == '__main__':
  nfiles = int(sys.argv[1])
  for i in range(nfiles):
    if i%10 >= 2: continue
    # 123 => 1/2/3.txt
    fname = '/'.join(list(str(i)))
    fname = f"{fname}_nb.py"
    p = Path(fname)
    p.parent.mkdir(exist_ok=True)
    p.write_text(make_file_content(fname, is_notebook=True))
