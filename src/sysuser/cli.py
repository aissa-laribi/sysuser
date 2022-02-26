import argparse
from json import JSONDecodeError
# This starts building up our own little parser that does what we want

def create_parser():
  parser = argparse.ArgumentParser()
  # These will add some arguments to the parser. First is the path to the export file.
  # Second is the format of the export file. The default will be JSON, with csv as another
  # option we can pick. The second argument also turns whatever we type (when prompted)
  # to lowercases letters. So if we type CSV or JSON, they'll make it in to the parser as csv
  # or json, respectively.
  parser.add_argument('--path', help='the path to the export file')
  parser.add_argument('--format', default='json', choices=['json','csv'], type=str.lower)
  return parser
def main():
  import sys
# Here, we want to import the export and users modules
  from sysuser  import export, users
  # We're importing as u, because users is probably what
  # the list will be named.
  from sysuser import users as u
  # Here we're going to create a parser, and immediately
  # have it start parsing the args, so that we have access
  # to the args.
  args = create_parser().parse_args()
  # This reads in the user information (from the pwd module
  # that we used in users.py).
  users = u.fetch_users()
  # Now for some conditional logic, based on the path that's
  # passed in, to determine the file that we're using, and
  # and the format that's passed in, so that we know how to
  # export it

    # The first argument is going to be the path.
  if args.path:
        # If the path is present at all, we're going to open the file,
        # make sure it's writable, and set the newline to be an empty
        # string. We don't want any extra strings or characters in what
        # we're doing.
    file = open(args.path,'w',newline='')

        # If we're NOT writing to a file, then the output is going to
        # be STDOUT
  else:
    file = sys.stdout
      # This is where the writing will actually happen. Our first part
      # if the if/else will be testing for whether we're dealing with
      # JSON or not. If it is (which is the default), then we'll call the
      # export module to_json_file and write users out to the file in
      # JSON format.
    if args.format == 'json':
      export.to_csv_file(file, users)
