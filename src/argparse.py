import traceback
from argparse import ArgumentParser
from dataclasses import dataclass

@dataclass
class Arguments:
  input: str
  verbose: bool

  @staticmethod
  def from_args():
    parser = ArgumentParser()

    parser.add_argument(
      '--input',
      '-i',
      required = True,
      help = 'Input value'
    )

    parser.add_argument(
      '--verbose',
      '-v',
      action = 'store_true',
      required = False,
      help = 'Add tracebacks to error messages'
    )

    return Arguments(**vars(parser.parse_args()))

  def run(self):
    print(self.input)

def main(args):
  try:
    args.run()
  except Exception as error:
    if args.verbose:
      traceback.print_exc()
    print(f'error: {str(error)}')

if __name__ == '__main__':
  main(Arguments.from_args())
