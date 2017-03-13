import sys
import shlex
import re


def validate(line):
    try:
        tokens = shlex.split(line)
    except ValueError:
        return False
    except SyntaxError:
        return False
    except:
        return False
    if len(tokens) < 2:
        return False
    
    if (tokens[0] != 'list' and \
    tokens[0] != 'show' and \
    tokens[0] != 'create' and \
    tokens[0] != 'update' and \
    tokens[0] != 'edit' and \
    tokens[0] != 'comment' and \
    tokens[0] != 'delete'):
        return False
    if (tokens[1] != 'repos' and \
    tokens[1] != 'issues' and \
    tokens[1] != 'comments' and \
    tokens[1] != 'issue' and \
    tokens[1] != 'comment'):
        return False
    
    print(tokens)
    
    match = re.search('[\w-]*/?[\w-]*', tokens[2])
    if (not(match.group() is tokens[2]) or re.search('_', tokens[2]) or \
        (tokens[2] is "")):
        return False
    
    
    
    
    return True
    
