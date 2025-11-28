
def get_suffix(filename, has_dot):
    suffix = ''
    suffix_index = filename.rfind('.')
    suffix = filename[suffix_index:] if has_dot else filename[suffix_index+1:]

    return suffix

if __name__ == '__main__':
    print(get_suffix('daeass.pdf', False))
