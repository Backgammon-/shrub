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
    
    # Any other fields are text fields (titles, descriptions, etc). Non alpha-numeric charachters are prohibited.
    if len(tokens) > 3:
        if re.search('\W+', tokens[3]):
            return False
    if len(tokens) > 4:
        if re.search('\W+', tokens[4]):
            return False
    if len(tokens) == 6:
        if re.search('\W+', tokens[5]):
            return False
    if len(tokens) > 6:
        return False
    
    return True
    
