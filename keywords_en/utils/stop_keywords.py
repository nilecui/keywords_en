from __future__ import absolute_import, print_function, unicode_literals

from tqdm.notebook import tqdm
from itertools import islice
from re import sub


class StopKeywords:
    def __init__(self, stop_kw_file="stop_keywords.csv"):
        self.stop_kw_file = stop_kw_file

    def get_keywords(self):
        num_lines = sum(1 for line in open(self.stop_kw_file))
        with open(self.stop_kw_file) as kwfile:
            dict_idf = {}
            with tqdm(total=num_lines) as pbar:
                for i, line in tqdm(islice(enumerate(kwfile), 1, None)):
                    try:
                        cells = line.split(",")
                        idf = float(sub("[^0-9.]", "", cells[3]))
                        dict_idf[cells[0]] = idf
                    except Exception as e:
                        print(i, e)
                        print("Error on: " + line)
                        continue
                    finally:
                        pbar.update(1)


        return dict_idf


if __name__=="__main__":
    stop_kw_obj = StopKeywords(stop_kw_file="stop_keywords.csv")
    stop_kw_obj.read_lines()
