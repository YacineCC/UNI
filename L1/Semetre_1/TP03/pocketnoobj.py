#!/usr/bin/env python3
# coding: utf-8
"""
 ------------------------------------------------------------------
 PocketNoObj - Pocket No Object
 Version 1.4 (4 avril 2018)
 Module programmation impérative des listes, dictionnaires, chaînes
 de caractères et manipulation de fichiers

 J. RAZIK - razik@univ-tln.fr
 http://razik.univ-tln.fr
 ------------------------------------------------------------------

 ------------------------------------------------------------------
 A destination des étudiants de L1 informatique à l'UTLN.

 Ce petit module permet de charger des fonctions de plusieurs modules de base
 dans l'espace de nommage global de l'utilisateur pour éviter une utilisation
 orientée objet de ces fonctions.

 Les modules impactés sont: list, dict, str, fichier (read, write, etc).

 Exemples:
 >>> a = [1, 2, 3]
 >>> f = open('/tmp/test', 'r')

 Sans ce module:
 >>> a.pop()
 >>> a.index(2)
 >>> a.append(4)
 >>> f.read(1)
 >>> f.close()

 Avec ce module:
 >>> pop(a)
 >>> index(a, 2)
 >>> append(a, 4)
 >>> read(f, 1)
 >>> close(f)

 ------------------------------------------------------------
"""

# from __main__ import __dict__ as namespace
from builtins import __dict__ as namespace
from collections import OrderedDict
import pydoc
import inspect
import _io

_cmd_list = ['list_' + f for f in dir(list()) if not f.startswith('_') and
             eval('callable(list.' + f + ')')]
_cmd_dict = ['dict_' + f for f in dir(dict()) if not f.startswith('_') and
             eval('callable(dict.' + f + ')')]
_cmd_str = ['str_' + f for f in dir('') if not f.startswith('_') and
            eval('callable(str.' + f + ')')]
_cmd_file = [
    'file_' + f for f in dir(_io.TextIOWrapper) if not f.startswith('_') and
    eval('callable(_io.TextIOWrapper.' + f + ')')]

_cmd = _cmd_list + _cmd_dict + _cmd_str + _cmd_file

# doublons = [w for w in cmd if sum(
#     [w in c for c in [cmd_list, cmd_dict, cmd_str, cmd_file]]) > 1]
# print(doublons)

# {'copy': ['list', 'dict'], 'count': ['list', 'str'],
#  'clear': ['list', 'dict'], 'index': ['list', 'str'],
#  'pop': ['list', 'dict']}
# pop est un peu différent entre list et dict
# count est différent entre list et str


_types = {'list': 'list',
          'dict': 'dict',
          'str': 'str',
          'file': '_io.TextIOWrapper'}


def _makedoc(fun):
    """ Fonction qui retourne la documentation assossiée à une fonction
    en appliquant quelques transformations si la signature apparait dans la
    doc, pour la changer en impérative. """
    le_module, fonc = fun.split('_', 1)
    module = _types[le_module]
    doc = ''
    # print(fun)
    doc = eval('pydoc.getdoc(' + module + '.' + fonc + ')')
    # eval(module + '.' + fonc + '.__doc__')
    # print(doc)
    la = doc.split('->', 1)
    if len(la) == 1:
        # il n'y a pas de description de la signature de la fonction
        # print(doc)
        return '"' + le_module + '" case\n' + doc
    else:
        # la signature est présente
        a, a_reste = la
    # on cherche le "." de la notation objet
    b, b_reste = a.split('.', 1)
    # on cherche le début des paramètres
    c, c_reste = b_reste.split('(', 1)
    if c_reste[0] == ')':
        # pas de paramètres "()"
        d = ''
    else:
        d = ', '
    # on recompose
    doc = c + '(' + b + d + c_reste + '->' + a_reste
    # print(doc)
    return '"' + le_module + '" case\n' + doc


def _makesig(fun):
    """ Fonction qui permet de générer la signature si possible non générique
    pour une fonction devenue impérative. """
    module, fonc = fun.split('_', 1)
    initiales = module.upper()
    module = _types[module]
    le_self = ''

    try:
        sig = eval('inspect.signature(' + module + '.' + fonc + ')')
        sig = OrderedDict(
            ((s, str(sig.parameters[s])) for s in sig.parameters))
    except ValueError as e:
        sig = OrderedDict((('*args', '*args'), ('**kwargs', '**kwargs')))

    if 'self' in sig:
        del(sig['self'])
    if '/' in sig:
        del(sig['/'])

    if initiales[0] not in sig:
        sig[initiales[0]] = initiales[0]
        sig.move_to_end(initiales[0], last=False)
        le_self = initiales[0]
    elif initiales[:2] not in sig:
        sig[initiales[:2]] = initiales[:2]
        sig.move_to_end(initiales[:2], last=False)
        le_self = initiales[:2]
    elif initiales not in sig:
        sig[initiales] = initiales
        sig.move_to_end(initiales, last=False)
        le_self = initiales
    else:
        print('Erreur de nommage.')
        exit(1)

    return list(sig.values()), le_self


def _makefun(fun, doublon):
    """
    Permet de créer dynamiquement une fonction non-objet pour une fonction
    objet
    """
    le_module, fonc = fun.split('_', 1)
    module = _types[le_module]

    # création de la signature de la nouvelle fonction
    signature, le_self = _makesig(fun)
    # signature de l'appel à la vraie fonction (sans les '=' des valeurs
    # par défaut)
    signature_appel = [param.split('=')[0] for param in signature]

    to_exec = ('def ' + fonc + '(' + ', '.join(signature) + ')' + ':\n    '
               'return ' + le_self + '.' + fonc +
               '(' + ', '.join(signature_appel[1:]) +
               ')' + '\n')
    # print(to_exec)  # pour le debug

    # création dynamique de la nouvelle fonction
    exec('def ' + fonc + '(' + ', '.join(signature) + ')' + ':\n    ' +
         'return ' + le_self + '.' + fonc +
         '(' + ', '.join(signature_appel[1:]) +
         ')' + '\n')

    # on extrait la documentation de la fonction d'origine
    doc = _makedoc(fun)

    # on l'ajoute à la nouvelle fonction
    if doublon is None:
        exec(fonc + '.__doc__ = """' + doc + '"""')
    else:
        # la fonction est déjà définie dars l'espace de nommage,
        # on augmente la documentation
        exec(fonc + '.__doc__ = """' + doublon.__doc__ + '\n\n' + doc + '"""')

    return locals()[fonc]


# on ajoute les fonctions dans l'espace de nommage
for _c in _cmd:
    _module, _fonc = _c.split('_', 1)
    namespace[_fonc] = _makefun(_c, namespace.get(_fonc))

print("Initialisation de l'espace de nommage fait.")
