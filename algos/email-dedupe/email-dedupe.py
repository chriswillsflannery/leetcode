#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
We want to build a tool to deduplicate and collect email & user id pairs.
The name & email pairs are provided as: name:email
Name can be constructed in a set of different ways:
- <First Name>
- <Last Name>,<First Name>
- <First Name> <Last Name>
- <First Initial>. <Middle Initial>. <Last Name>
- <First Name> <Middle Name> <Last Name>
- <First Name> <Middle Initial>. <Last Name>
- <Last Name>,<First Name> <Middle Name>
For John Fitzgerald Kennedy, all following can be encountered.
John
Kennedy, John
John Kennedy
Kennedy, John Fitzgerald
John Fitzgerald Kennedy
J. F. Kennedy
John F. Kennedy
Customer will be sending us a file containing these entries and we need to prepare a {email: name} map.
Note that we want to capture as much information as possible, i.e. if there are multiple entries
and only some of those contain the middle name, we want the output to have it.
The output name should be in "FirstName MiddleName LastName" format (or initials)
Sample File:
John:john@company.com
Kennedy,John:john@company.com
John Kennedy:john@company.com
Kennedy,John Fitzgerald:john@company.com
John Fitzgerald Kennedy:john@company.com
Carter:carter@company.com
Ford:ford@company.com
Ford,Gerald:ford@company.com
Gerald Ford:ford@company.com
The result would be:
  {
    "john@company.com": "John Fitzgerald Kennedy",
    "carter@company.com": "Carter"
    "ford@company.com": "Gerald Ford"
  }
"""


from collections import deque
import re

initial_regex = r"(?P<%s_initial>[a-zA-Z]\.)"
first_initial = initial_regex % "first"
middle_initial = initial_regex % "middle"
name_regex = r"(?P<%s_name>[a-zA-Z]+)"
first_name = name_regex % "first"
last_name = name_regex % "last"
middle_name = name_regex % "middle"

# firstName (optional lastName), cases 1 and 3
name_regex_one = re.compile("^(?P<first_name>[a-zA-Z]+)(?: (?P<last_name>[a-zA-Z]+))?$")
# last_name, first_name (optional middlename) cases 2 and 4
name_regex_two = re.compile("^" + ",".join([last_name, first_name]) + "(?: " + middle_name + ")?$")
# (firstname or firstIntitial) (middle_name or middle_initial ) last_name  - cases 5, 6 or 7
name_regex_three = re.compile(
  r"^(?P<first_name>[a-zA-Z]+) (?P<middle_initial>[a-zA-Z]\.) (?P<last_name>[a-zA-Z]+)$"
)
name_regex_four = re.compile(
  r"^(?P<first_initial>[a-zA-Z]\.) (?P<middle_name>[a-zA-Z]+) (?P<last_name>[a-zA-Z]+)$"
)
name_regex_five = re.compile(
  r"^(?P<first_name>[a-zA-Z]+) (?P<middle_name>[a-zA-Z]+) (?P<last_name>[a-zA-Z]+)"
)
name_regex_six = re.compile(
  r"^(?P<first_initial>[a-zA-Z]\.) (?P<middle_initial>[a-zA-Z]\.) (?P<last_name>[a-zA-Z]+)$"
)

REGEXES = [
  name_regex_one,
  name_regex_two,
  name_regex_three,
  name_regex_four,
  name_regex_five,
  name_regex_six,
]


class Name(object):
  def __init__(self, **kwargs):

    for k, v in kwargs.items():
      setattr(self, k, v)

  def update(self, **kwargs):
    for k, v in kwargs.items():
      if v is not None:
        setattr(self, k, v)

  def print_out(self, email):
    out_args = []
    if hasattr(self, "first_name") and self.first_name:
      out_args.append(self.first_name)
    elif hasattr(self, "first_initial") and self.first_initial:
      out_args.append(self.first_initial)
    if hasattr(self, "middle_name") and self.middle_name:
      out_args.append(self.middle_name)
    elif hasattr(self, "middle_initial") and self.middle_initial:
      out_args.append(self.middle_initial)
    if hasattr(self, "last_name") and self.last_name:
      out_args.append(self.last_name)

    print(":".join([" ".join(out_args), str(email)]))


def get_email_and_name(l):
  name, email = l.split(":")
  for regex in REGEXES:
    name_dict = regex.match(name)
    if name_dict is not None:
      return name_dict.groupdict(), email


if __name__ == "__main__":
  email_to_names = {}
  email_list = deque()
  while True:
    line = input()
    if not line:
      break
    name, email = get_email_and_name(line)
    if email in email_to_names:
      email_to_names[email].update(**name)
    else:
      email_to_names[email] = Name(**name)
      email_list.append(email)
  for email in email_list:
    email_to_names[email].print_out(email)

"""
The purpose of this excercise is to review the above code as if it were a PR.
"""