# module for saving reports to a file and reading them back
def save_report(report, filename):
    path = filename + ".txt"

    # write report content into file
    with open(path, "w", encoding="utf-8") as f:
        f.write(report)
    return path


def read_back(path):

    # read and return file content
    with open(path, "r", encoding="utf-8") as f:
        return f.read()