#!/usr/bin/env python3
"""Audit « tuto ou réflexion » des TP : mesure objective (aucune modification). Usage : python3 tools/audit_tp.py [csv]"""
import re,glob,os,sys
rows=[]
for f in sorted(set(glob.glob('docs/**/02-tp.md',recursive=True))):
    s=open(f,encoding='utf8').read()
    body=re.sub(r'<details.*?</details>','',s,flags=re.S)           # hors aides repliées
    blocks=re.findall(r'```[a-z]*\n(.*?)```',body,flags=re.S)
    cmdlines=sum(len([l for l in b.split('\n') if l.strip() and not l.strip().startswith(('#','!'))]) for b in blocks if not re.search(r'^\s*(Interface|Port|VLAN|Pro )',b))
    inline=len(re.findall(r'`[a-z][a-z0-9 /\-\.]{5,}`',body))        # commandes en ligne
    q=len(re.findall(r'❓',s))
    qj=len(re.findall(r'❓[^\n]*(pourquoi|explique|justifie|à ton avis|que se passe|qu.est-ce qui|comment saurais|que conclu|quel risque|que feras|que deviendrait)',s,flags=re.I))
    pred=len(re.findall(r'(à ton avis|prédis|anticipe|avant de (lancer|tester|taper|valider)|que va-t-il|que vas-tu observer|hypoth)',s,flags=re.I))
    bilan=1 if re.search(r'(ce que j.ai (appris|décidé|observé|compris)|ce que je retiens|j.ai décidé|ma preuve)',s,flags=re.I) else 0
    pas=1 if re.search(r'passeport',s,flags=re.I) else 0
    cocher=1 if re.search(r'Ce que je sais faire',s) else 0
    pannes=len(re.findall(r'(panne|diagnostic|dépann)',s,flags=re.I))
    det=len(re.findall(r'<details',s))
    words=len(body.split())
    tuto=(cmdlines+inline)/max(1,q)                                   # commandes données par question posée
    rows.append(dict(pas=pas,f=f.replace('docs/','').replace('/02-tp.md','').replace('/0','/0'),cmd=cmdlines,inl=inline,q=q,qj=qj,pred=pred,bilan=bilan,cocher=cocher,pan=pannes,det=det,w=words,tuto=round(tuto,1)))
if len(sys.argv)>1:
    import csv; w=csv.DictWriter(open(sys.argv[1],'w',newline=''),fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
rows.sort(key=lambda r:-r['tuto'])
print('%-44s %4s %4s %3s %5s %4s %5s %5s %5s %5s'%('TP','cmd','inl','❓','justif','pred','bilan','pass','aides','tuto'))
for r in rows: print('%-44s %4d %4d %3d %5d %4d %5d %5d %5d %5.1f'%(r['f'][:44],r['cmd'],r['inl'],r['q'],r['qj'],r['pred'],r['bilan'],r['pas'],r['det'],r['tuto']))
print(len(rows),'TP')
