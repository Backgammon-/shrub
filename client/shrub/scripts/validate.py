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
    """
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
    """
    
    if (tokens[0] != 'create_comment' and \
    tokens[0] != 'create_issue' and \
    tokens[0] != 'delete_comment' and \
    tokens[0] != 'edit_comment' and \
    tokens[0] != 'edit_issue' and \
    tokens[0] != 'list_comments' and \
    tokens[0] != 'list_issues'):
        return False
    
    
    print(tokens)
    
    match = re.search('[\w-]*/?[\w-]*', tokens[1])
    if (not(match.group() is tokens[1]) or re.search('_', tokens[1]) or \
        (tokens[1] is "")):
        return False
    
    # Any other fields are text fields (titles, descriptions, etc). Non alpha-numeric charachters are prohibited.
    if len(tokens) > 2:
        if re.search('\W+', tokens[2]):
            return False
    if len(tokens) > 3:
        if re.search('\W+', tokens[3]):
            return False
    if len(tokens) == 5:
        if re.search('\W+', tokens[4]):
            return False
    if len(tokens) > 5:
        return False
    
    return True
    
