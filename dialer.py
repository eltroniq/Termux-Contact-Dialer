#!/data/data/com.termux/files/usr/bin/env python3
import sys, os, linecache, codecs as c

contact_path = "~/contacts.vcf"

i = 0
i1 = []
i2 = []

with open(contact_path, 'r') as f:
  for l in f:
    if l.lower().find('begin:vcard') >= 0:
      i1.append(i)
    if l.lower().find('end:vcard') >= 0:
      i2.append(i)
    i += 1

contacts = [[],[]]

for i3 in range(len(i1)):
  h1 = False
  h2 = False
  for i4 in range(i1[i3], i2[i3]+1):
    l = linecache.getline(contact_path, i4)
    if l.find('FN:') >= 0 or l.find('FN;') >= 0:
      h1 = True
      if l.find('CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:')>=0:
        l1 = l.split("CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:")[1].replace('=','')[:-1]
        l1 = c.decode(l1,"hex").decode('utf8','ignore')
      else:
        l1 = l[3:-1]
    if l.lower().find('tel') >= 0 and (l.lower().find('cell') >= 0 or l.lower().find('home') >= 0):
      h2 = True
      l2 = l[9:-1]
    if h1 and h2:
      contacts[0].append(l1)
      contacts[1].append(l2)
      h1,h2 = False,False

x = sys.argv[1]
dial = []
h=0

for i in range(len(contacts[0])):
  if contacts[0][i].lower().find(x.lower()) >= 0:
    print(" [%s] %s %s"%(h,contacts[0][i], contacts[1][i]))
    dial.append(contacts[1][i])
    h+=1

x = 0

if len(dial) == 0:
  print("No matches")
  exit()

if len(dial) != 1:
  try:
    x = int(input("Please select: "))
  except Exception:
    print("Exiting...")
    exit()

os.popen("termux-telephony-call %s" % dial[x])
