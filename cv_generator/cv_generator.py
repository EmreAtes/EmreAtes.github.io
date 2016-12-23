#!/usr/bin/env python3
"""
This turned out to be so complicated that actually editing the website and the
resume separately would be easier than writing this :)
"""

from datetime import date
import yaml

class ResumeItem:
    def __init__(self, name, start_date=None, end_date=None, location=None, description=None):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.description = description

    def print_text(self):
        return_str = str(self.name) + '\n'
        return_str += "{} - {}, {}".format(
            self.start_date, self.end_date, self.location) + '\n'
        return_str += str(self.description) + '\n'
        return return_str

    def print_yaml(self):
        return yaml.dump(self)

    def print_latex(self):
        return_str = "\\employer{\\textbf{%s}}\n" % self.name
        return_str += "\\title{%s - %s}\n" % (self.start_date.year, self.end_date.year)
        return return_str


if __name__ == '__main__':
    metu1 = ResumeItem("Middle East Technical University",
                       start_date=date(2010, 9, 1),
                       end_date=date(2015, 6, 1),
                       location="Ankara, Turkey",
                       description="GPA: 3.23, Ranking: 37th among 353")

    print(metu1.print_text())
    print(metu1.print_yaml())
    print(metu1.print_latex())
    

