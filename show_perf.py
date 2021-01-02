import re
import os
import matplotlib
import matplotlib.pyplot as plt
import argparse


def show_plot(bandwidth, interval, filename, folder, save=True):
    fig, ax = plt.subplots()
    ax.plot(interval, bandwidth)

    ax.set(xlabel='interval (second)', ylabel='bandwidth (Mbits/sec)',
           title='bandwidth plot')
    ax.grid()
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")

    if save:
        os.makedirs(folder+"/images", exist_ok=True)
        file = folder + "/images/" + filename.strip().split('\\')[-1] + ".png"
        plt.savefig(file)


if __name__ == '__main__':
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='file', type=str,
                        nargs='+', help='perf output file')
    args = parser.parse_args()
    files = args.file
    '''
    folder = 'classic'
    files = [dataFile for dataFile in os.listdir(folder) if (
        dataFile.endswith('tcp') or dataFile.endswith('udp'))]

    target = 'Interval'
    for file in files:
        lines = list()
        begin = 0
        end = 0
        with open(os.path.join(folder, file), 'r') as f:
            for line in f:
                lines.append(re.split(r'\s+', line))

        for index, s_line in enumerate(lines):
            if begin == 0 and target in s_line:
                begin = index + 1
            elif target in s_line:
                end = index - 1

        data_line = lines[begin: end]

        bandwidth = [float(item[6]) for item in data_line]
        #interval = [item[2] for item in data_line]
        interval = range(end-begin)

        show_plot(bandwidth, interval, file, folder, True)
