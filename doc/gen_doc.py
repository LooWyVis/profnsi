#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# depuis le dossier contenant profnsi_autodoc.sty
python3 gen_doc.py profnsi.sty --out-md doc.md

Structure du format autodoc

% --- autodoc
% name: \\maCommande
% kind: newcommand
% args:
%   num: 2
%   opt_default: ValeurParDefaut
% description: Ma super commande qui...
% example: \\maCommande{arg1}[opt]
% --- end-autodoc
"""


import re, argparse, html, datetime
from pathlib import Path

def parse_autodoc(text):
    entries = []
    blocks = re.findall(r'% --- doc(.*?)% --- end-doc', text, flags=re.S)
    for b in blocks:
        data = {'args': {}, 'meta': {}}
        lines = b.splitlines()
        for line in lines:
            s = line.lstrip('%').strip()
            if not s: continue
            if s.startswith('name:'): data['name'] = s.split('name:',1)[1].strip().lstrip('\\')
            elif s.startswith('kind:'): data['kind'] = s.split('kind:',1)[1].strip()
            elif s.startswith('description:'): data['description'] = s.split('description:',1)[1].strip()
            elif s.startswith('example:'): data['example'] = s.split('example:',1)[1].strip()
        in_args = False
        for line in lines:
            raw = line.lstrip('%')
            if raw.strip().startswith('args:'): in_args = True; continue
            if in_args:
                if not raw.startswith('   '): in_args = False; continue
                kv = raw.strip().split(':',1)
                if len(kv)==2: data['args'][kv[0].strip()] = kv[1].strip()
        data.setdefault('description','')
        data.setdefault('example','')
        data.setdefault('args',{})
        entries.append(data)
    entries.sort(key=lambda x: x.get('name','').lower())
    return entries

def render_markdown(entries):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    out = ['#Profnsi']
    out += [f'Documentation des commandes — générée le {now}\n']
    out += ['# Présentation','']
    out += ['**Un package pour les enseignants de NSI, pour afficher des structures de données facilement, des opérations binaires, du code, ...**', '']
    out += ['**Inclus un système d\'auto template de document, avec gestion automatique de version éléves/prof**', '']
    out += ["""```tex
\\documentclass[11pt]{exam}

\\usepackage[a4paper,margin={.1\\paperheight,.1\\paperwidth},marginratio=1:1]{geometry}

\\usepackage[french]{babel}

\\usepackage[T1]{fontenc}

% Choix des options et des infos d’en-tête
\\usepackage[cours,eleve]{profnsi}
\\profnsisetup{
niveau=Première,
matiere=NSI,
titre=Représentation des données,
chapitre=3
}

\\begin{document}
\\creerDoc
ecrire votre document
\\end{document}
```""", "",]
    
    out += ['# Listes des commandes','']
    for e in entries:
        disp = '\\' + e['name']
        args_str = ', '.join([f'`{k}={v}`' for k,v in e['args'].items()]) or '_aucun_'
        desc = (e.get('description','') or '_TODO_').replace('\\n','\n')
        ex = (e.get('example','') or 'TODO').replace('\\n','\n')
        if ex != "TODO":
            out += [
                f'## {disp}',
                f'**Type** : `{e["kind"]}`  ',
                f'**Arguments** : {args_str}  ',
                f'**Description** :\n\n{desc}\n',
                f'**Exemple** :\n\n```tex\n{ex}\n```',
                ''
            ]
        else:
            out += [
                f'## {disp}',
                f'**Type** : `{e["kind"]}`  ',
                f'**Arguments** : {args_str}  ',
                f'**Description** :\n\n{desc}\n',
                ''
            ]

    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input_sty', help='Chemin du .sty annoté')
    ap.add_argument('--out-md', default='doc.md')
    args = ap.parse_args()
    text = Path(args.input_sty).read_text(encoding='utf-8', errors='ignore')
    entries = parse_autodoc(text)
    Path(args.out_md).write_text(render_markdown(entries), encoding='utf-8')
    print('OK:', args.out_md)

if __name__ == '__main__':
    main()