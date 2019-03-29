def read_map(path_file):
    try:
        arq = open(path_file, 'rt')
        size_map = arq.readline().strip('\n').split(' ')
        conteudo = arq.readline()
        lst_wall = []
        map = [size_map]
        while conteudo != '':
            lst_wall.append(conteudo.strip('\n').split(' '))
            conteudo = arq.readline()
        map.append(lst_wall)
        return map
    except IOError:
        print("Arquivo não encontrado!")
        exit(0)


def create_map(path):
    config = read_map(path)
    size_map = config[0]
    lst_wall = config[1]
    col = int(size_map[1])
    lin = int(size_map[0])
    map = [[0] * col for i in range(lin)]

    for wall in lst_wall:
        col = int(wall[0])
        lin = int(wall[1])
        map[lin][col] = 1

    return map